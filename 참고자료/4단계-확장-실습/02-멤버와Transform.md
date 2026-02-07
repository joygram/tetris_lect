---
layout: default
title: 4단계 확장 실습 02 - 멤버와 Transform
---

# 4단계 확장 실습 02: 멤버와 Transform

## 📌 이 실습은?

**멤버 변수**(저장소)를 두고, **메소드**로 그 값을 바꾼 뒤 **Transform** 위치에 반영하는 실습입니다.  
**이전 단계를 다 보지 않았어도** 이 파일만 따라 하면 진행할 수 있도록 되어 있습니다.

**이전 단계 링크** (필요할 때만 참고):
- [4단계: 블록 이동 구현](../../단계별-학습/4단계-블록-이동-구현.md) — MoveLeft/MoveRight, position 사용 맥락
- [멤버와 메소드 (개념)](../개념/멤버와메소드.md) — 저장소와 그걸 다루는 함수
- [Transform (개념)](../개념/Transform.md) — position, localScale 확장 설명
- [4단계 확장 실습 01: 변수와 Transform](./01-변수와Transform.md) — 변수 + Transform (선택)

---

## 🎯 목표

- **멤버 변수**에 현재 위치(또는 이동량)를 저장한다.
- **메소드**로 그 값을 바꾼 뒤 **transform.position**에 넣는다.
- “저장소(멤버) + 그걸 다루는 함수(메소드)” 짝을 느껴 본다.

---

## 🛠️ 실습: 멤버 + 메소드로 이동하기

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Stage4_02_Member** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다.

---

### 수행 과정

1. **Cube 생성**
   - Hierarchy에서 우클릭 → 3D Object → Cube
   - 이름: **"MemberTransformTest"**

2. **C# 스크립트 생성**
   - 이름: `MemberTransformTest`

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class MemberTransformTest : MonoBehaviour
{
    // 멤버 변수 (저장소): 클래스 안, 메소드 밖 — 여러 메소드에서 씀
    private float moveSpeed = 2f;

    // 메소드: 저장소(moveSpeed)를 이용해 Transform 위치를 바꿈
    void MoveRight()
    {
        transform.position += Vector3.right * moveSpeed;
    }

    void MoveUp()
    {
        transform.position += Vector3.up * moveSpeed;
    }

    void Start()
    {
        // 처음 위치 설정
        transform.position = new Vector3(0, 0, 0);
        Debug.Log("처음 위치: " + transform.position);

        MoveRight();  // 오른쪽으로 moveSpeed만큼
        Debug.Log("MoveRight 후: " + transform.position);

        MoveUp();     // 위로 moveSpeed만큼
        Debug.Log("MoveUp 후: " + transform.position);
    }
}
```

4. **스크립트를 MemberTransformTest(Cube)에 추가 후 Play**
   - Console: 처음 (0,0,0) → MoveRight 후 (2,0,0) → MoveUp 후 (2,2,0) 순서로 출력되는지 확인
   - Scene 뷰에서 Cube가 오른쪽·위로 이동한 것 확인

5. **직접 해보기**: `moveSpeed = 1f;` 로 바꾸거나, `void MoveLeft() { transform.position += Vector3.left * moveSpeed; }` 메소드를 추가한 뒤 Start에서 `MoveLeft();` 를 호출해 보세요.

6. **이어서**: 자식 위치를 배열에 담아 회전하는 실습이 궁금하면 → [4단계 확장 실습 03: 배열과 Transform](./03-배열과Transform.md)

---

[← 4단계 확장 실습 01: 변수와 Transform](./01-변수와Transform.md) | [4단계 확장 실습 03: 배열과 Transform →](./03-배열과Transform.md)
