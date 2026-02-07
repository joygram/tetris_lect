---
layout: default
title: 코드 리뷰 1단계 - GameBoard
---

# 코드 리뷰 1단계: GameBoard

8단계 이후 최종 **GameBoard.cs** 전체 코드와 설명·복습입니다.

**역할**: 게임 보드 그리드(width×height)를 2차원 배열로 관리하고, 블록 고정(AddToGrid), 행 제거(ClearFullRows), 게임 오버 판단(IsGameOver), 칸 비었는지(IsCellEmpty)를 담당합니다.

---

## 전체 코드

```csharp
using UnityEngine;

public class GameBoard : MonoBehaviour
{
    public int width = 10;      // 가로 10칸
    public int height = 20;     // 세로 20칸
    private Transform[,] grid;  // 2차원 배열: 각 칸에 고정된 블록 조각(Transform) 저장

    void Awake()
    {
        grid = new Transform[width, height];
        Debug.Log($"게임 보드 생성: {width}x{height}");
    }

    public bool IsValidPosition(Vector2Int position)
    {
        return position.x >= 0 && position.x < width &&
               position.y >= 0 && position.y < height;
    }

    public void AddToGrid(TetrisBlock block)
    {
        Vector3 parentPos = block.transform.position;
        for (int i = block.transform.childCount - 1; i >= 0; i--)   // ⚠ 역순
        {
            Transform child = block.transform.GetChild(i);
            Vector3 childWorld = parentPos + block.transform.TransformDirection(child.localPosition);
            Vector3Int cell = Vector3Int.RoundToInt(childWorld);
            if (cell.x >= 0 && cell.x < width && cell.y >= 0 && cell.y < height)
            {
                child.SetParent(transform);
                grid[cell.x, cell.y] = child;
                child.position = new Vector3(cell.x, cell.y, 0f);
            }
        }
    }

    public bool IsGameOver()
    {
        for (int y = height - 2; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[x, y] != null)
                    return true;
            }
        }
        return false;
    }

    public bool IsCellEmpty(int x, int y)
    {
        if (x < 0 || x >= width || y < 0 || y >= height)
            return false;
        return grid[x, y] == null;
    }

    bool IsRowFull(int row)
    {
        for (int x = 0; x < width; x++)
        {
            if (grid[x, row] == null)
                return false;
        }
        return true;
    }

    void ClearRow(int row)
    {
        for (int x = 0; x < width; x++)
        {
            if (grid[x, row] != null)
            {
                Destroy(grid[x, row].gameObject);
                grid[x, row] = null;
            }
        }
    }

    void MoveRowsDown(int clearedRow)
    {
        for (int y = clearedRow + 1; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[x, y] != null)
                {
                    grid[x, y - 1] = grid[x, y];
                    grid[x, y] = null;
                    grid[x, y - 1].position = new Vector3(x, y - 1, 0f);
                }
            }
        }
    }

    public int ClearFullRows()
    {
        int linesCleared = 0;
        for (int y = 0; y < height; y++)
        {
            if (IsRowFull(y))
            {
                ClearRow(y);
                MoveRowsDown(y);
                y--;
                linesCleared++;
            }
        }
        return linesCleared;
    }
}
```

---

## 코드 설명

### 멤버 변수
- **width, height**: 보드 크기(가로 10, 세로 20). Inspector에서 변경 가능.
- **grid**: `Transform[,]` 2차원 배열. `grid[x, y]`에 해당 칸에 고정된 블록 조각(자식 Transform)을 저장. 비어 있으면 null.

### Awake()
- 씬 로드 시 **한 번** 실행됩니다(Start보다 먼저).
- `grid`를 width×height 크기로 생성하고, Console에 로그를 남깁니다.

### IsValidPosition(Vector2Int position)
- 주어진 (x, y)가 보드 범위 **안**이면 true, 밖이면 false를 반환합니다.
- 0 ≤ x < width, 0 ≤ y < height 인지 검사합니다.

### AddToGrid(TetrisBlock block)
- **블록을 그리드에 고정**할 때 호출됩니다(TetrisBlock.LockPiece에서 호출).
- 블록의 **각 자식(큐브)**을 순회하면서, 월드 좌표를 칸 좌표로 바꾸고 `grid[cell.x, cell.y]`에 넣습니다.
- **역순 for (i = childCount - 1; i >= 0; i--)** 인 이유: 자식을 GameBoard로 SetParent 하면 childCount가 줄어들기 때문에, 정순으로 돌면 일부 자식만 처리됩니다. 역순으로 돌면 안전합니다.
- `child.position = new Vector3(cell.x, cell.y, 0f)`로 칸에 맞춰 스냅합니다.

### IsGameOver()
- **스폰 영역**(맨 위 2줄, y = height-2, height-1)에 블록이 하나라도 있으면 true를 반환합니다.
- Spawner가 다음 블록을 만들기 전에 이 메소드를 호출해, 게임 오버면 스폰하지 않습니다.

### IsCellEmpty(int x, int y)
- 해당 칸이 **비어 있으면** true, 보드 밖이거나 이미 블록이 있으면 false입니다.
- TetrisBlock.ValidMove에서 “이동할 칸이 비어 있는지” 검사할 때 사용합니다.

### IsRowFull(int row) / ClearRow(int row) / MoveRowsDown(int clearedRow)
- **IsRowFull**: 해당 행이 가득 찼는지 검사(한 칸이라도 null이면 false).
- **ClearRow**: 해당 행의 모든 칸에 있는 오브젝트를 Destroy 하고 grid를 null로 만듭니다.
- **MoveRowsDown**: 지운 행 **위쪽**의 모든 행을 한 칸씩 아래로 내립니다. `grid[x, y-1] = grid[x, y]` 후 position을 (x, y-1, 0)으로 스냅합니다.

### ClearFullRows()
- **아래부터** 각 행을 검사해, 가득 찬 행이 있으면 ClearRow → MoveRowsDown 하고, 지운 행 개수를 세어 반환합니다.
- `y--`는 한 행을 지우고 내렸을 때 같은 인덱스가 다시 채워졌을 수 있으므로, 같은 y를 다시 검사하기 위함입니다.
- TetrisBlock.LockPiece에서 이 **반환값(linesCleared)**을 GameController.AddScore에 넘겨 점수를 계산합니다.

---

## 복습

| 구분 | 내용 |
|------|------|
| **Awake vs Start** | Awake는 씬 로드 시 가장 먼저 한 번, Start는 그 다음 한 번. 보드처럼 “다른 스크립트보다 먼저 준비”할 때 Awake에서 grid 생성. |
| **2차원 배열** | `Transform[,] grid`로 [x, y] 칸에 고정된 블록 조각을 저장. null이면 빈 칸. |
| **AddToGrid 역순** | SetParent 하면 childCount가 줄어들므로, 자식을 돌 때 **역순**으로 돌아야 4개 모두 처리됨. |
| **IsGameOver** | 맨 위 2줄(row 18, 19)만 검사. 스폰 위치가 그 근처이므로, 그곳에 블록이 있으면 더 스폰할 수 없음. |
| **ClearFullRows 흐름** | IsRowFull → ClearRow(지우기) → MoveRowsDown(위 행들 내리기) → 지운 줄 수 반환. |

---

[← 이전: 8단계 - 게임 완성](../../단계별-학습/8단계-게임-완성.md) | [다음: 코드 리뷰 2단계 (GameController) →](./GameController.md)
