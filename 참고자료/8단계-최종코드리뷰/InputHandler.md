---
layout: default
title: 코드 리뷰 3단계 - InputHandler
---

# 코드 리뷰 3단계: InputHandler

8단계 이후 최종 **InputHandler.cs** 전체 코드와 설명·복습입니다.

**역할**: 매 프레임 키 입력을 받아, 씬에 있는 **현재 TetrisBlock**의 MoveLeft, MoveRight, MoveDown, Rotate, HardDrop을 호출합니다. 좌우·아래는 쿨다운으로 연속 입력을 보정합니다.

---

## 전체 코드

```csharp
using UnityEngine;

public class InputHandler : MonoBehaviour
{
    private float moveCooldown = 0.1f;   // 연속 입력 간격(초)
    private float moveTimer = 0f;

    void Update()
    {
        moveTimer += Time.deltaTime;

        if (Input.GetKey(KeyCode.LeftArrow) || Input.GetKey(KeyCode.A))
        {
            if (moveTimer >= moveCooldown) { MoveLeft(); moveTimer = 0f; }
        }
        if (Input.GetKey(KeyCode.RightArrow) || Input.GetKey(KeyCode.D))
        {
            if (moveTimer >= moveCooldown) { MoveRight(); moveTimer = 0f; }
        }
        if (Input.GetKey(KeyCode.DownArrow) || Input.GetKey(KeyCode.S))
        {
            TetrisBlock current = FindObjectOfType<TetrisBlock>();
            if (current != null && moveTimer >= moveCooldown)
            {
                current.MoveDown();
                moveTimer = 0f;
            }
        }
        if (Input.GetKeyDown(KeyCode.UpArrow) || Input.GetKeyDown(KeyCode.W))
        {
            Rotate();
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            TetrisBlock current = FindObjectOfType<TetrisBlock>();
            if (current != null)
            {
                current.HardDrop();
            }
        }
    }

    void MoveLeft()
    {
        TetrisBlock current = FindObjectOfType<TetrisBlock>();
        if (current != null) current.MoveLeft();
    }
    void MoveRight()
    {
        TetrisBlock current = FindObjectOfType<TetrisBlock>();
        if (current != null) current.MoveRight();
    }
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

| 구분 | 내용 |
|------|------|
| **GetKey vs GetKeyDown** | GetKey: 키가 눌린 **매 프레임** true. GetKeyDown: 키가 **눌린 그 프레임 한 번만** true. 좌우·아래는 GetKey+쿨다운, 회전·스페이스는 GetKeyDown. |
| **쿨다운** | moveTimer += Time.deltaTime로 시간을 쌓고, moveTimer >= moveCooldown일 때만 이동·moveTimer = 0. 연속 입력 시 0.1초 간격으로만 반응. |
| **FindObjectOfType&lt;TetrisBlock&gt;()** | 씬에 있는 TetrisBlock 컴포넌트를 하나 찾습니다. LockPiece 후에는 현재 블록이 없을 수 있어 null 체크를 합니다. |
| **호출 흐름** | InputHandler(키 감지) → TetrisBlock.MoveLeft/MoveRight/MoveDown/Rotate/HardDrop(실제 이동·회전·고정). |

---

[← 이전: 코드 리뷰 2단계 (GameController)](./GameController.md) | [다음: 코드 리뷰 4단계 (Spawner) →](./Spawner.md)
