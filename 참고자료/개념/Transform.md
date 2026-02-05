---
layout: default
title: Transform
---

# Transform

## 📖 개념 설명

**Transform**은 GameObject의 위치, 회전, 크기 정보를 담고 있습니다.

```csharp
// 위치 변경
transform.position = new Vector3(5, 10, 0);

// 이동
transform.position += Vector3.right;  // 오른쪽으로 이동

// 회전
transform.rotation = Quaternion.Euler(0, 90, 0);
```

**테트리스 예시**:
```csharp
transform.position = new Vector3(5, 10, 0);
```

---

## 🛠️ 실습: Transform으로 위치·크기 변경하기

**목표**: 스크립트에서 transform.position, localScale을 바꿔 봅니다.

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

**이 실습만** 할 전용 씬이 없으면 아래 순서로 **한 번만** 만듭니다. (이미 `ConceptTest_Transform` 씬이 있으면 **File → Open Scene**으로 열고 아래 실습만 이어서 하세요.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Transform** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다. (다른 문서로 왔다 갔다 하지 않습니다.)

---

### 수행 과정

1. **Cube 생성**
   - Hierarchy에서 우클릭 → 3D Object → Cube
   - 이름: **"TransformTest"**

2. **C# 스크립트 생성**
   - 이름: `TransformTest`

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class TransformTest : MonoBehaviour
{
    void Start()
    {
        // 위치를 (3, 2, 0)으로 설정
        transform.position = new Vector3(3, 2, 0);
        
        // 크기를 (2, 2, 2)로 설정 (2배로 키움)
        transform.localScale = new Vector3(2, 2, 2);
        
        Debug.Log("위치: " + transform.position);
        Debug.Log("크기: " + transform.localScale);
    }
}
```

4. **스크립트를 TransformTest(Cube)에 추가 후 Play**
   - Scene 뷰에서 Cube가 (3, 2, 0) 위치로 이동하고 2배 커진 것 확인
   - Console에서 위치·크기 값 확인

5. **직접 해보기**: `transform.position += Vector3.right;` 를 추가해 한 칸 오른쪽으로 이동시켜 보세요.

---

[← 개념 목록으로](../개념설명.md#-unity-개념)
