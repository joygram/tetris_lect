---
layout: default
title: 4단계 확장 실습 01 - 변수와 Transform
---

# 4단계 확장 실습 01: 변수와 Transform

## 📌 이 실습은?

**변수**에 값을 저장하고, 그 값을 **Transform**(위치·크기)에 넣어 보는 실습입니다.  
**이전 단계(1~3단계)를 다 보지 않았어도** 이 파일만 따라 하면 진행할 수 있도록 되어 있습니다.

**이전 단계 링크** (필요할 때만 참고):
- [1단계: Unity 기초](../../단계별-학습/1단계-Unity-기초.md) — 씬, 오브젝트, 스크립트 기본
- [4단계: 블록 이동 구현](../../단계별-학습/4단계-블록-이동-구현.md) — position, localPosition 사용 맥락
- [변수 (개념)](../개념/변수.md) — 변수란 무엇인지
- [Transform (개념)](../개념/Transform.md) — position, localScale 확장 설명

---

## 🎯 목표

- **로컬 변수**에 위치·크기 값을 저장한다.
- 그 변수 값을 **transform.position**, **transform.localScale**에 넣어 본다.

---

## 🛠️ 실습: 변수로 위치·크기 정하기

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Stage4_01_Variable** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다.

---

### 수행 과정

1. **Cube 생성**
   - Hierarchy에서 우클릭 → 3D Object → Cube
   - 이름: **"VariableTransformTest"**

2. **C# 스크립트 생성**
   - 이름: `VariableTransformTest`

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class VariableTransformTest : MonoBehaviour
{
    void Start()
    {
        // 변수에 위치·크기 값을 저장 (로컬 변수 = Start() 안에서만 사용)
        float posX = 3f;
        float posY = 2f;
        float posZ = 0f;
        float scaleSize = 2f;  // 2배 크기

        // 변수 값을 Transform에 넣기
        transform.position = new Vector3(posX, posY, posZ);
        transform.localScale = new Vector3(scaleSize, scaleSize, scaleSize);

        Debug.Log("위치: " + transform.position);
        Debug.Log("크기: " + transform.localScale);
    }
}
```

4. **스크립트를 VariableTransformTest(Cube)에 추가 후 Play**
   - Scene 뷰에서 Cube가 (3, 2, 0)으로 이동하고 2배 커진 것 확인
   - Console에서 위치·크기 값 확인

5. **직접 해보기**: `posX = 5f;` 로 바꾼 뒤 다시 Play 해 보세요. Cube가 더 오른쪽으로 이동하는지 확인합니다.

6. **이어서**: 저장소(멤버)를 두고 그걸 메소드로 바꾸는 실습이 궁금하면 → [4단계 확장 실습 02: 멤버와 Transform](./02-멤버와Transform.md)

---

[← Transform 개념으로](../개념/Transform.md) | [4단계 확장 실습 02: 멤버와 Transform →](./02-멤버와Transform.md)
