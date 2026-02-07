---
layout: default
title: 코드 리뷰 4단계 - Spawner
---

# 코드 리뷰 4단계: Spawner

8단계 이후 최종 **Spawner.cs** 전체 코드와 설명·복습입니다.

**역할**: 다음 블록을 **프리팹 배열**에서 랜덤으로 골라 spawnPoint 위치에 생성합니다. 게임 오버일 때는 스폰하지 않고 GameController.GameOver()를 호출한 뒤 Time.timeScale = 0으로 멈춥니다.

---

## 전체 코드

```csharp
using UnityEngine;

public class Spawner : MonoBehaviour
{
    public GameObject[] tetrisBlockPrefabs;   // Inspector에서 7개 연결
    public Transform spawnPoint;               // 스폰 위치

    private GameBoard gameBoard;
    private GameController gameController;

    void Start()
    {
        gameBoard = FindObjectOfType<GameBoard>();
        gameController = FindObjectOfType<GameController>();
        SpawnNext();
    }

    public void SpawnNext()
    {
        if (gameBoard.IsGameOver())
        {
            Debug.Log("Game Over!");
            gameController.GameOver();
            Time.timeScale = 0;
            return;
        }
        int randomIndex = Random.Range(0, tetrisBlockPrefabs.Length);
        Instantiate(
            tetrisBlockPrefabs[randomIndex],
            spawnPoint.position,
            Quaternion.identity
        );
    }
}
```

---

## 코드 설명

### 멤버 변수
- **tetrisBlockPrefabs**: GameObject 배열. Inspector에서 I_Block, O_Block 등 7종 프리팹을 넣습니다.
- **spawnPoint**: 블록이 생성될 위치(Transform). Inspector에서 빈 오브젝트(예: Spawn Point)를 연결합니다.
- **gameBoard, gameController**: Start에서 FindObjectOfType으로 한 번 찾아 두고, SpawnNext에서 사용합니다.

### Start()
- 게임 시작 시 **한 번** 실행됩니다.
- GameBoard, GameController를 찾은 뒤 **SpawnNext()**를 호출해 **첫 블록**을 만듭니다.

### SpawnNext()
- **TetrisBlock.LockPiece**에서 “블록 고정 후 다음 블록 생성”을 위해 호출됩니다.
- **게임 오버 검사**: `gameBoard.IsGameOver()`가 true면(스폰 영역에 블록이 있으면) Debug.Log, gameController.GameOver()(화면에 "Game Over" 표시), **Time.timeScale = 0**(게임 시간 정지) 후 return. 새 블록을 만들지 않습니다.
- **스폰**: Random.Range(0, tetrisBlockPrefabs.Length)로 0~6 중 하나를 골라, 해당 프리팹을 **spawnPoint.position**에 **Quaternion.identity** 회전으로 Instantiate합니다. 생성된 블록은 TetrisBlock이 붙어 있어서 자동으로 낙하·입력에 반응합니다.

---

## 복습

| 구분 | 내용 |
|------|------|
| **Instantiate** | 프리팹을 씬에 실제 오브젝트로 만드는 Unity API. (프리팹, 위치, 회전)을 넘깁니다. |
| **Random.Range(0, Length)** | 0 이상 Length **미만** 정수. 7개면 0~6. |
| **Time.timeScale = 0** | 게임 시간을 멈춤. Update의 Time.deltaTime이 0이 되어 움직임이 멈춥니다. |
| **호출 흐름** | LockPiece() → Spawner.SpawnNext() → (게임 오버 아니면) Instantiate(다음 블록). |
| **Inspector 연결** | Tetris Block Prefabs 7개, Spawn Point 하나 반드시 연결. |

---

[← 이전: 코드 리뷰 3단계 (InputHandler)](./InputHandler.md) | [다음: 코드 리뷰 5단계 (TetrisBlock) →](./TetrisBlock.md)
