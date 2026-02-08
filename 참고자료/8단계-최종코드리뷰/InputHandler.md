---
layout: default
title: 코드 리뷰 3단계 - InputHandler
---

# 코드 리뷰 3단계: InputHandler

8단계 이후 최종 **InputHandler.cs** 전체 코드와 설명·복습입니다.

**역할**: 매 프레임 키 입력을 받아, 씬에 있는 **현재 TetrisBlock**의 MoveLeft, MoveRight, MoveDown, Rotate, HardDrop을 호출합니다. 좌우·아래는 쿨다운으로 연속 입력을 보정합니다.

**관련 단계 복기**: [5단계 - 입력 처리](../../단계별-학습/5단계-입력-처리.md)(InputHandler, GetKey/GetKeyDown, 쿨다운, FindObjectOfType&lt;TetrisBlock&gt;) → [8단계 - 게임 완성](../../단계별-학습/8단계-게임-완성.md)(스페이스 → HardDrop).

---

## 전체 코드

```csharp
using UnityEngine;

/// <summary>
/// 키 입력을 받아 현재 TetrisBlock의 이동·회전·하드드롭을 호출.
/// 좌우·아래는 쿨다운으로 연속 입력 시 0.1초 간격만 반응.
/// </summary>
public class InputHandler : MonoBehaviour
{
    private float moveCooldown = 0.1f;   // 연속 입력 시 이동 허용 간격(초). 키를 누르고 있으면 0.1초마다 한 번만 이동
    private float moveTimer = 0f;        // 쿨다운 경과 시간 누적

    /// <summary>매 프레임 키 입력 검사. 좌우·아래는 GetKey+쿨다운, 회전·스페이스는 GetKeyDown(한 번만).</summary>
    void Update()
    {
        moveTimer += Time.deltaTime;

        // 좌우 이동: 키가 눌린 동안 쿨다운마다 한 번씩만 이동
        if (Input.GetKey(KeyCode.LeftArrow) || Input.GetKey(KeyCode.A))
        {
            if (moveTimer >= moveCooldown) { MoveLeft(); moveTimer = 0f; }
        }
        if (Input.GetKey(KeyCode.RightArrow) || Input.GetKey(KeyCode.D))
        {
            if (moveTimer >= moveCooldown) { MoveRight(); moveTimer = 0f; }
        }
        // 아래 이동: 쿨다운 적용, 현재 블록이 있을 때만
        if (Input.GetKey(KeyCode.DownArrow) || Input.GetKey(KeyCode.S))
        {
            TetrisBlock current = FindObjectOfType<TetrisBlock>();
            if (current != null && moveTimer >= moveCooldown)
            {
                current.MoveDown();
                moveTimer = 0f;
            }
        }
        // 회전: 키를 누른 그 프레임 한 번만
        if (Input.GetKeyDown(KeyCode.UpArrow) || Input.GetKeyDown(KeyCode.W))
        {
            Rotate();
        }
        // 하드 드롭(바닥까지 즉시 낙하): 스페이스 한 번만
        if (Input.GetKeyDown(KeyCode.Space))
        {
            TetrisBlock current = FindObjectOfType<TetrisBlock>();
            if (current != null)
            {
                current.HardDrop();
            }
        }
    }

    /// <summary>씬에서 현재 TetrisBlock을 찾아 왼쪽으로 한 칸 이동 요청.</summary>
    void MoveLeft()
    {
        TetrisBlock current = FindObjectOfType<TetrisBlock>();
        if (current != null) current.MoveLeft();
    }
    /// <summary>씬에서 현재 TetrisBlock을 찾아 오른쪽으로 한 칸 이동 요청.</summary>
    void MoveRight()
    {
        TetrisBlock current = FindObjectOfType<TetrisBlock>();
        if (current != null) current.MoveRight();
    }
    /// <summary>씬에서 현재 TetrisBlock을 찾아 90도 회전 요청.</summary>
    void Rotate()
    {
        TetrisBlock current = FindObjectOfType<TetrisBlock>();
        if (current != null) current.Rotate();
    }
}
```

---

## 코드 설명

### 멤버 변수
- **moveCooldown**: 좌우·아래 이동 시 연속 입력으로 인한 과도한 이동을 막기 위한 간격(0.1초).
- **moveTimer**: 매 프레임 Time.deltaTime만큼 증가. moveCooldown 이상이 되면 이동을 허용하고 0으로 리셋합니다.

### Update()
- **매 프레임** 실행됩니다.
- **좌우(LeftArrow/A, RightArrow/D)**: GetKey로 눌린 동안 검사. moveTimer가 moveCooldown 이상일 때만 MoveLeft/MoveRight를 호출하고 moveTimer를 0으로 만듭니다.
- **아래(DownArrow/S)**: GetKey로 눌린 동안, FindObjectOfType&lt;TetrisBlock&gt;()으로 현재 블록을 찾고, moveCooldown 이상이면 MoveDown()을 호출합니다.
- **회전(UpArrow/W)**: GetKeyDown으로 **한 번 눌릴 때만** Rotate()를 호출합니다.
- **스페이스**: GetKeyDown으로 **한 번 눌릴 때만** 현재 블록을 찾아 HardDrop()을 호출합니다.

### MoveLeft(), MoveRight(), Rotate()
- 씬에서 TetrisBlock을 FindObjectOfType으로 찾고, 있으면 해당 메소드(MoveLeft, MoveRight, Rotate)를 호출합니다.
- 현재 조작 중인 블록은 **항상 씬에 하나**이므로(나머지는 LockPiece로 그리드에 붙고 블록 오브젝트는 Destroy됨), 찾은 것이 곧 “현재 블록”입니다.

---

## 복습

아래는 **5단계·8단계**에서 배운 내용을 정리한 복기 표입니다.

| 구분 | 내용 | 관련 단계 |
|------|------|-----------|
| **GetKey vs GetKeyDown** | GetKey: 키가 눌린 **매 프레임** true. GetKeyDown: 키가 **눌린 그 프레임 한 번만** true. 좌우·아래는 GetKey+쿨다운, 회전·스페이스는 GetKeyDown. | 5단계 |
| **쿨다운** | moveTimer += Time.deltaTime로 시간을 쌓고, moveTimer >= moveCooldown일 때만 이동·moveTimer = 0. 연속 입력 시 0.1초 간격으로만 반응. | 5단계 |
| **FindObjectOfType&lt;TetrisBlock&gt;()** | 씬에 있는 TetrisBlock 컴포넌트를 하나 찾습니다. LockPiece 후에는 현재 블록이 없을 수 있어 null 체크를 합니다. | 5단계 |
| **호출 흐름** | InputHandler(키 감지) → TetrisBlock.MoveLeft/MoveRight/MoveDown/Rotate/HardDrop(실제 이동·회전·고정). | 5·8단계 |

---

[← 이전: 코드 리뷰 2단계 (GameController)](./GameController.md) | [다음: 코드 리뷰 4단계 (Spawner) →](./Spawner.md)
