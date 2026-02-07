---
layout: default
title: 4단계 확장 실습 03 - 배열과 Transform
---

# 4단계 확장 실습 03: 배열과 Transform

## 📌 이 실습은?

**배열**에 자식 오브젝트의 **localPosition**을 넣고, 90도 회전한 뒤 다시 적용하는 실습입니다.  
**이전 단계를 다 보지 않았어도** 이 파일만 따라 하면 진행할 수 있도록 되어 있습니다.

**이전 단계 링크** (필요할 때만 참고):
- [4단계: 블록 이동 구현](../../단계별-학습/4단계-블록-이동-구현.md) — Rotate(), GetChild, localPosition, 회전 공식
- [배열 (개념)](../개념/배열.md) — 배열이란 무엇인지
- [Transform (개념)](../개념/Transform.md) — GetChild, childCount, localPosition 확장 설명
- [회전 수학 (개념)](../개념/회전수학.md) — 90도 시계 방향 (x,y)→(-y,x)
- [4단계 확장 실습 02: 멤버와 Transform](./02-멤버와Transform.md) — 멤버 + Transform (선택)

---

## 🎯 목표

- **배열**에 자식들의 **localPosition**을 저장한다.
- 90도 시계 방향 회전 공식 **(x, y) → (-y, x)** 로 새 위치를 배열에 넣는다.
- 그 배열 값을 다시 자식 **localPosition**에 넣어 회전 효과를 낸다.

---

## 🛠️ 실습: 배열로 자식 위치 회전하기

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Stage4_03_Array** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다.

---

### 계층 구조 만들기 (부모 + 자식 4개)

1. **빈 오브젝트 생성** (부모)
   - Hierarchy 우클릭 → Create Empty
   - 이름: **"ArrayTransformTest"**
2. **자식 Cube 4개 만들기**
   - Hierarchy에서 우클릭 → 3D Object → Cube
   - 이름: **"Block0"** → ArrayTransformTest 오브젝트를 끌어다 **Block0** 위에 놓아 자식으로 만듦
   - Block0 선택 → Inspector에서 **Transform > Position** 을 **(0, 0, 0)** 으로 설정
   - 같은 방법으로 **Block1** 만들고 Position **(1, 0, 0)**
   - **Block2** 만들고 Position **(2, 0, 0)**
   - **Block3** 만들고 Position **(1, 1, 0)**
   - 최종 구조: **ArrayTransformTest** 아래 **Block0, Block1, Block2, Block3** (L자 모양처럼)

---

### 수행 과정

1. **C# 스크립트 생성**
   - 이름: `ArrayTransformTest`

2. **스크립트를 부모(ArrayTransformTest)에 추가**

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class ArrayTransformTest : MonoBehaviour
{
    void Start()
    {
        // 자식 개수만큼 배열 만들기
        int count = transform.childCount;
        Vector3[] newLocalPositions = new Vector3[count];

        // 각 자식의 localPosition을 90도 시계 방향 회전: (x, y) → (-y, x)
        for (int i = 0; i < count; i++)
        {
            Transform child = transform.GetChild(i);
            Vector3 localPos = child.localPosition;
            float newX = -localPos.y;
            float newY = localPos.x;
            newLocalPositions[i] = new Vector3(newX, newY, 0);
        }

        // 회전한 위치를 자식들에게 적용
        for (int i = 0; i < count; i++)
        {
            Transform child = transform.GetChild(i);
            child.localPosition = newLocalPositions[i];
        }

        Debug.Log("자식 " + count + "개 위치를 90도 시계 방향 회전 적용했습니다.");
    }
}
```

4. **Play**
   - Scene 뷰에서 L자 블록들이 90도 회전한 모양으로 바뀌는지 확인
   - Console 메시지 확인

5. **직접 해보기**: `newLocalPositions` 배열을 채운 뒤, **한 번에 적용하기 전**에 `Debug.Log("회전 후 위치[" + i + "]: " + newLocalPositions[i]);` 를 for문 안에 넣어 각 자식의 새 위치를 출력해 보세요.

6. **정리**: 4단계 테트리스 **Rotate()** 에서도 같은 방식으로 `Vector3[] newLocalPositions` 배열에 회전한 위치를 넣고, 유효하면 자식 `localPosition`에 적용합니다. → [4단계 Rotate 코드](../../단계별-학습/4단계-블록-이동-구현.md#4-회전-기능-구현)

---

[← 4단계 확장 실습 02: 멤버와 Transform](./02-멤버와Transform.md) | [Transform 개념으로](../개념/Transform.md)
