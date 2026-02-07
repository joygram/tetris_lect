---
layout: default
title: 코드 리뷰 2단계 - GameController
---

# 코드 리뷰 2단계: GameController

8단계 이후 최종 **GameController.cs** 전체 코드와 설명·복습입니다.

**역할**: 점수·줄·레벨을 저장하고, UI 텍스트(점수/줄/레벨)를 갱신하며, 게임 오버 시 화면에 "Game Over"를 띄웁니다. TetrisBlock.LockPiece → AddScore, Spawner → GameOver 호출을 받습니다.

---

## 전체 코드

```csharp
using UnityEngine;
using TMPro;

public class GameController : MonoBehaviour
{
    public int score = 0;
    public int lines = 0;
    public int level = 1;

    public TMP_Text scoreText;   // Inspector에서 연결
    public TMP_Text linesText;
    public TMP_Text levelText;
    public TMP_Text gameOverText;   // 게임 오버 시 표시

    void Start()
    {
        gameOverText.gameObject.SetActive(false);   // 시작할 때 숨김
        UpdateUI();
    }

    public void AddScore(int linesCleared)
    {
        int points = 0;
        switch (linesCleared)
        {
            case 1: points = 100; break;
            case 2: points = 300; break;
            case 3: points = 500; break;
            case 4: points = 800; break;
        }
        score += points * level;
        lines += linesCleared;
        level = (lines / 10) + 1;
        UpdateUI();
    }

    public void GameOver()
    {
        gameOverText.gameObject.SetActive(true);
        gameOverText.text = "Game Over";
    }

    void UpdateUI()
    {
        scoreText.text = $"점수: {score}";
        linesText.text = $"줄: {lines}";
        levelText.text = $"레벨: {level}";
    }
}
```

---

## 코드 설명

### 멤버 변수
- **score, lines, level**: 점수, 지운 줄 누적, 레벨. 레벨은 `(lines / 10) + 1`로 계산합니다.
- **scoreText, linesText, levelText**: 화면에 점수·줄·레벨을 보여주는 TextMeshPro 오브젝트. Inspector에서 드래그로 연결합니다.
- **gameOverText**: 게임 오버일 때만 켜서 "Game Over"를 표시하는 텍스트. 기본은 비활성(SetActive(false)).

### Start()
- 게임 시작 시 **한 번** 실행됩니다.
- gameOverText를 숨기고, UpdateUI()로 점수·줄·레벨 텍스트를 처음 값으로 갱신합니다.

### AddScore(int linesCleared)
- **TetrisBlock.LockPiece**에서 호출됩니다. 지운 줄 개수(linesCleared)를 받아 점수를 올립니다.
- **점수 규칙**: 1줄 100, 2줄 300, 3줄 500, 4줄 800. 여기에 **레벨**을 곱해 `score += points * level`로 계산합니다.
- **lines**에 linesCleared를 더하고, **level**은 `(lines / 10) + 1`로 다시 계산합니다(10줄마다 레벨 1 증가).
- 마지막에 UpdateUI()로 화면 텍스트를 다시 그립니다.

### GameOver()
- **Spawner.SpawnNext**에서 게임 오버일 때 호출됩니다.
- gameOverText 오브젝트를 켜고(SetActive(true)), 텍스트를 "Game Over"로 설정합니다.

### UpdateUI()
- scoreText, linesText, levelText의 **.text**에 현재 score, lines, level 값을 문자열로 넣어 화면에 반영합니다.
- AddScore() 후, Start() 시에 호출됩니다.

---

## 복습

| 구분 | 내용 |
|------|------|
| **TMP_Text** | TextMeshPro용 타입. `using TMPro` 필요. Inspector에서 "Text - TextMeshPro" 오브젝트를 연결할 때 사용. |
| **AddScore 호출 흐름** | LockPiece → ClearFullRows() 반환값 → AddScore(linesCleared) → 점수·줄·레벨 갱신 → UpdateUI(). |
| **GameOver 호출 흐름** | Spawner.SpawnNext()에서 IsGameOver()가 true일 때 gameController.GameOver() 호출 → 화면에 "Game Over" 표시. |
| **레벨 공식** | level = (lines / 10) + 1. 0줄→1레벨, 10줄→2레벨, 20줄→3레벨 … |
| **SetActive** | gameObject.SetActive(false)는 비활성(숨김), true는 활성(보임). gameOverText는 시작 시 숨기고, 게임 오버 시에만 켬. |

---

[← 이전: 코드 리뷰 1단계 (GameBoard)](./GameBoard.md) | [다음: 코드 리뷰 3단계 (InputHandler) →](./InputHandler.md)
