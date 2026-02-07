---
layout: default
title: 3단계 확장 실습 01 - GetChild과 자식 순회
---

# 3단계 확장 실습 01: GetChild과 자식 순회

## 📌 이 실습은?

**부모 오브젝트**의 **자식 개수(childCount)** 와 **GetChild(i)** 로 자식을 순회해 보는 실습입니다.  
**이전 단계를 다 보지 않았어도** 이 파일만 따라 하면 진행할 수 있습니다.

**이전 단계 링크** (필요할 때만 참고):
- [3단계: 테트리스 블록 만들기](../../../단계별-학습/3단계-테트리스-블록-만들기.md) — 프리팹, 부모-자식 구조
- [Transform (개념)](../개념/Transform.md) — GetChild, childCount, localPosition
- [2단계 확장 실습 01](../2단계/01-Awake와배열범위검사.md) — Awake와 배열 (선택)

---

## 🎯 목표

- **transform.childCount** 로 자식 개수를 읽는다.
- **transform.GetChild(i)** 로 i번째 자식 Transform을 가져와 **localPosition**을 출력한다.

---

## 🛠️ 실습

### 이 실습 전용 씬 만들기 (환경 설정)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Stage3_GetChild** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다.

---

### 계층 구조 만들기 (부모 + 자식 3개)

1. **빈 오브젝트** 생성 → 이름: **"Stage3ExpandTest"**
2. **Stage3ExpandTest 선택 상태**에서 Hierarchy 우클릭 → 3D Object → Cube → 이름: **"Block0"** (자식으로 붙음)
3. 같은 방법으로 **Block1**, **Block2** 추가 (총 자식 3개)
4. Block0 Position **(0, 0, 0)**, Block1 **(1, 0, 0)**, Block2 **(0, 1, 0)** 으로 설정 (Inspector에서)

---

### 수행 과정

1. **C# 스크립트 생성**  
   - 이름: `Stage3ExpandTest`

2. **스크립트를 부모(Stage3ExpandTest)에 추가**

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class Stage3ExpandTest : MonoBehaviour
{
    void Start()
    {
        int count = transform.childCount;
        Debug.Log("자식 개수: " + count);

        for (int i = 0; i < count; i++)
        {
            Transform child = transform.GetChild(i);
            Debug.Log($"자식 {i}: {child.name}, localPosition = {child.localPosition}");
        }
    }
}
```

4. **Play**  
   - Console: "자식 개수: 3", 자식 0·1·2 이름과 localPosition 출력 확인

5. **직접 해보기**: 자식 Cube를 하나 더 추가한 뒤 다시 Play 해 보세요. 자식 개수가 4로 나오는지 확인합니다.

6. **이어서**: 4단계에서 쓰는 변수·멤버·배열 + Transform 실습이 궁금하면 → [4단계 확장 실습 (목차)](../../4단계-확장-실습/README.md)

---

[← 2단계 확장 실습](../2단계/01-Awake와배열범위검사.md) | [단계별 확장 실습 목차](../README.md) | [4단계 확장 실습 →](../../4단계-확장-실습/README.md)
