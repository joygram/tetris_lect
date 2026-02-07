---
layout: default
title: 5단계 확장 실습 01 - Input과 쿨다운
---

# 5단계 확장 실습 01: Input과 쿨다운

## 📌 이 실습은?

**Input.GetKey** 와 **Time.deltaTime** 으로 **쿨다운**을 두고, 키를 누를 때마다 일정 간격으로만 동작하도록 하는 실습입니다.  
**이전 단계를 다 보지 않았어도** 이 파일만 따라 하면 진행할 수 있습니다.

**이전 단계 링크** (필요할 때만 참고):
- [5단계: 입력 처리](../../../단계별-학습/5단계-입력-처리.md) — InputHandler, moveCooldown, Input.GetKey
- [Time.deltaTime (개념)](../개념/Time-deltaTime.md) — deltaTime으로 1초마다 실행
- [4단계 확장 실습 (목차)](../4단계-확장-실습/README.md) — 멤버 + 메소드 (선택)

---

## 🎯 목표

- **멤버 변수** moveTimer, moveCooldown을 둔다.
- **Update()** 에서 moveTimer += Time.deltaTime 하고, moveCooldown 이상일 때만 **Input.GetKey** 로 동작을 실행한 뒤 moveTimer를 0으로 만든다.

---

## 🛠️ 실습

### 이 실습 전용 씬 만들기 (환경 설정)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Stage5_InputCooldown** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다.

---

### 수행 과정

1. **빈 GameObject 생성**  
   - Hierarchy 우클릭 → Create Empty → 이름: **"Stage5ExpandTest"**

2. **C# 스크립트 생성**  
   - 이름: `Stage5ExpandTest`

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class Stage5ExpandTest : MonoBehaviour
{
    private float moveCooldown = 0.5f;  // 0.5초마다 한 번만 반응
    private float moveTimer = 0f;

    void Update()
    {
        moveTimer += Time.deltaTime;

        if (Input.GetKey(KeyCode.Space) && moveTimer >= moveCooldown)
        {
            Debug.Log("Space 눌림 (쿨다운 적용)");
            moveTimer = 0f;
        }
    }
}
```

4. **스크립트를 Stage5ExpandTest에 추가 후 Play**  
   - Space를 누르면 Console에 "Space 눌림" 출력. 연타해도 **0.5초 간격**으로만 출력되는지 확인

5. **직접 해보기**: `moveCooldown = 1f` 로 바꾼 뒤 1초 간격으로만 출력되는지 확인해 보세요.

6. **이어서**: 6단계에서 쓰는 그리드·행 검사 실습이 궁금하면 → [6단계 확장 실습 01 - 그리드와 행 검사](../6단계/01-그리드와행검사.md)

---

[← 4단계 확장 실습](../4단계-확장-실습/README.md) | [단계별 확장 실습 목차](../README.md) | [6단계 확장 실습 →](../6단계/01-그리드와행검사.md)
