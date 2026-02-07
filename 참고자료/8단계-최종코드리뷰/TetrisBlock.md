---
layout: default
title: 코드 리뷰 5단계 - TetrisBlock
---

# 코드 리뷰 5단계: TetrisBlock

8단계 이후 최종 **TetrisBlock.cs** 전체 코드와 설명·복습입니다.

**역할**: **한 블록**의 이동·회전·낙하·고정을 담당합니다. ValidMove로 이동 가능 여부를 검사하고, LockPiece에서 GameBoard·GameController·Spawner와 연결합니다.

**관련 단계 복기**: [4단계 - 블록 이동 구현](../../단계별-학습/4단계-블록-이동-구현.md)(ValidMove, MoveLeft/Right/Down, Rotate, 자동 낙하) → [6단계 - 행 제거 시스템](../../단계별-학습/6단계-행-제거-시스템.md)(LockPiece, AddToGrid, ClearFullRows, SpawnNext) → [7단계 - 점수·레벨 시스템](../../단계별-학습/7단계-점수-레벨-시스템.md)(AddScore 연동) → [8단계 - 게임 완성](../../단계별-학습/8단계-게임-완성.md)(HardDrop).

---

## 전체 코드

```csharp
using UnityEngine;

public class TetrisBlock : MonoBehaviour
{
    private GameBoard gameBoard;
    public float fallSpeed = 1f;   // 몇 초에 한 칸 낙하
    private float fallTimer = 0f;

    void Start()
    {
        gameBoard = FindObjectOfType<GameBoard>();
    }

    public bool ValidMove(Vector3 offset)
    {
        Vector3 parentNew = transform.position + offset;
        for (int i = 0; i < transform.childCount; i++)
        {
            Transform child = transform.GetChild(i);
            Vector3 childWorld = parentNew + transform.TransformDirection(child.localPosition);
            Vector3Int cell = Vector3Int.RoundToInt(childWorld);
            if (cell.x < 0 || cell.x >= gameBoard.width || cell.y < 0 || cell.y >= gameBoard.height)
                return false;
            if (!gameBoard.IsCellEmpty(cell.x, cell.y))
                return false;
        }
        return true;
    }

    public void MoveLeft()
    {
        if (ValidMove(Vector3.left))
            transform.position += Vector3.left;
    }
    public void MoveRight()
    {
        if (ValidMove(Vector3.right))
            transform.position += Vector3.right;
    }
    public void MoveDown()
    {
        if (ValidMove(Vector3.down))
            transform.position += Vector3.down;
        else
            LockPiece();
    }
    public void HardDrop()
    {
        while (ValidMove(Vector3.down))
            transform.position += Vector3.down;
        LockPiece();
    }

    void Update()
    {
        GameController gameController = FindObjectOfType<GameController>();
        float currentFallSpeed = fallSpeed / gameController.level;
        fallTimer += Time.deltaTime;
        if (fallTimer >= currentFallSpeed)
        {
            MoveDown();
            fallTimer = 0f;
        }
    }

    public void Rotate()
    {
        transform.Rotate(0f, 0f, -90f);
        if (!ValidMove(Vector3.zero))   // 회전 후 위치가 유효하지 않으면 되돌리기
            transform.Rotate(0f, 0f, 90f);
    }

    public void LockPiece()   // 고정 → 행 제거 → 점수 → 다음 블록 스폰 (순서 유지)
    {
        gameBoard.AddToGrid(this);
        int linesCleared = gameBoard.ClearFullRows();

        FindObjectOfType<GameController>().AddScore(linesCleared);
        FindObjectOfType<Spawner>().SpawnNext();

        Destroy(gameObject);
    }
}
```

---

## 코드 설명

### 멤버 변수
- **gameBoard**: Start에서 FindObjectOfType&lt;GameBoard&gt;()로 찾아 둠. ValidMove, LockPiece에서 사용.
- **fallSpeed**: 기본 낙하 간격(초). 레벨에 따라 나눠서 사용해 레벨이 올라갈수록 빨라짐.
- **fallTimer**: Update에서 쌓는 타이머. currentFallSpeed 이상이 되면 한 칸 MoveDown 후 0으로 리셋.

