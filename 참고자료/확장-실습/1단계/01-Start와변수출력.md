---
layout: default
title: 1단계 확장 실습 01 - Start와 변수 출력
---

# 1단계 확장 실습 01: Start와 변수 출력

## 📌 이 실습은?

**Start()** 안에서 **변수**에 값을 넣고 **Debug.Log**로 출력해 보는 실습입니다.  
**이전 단계를 다 보지 않았어도** 이 파일만 따라 하면 진행할 수 있습니다.

**이전 단계 링크** (필요할 때만 참고):
- [1단계: Unity 기초](../../../단계별-학습/1단계-Unity-기초.md) — 씬, 스크립트, Start()
- [변수 (개념)](../개념/변수.md) — 변수란 무엇인지
- [MonoBehaviour (개념)](../개념/MonoBehaviour.md) — Start() 용도

---

## 🎯 목표

- **Start()** 에서 **로컬 변수**에 값을 저장한다.
- **Debug.Log**로 그 값을 Console에 출력한다.

---

## 🛠️ 실습

### 이 실습 전용 씬 만들기 (환경 설정)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Stage1_StartVariable** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md) 참고.)

---

### 수행 과정

1. **빈 GameObject 생성**  
   - Hierarchy 우클릭 → Create Empty → 이름: **"Stage1ExpandTest"**

2. **C# 스크립트 생성**  
   - 이름: `Stage1ExpandTest`

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class Stage1ExpandTest : MonoBehaviour
{
    void Start()
    {
        // 변수에 값 저장 (로컬 변수 = Start() 안에서만 사용)
        int score = 100;
        string playerName = "플레이어";

        Debug.Log("점수: " + score);
        Debug.Log("이름: " + playerName);
    }
}
```

4. **스크립트를 Stage1ExpandTest에 추가 후 Play**  
   - Console에서 "점수: 100", "이름: 플레이어" 출력 확인

5. **직접 해보기**: `float speed = 1.5f;` 변수를 추가하고 Debug.Log로 출력해 보세요.

6. **이어서**: 2단계에서 쓰는 Awake·배열 실습이 궁금하면 → [2단계 확장 실습 01 - Awake와 배열·범위 검사](../2단계/01-Awake와배열범위검사.md)

---

[← 1단계로](../../../단계별-학습/1단계-Unity-기초.md) | [단계별 확장 실습 목차](../README.md) | [2단계 확장 실습 →](../2단계/01-Awake와배열범위검사.md)
