---
layout: default
title: 2단계 확장 실습 01 - Awake와 배열·범위 검사
---

# 2단계 확장 실습 01: Awake와 배열·범위 검사

## 📌 이 실습은?

**Awake()** 에서 **2차원 배열**을 만들고, **범위 검사** 함수를 써 보는 실습입니다.  
**이전 단계를 다 보지 않았어도** 이 파일만 따라 하면 진행할 수 있습니다.

**이전 단계 링크** (필요할 때만 참고):
- [2단계: 게임 보드 만들기](../../../단계별-학습/2단계-게임-보드-만들기.md) — Awake(), grid, IsValidPosition
- [배열 (개념)](../개념/배열.md) — 1·2차원 배열
- [MonoBehaviour (개념)](../개념/MonoBehaviour.md) — Awake() vs Start()
- [1단계 확장 실습 01](../1단계/01-Start와변수출력.md) — Start와 변수 (선택)

---

## 🎯 목표

- **Awake()** 에서 **2차원 배열**을 생성한다.
- "이 좌표가 보드 안인가?"를 검사하는 **함수**를 만들고 호출한다.

---

## 🛠️ 실습

### 이 실습 전용 씬 만들기 (환경 설정)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Stage2_AwakeArray** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다.

---

### 수행 과정

1. **빈 GameObject 생성**  
   - Hierarchy 우클릭 → Create Empty → 이름: **"Stage2ExpandTest"**

2. **C# 스크립트 생성**  
   - 이름: `Stage2ExpandTest`

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class Stage2ExpandTest : MonoBehaviour
{
    private int width = 5;
    private int height = 5;
    private int[,] grid;  // 2차원 배열 (참고: GameBoard는 Transform[,])

    void Awake()
    {
        grid = new int[width, height];
        Debug.Log($"보드 생성: {width}x{height}");
    }

    void Start()
    {
        // 범위 안인지 검사
        Debug.Log("(2, 3) 유효? " + IsValidPosition(2, 3));   // true
        Debug.Log("(-1, 0) 유효? " + IsValidPosition(-1, 0)); // false
        Debug.Log("(5, 5) 유효? " + IsValidPosition(5, 5));   // false
    }

    bool IsValidPosition(int x, int y)
    {
        return x >= 0 && x < width && y >= 0 && y < height;
    }
}
```

4. **스크립트를 Stage2ExpandTest에 추가 후 Play**  
   - Console에서 보드 생성 메시지와 (2,3)=true, (-1,0)=false, (5,5)=false 확인

5. **직접 해보기**: `IsValidPosition(0, 0)` 과 `IsValidPosition(4, 4)` 를 Start()에서 호출해 보세요. (둘 다 true여야 합니다.)

6. **이어서**: 3단계에서 쓰는 GetChild·자식 순회 실습이 궁금하면 → [3단계 확장 실습 01 - GetChild과 자식 순회](../3단계/01-GetChild과자식순회.md)

---

[← 1단계 확장 실습](../1단계/01-Start와변수출력.md) | [단계별 확장 실습 목차](../README.md) | [3단계 확장 실습 →](../3단계/01-GetChild과자식순회.md)