### Start()
- 씬에 올라온 뒤 **한 번** 실행. gameBoard를 찾아 둡니다.

### ValidMove(Vector3 offset)
- 이 블록이 **position + offset**으로 갔을 때 유효한지 검사합니다.
- **부모 예정 위치** = transform.position + offset. 각 **자식(큐브)**의 월드 좌표를 구해(Vector3Int로 반올림) 칸 좌표로 만든 뒤:
  - 보드 밖(cell.x/y 범위 밖)이면 false.
  - 해당 칸이 비어 있지 않으면(gameBoard.IsCellEmpty가 false) false.
- 모두 통과하면 true. 이동·회전 전에 항상 이걸로 검사합니다.

### MoveLeft / MoveRight
- ValidMove(Vector3.left/right)가 true일 때만 position을 한 칸 이동합니다.

### MoveDown
- ValidMove(Vector3.down)가 true면 한 칸 내립니다.
- **false면** 더 이상 내려갈 수 없다는 뜻이므로 **LockPiece()**를 호출해 고정하고, 행 제거·다음 블록 생성으로 이어지게 합니다.

### HardDrop
- ValidMove(Vector3.down)가 true인 동안 계속 한 칸씩 내린 뒤, 막히면 LockPiece()를 호출합니다. InputHandler에서 스페이스 키로 호출합니다.

### Update()
- **자동 낙하**를 담당합니다.
- GameController에서 level을 가져와 `currentFallSpeed = fallSpeed / level`로 계산(레벨이 높을수록 빠름).
- fallTimer가 currentFallSpeed 이상이 되면 MoveDown() 한 번 호출하고 fallTimer를 0으로 리셋합니다.

### Rotate()
- Z축 -90도 회전(시계 방향) 후, ValidMove(Vector3.zero)로 현재 위치가 유효한지 봅니다. 유효하지 않으면 +90도 돌려 원래대로 되돌립니다.

### LockPiece()
- **gameBoard.AddToGrid(this)**: 이 블록의 자식들을 그리드에 붙이고 칸에 스냅합니다.
- **gameBoard.ClearFullRows()**: 가득 찬 행을 지우고, 지운 줄 수를 받습니다.
- **GameController.AddScore(linesCleared)**: 점수·줄·레벨 갱신.
- **Spawner.SpawnNext()**: 다음 블록을 생성합니다.
- **Destroy(gameObject)**: 이 블록 오브젝트는 제거합니다(자식들은 이미 GameBoard 그리드로 옮겨졌음).

---

## 복습

아래는 **4·6·7·8단계**에서 배운 내용을 정리한 복기 표입니다.

| 구분 | 내용 | 관련 단계 |
|------|------|-----------|
| **ValidMove** | 이동/회전 **전**에 “그 위치가 보드 안이고, 칸이 비어 있는지” 검사. 범위 밖이거나 이미 쌓인 칸이면 false. | 4·6단계 |
| **자식 좌표** | 부모 position + TransformDirection(자식 localPosition)으로 자식의 월드 좌표를 구하고, RoundToInt로 칸 인덱스로 씀. | 4단계 |
| **MoveDown과 LockPiece** | MoveDown에서 ValidMove(down)가 false면 “바닥 또는 블록에 닿음”이므로 LockPiece()로 고정. | 6단계 |
| **레벨과 낙하** | Update에서 fallSpeed / gameController.level로 간격을 줄여, 레벨이 높을수록 빨리 낙하. | 7단계 |
| **LockPiece 흐름** | AddToGrid → ClearFullRows → AddScore(linesCleared) → SpawnNext() → Destroy. 순서가 바뀌면 안 됨. | 6·7·8단계 |

---

[← 이전: 코드 리뷰 4단계 (Spawner)](./Spawner.md) | [목차](./README.md)
