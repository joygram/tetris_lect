---
layout: default
title: FindObjectOfType
---

# FindObjectOfType

## 📖 개념 설명

**FindObjectOfType**은 씬에서 특정 타입의 컴포넌트를 가진 오브젝트를 찾습니다.

```csharp
GameBoard gameBoard = FindObjectOfType<GameBoard>();
```

**테트리스 예시**:
```csharp
gameBoard = FindObjectOfType<GameBoard>();
```

---

## 🛠️ 실습: FindObjectOfType으로 오브젝트 찾기

**목표**: 씬에 있는 특정 스크립트를 가진 오브젝트를 찾아 사용합니다.

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

**이 실습만** 할 전용 씬이 없으면 아래 순서로 **한 번만** 만듭니다. (이미 `ConceptTest_FindObjectOfType` 씬이 있으면 **File → Open Scene**으로 열고 아래 실습만 이어서 하세요.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_FindObjectOfType** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다. (다른 문서로 왔다 갔다 하지 않습니다.)

---

### 수행 과정

1. **찾을 대상 스크립트**
   - 이미 있는 **GameBoard** 스크립트 사용 또는
   - 새 스크립트 `TargetObject.cs` 생성:
```csharp
using UnityEngine;
public class TargetObject : MonoBehaviour
{
    public int value = 42;
}
```

2. **찾는 쪽 스크립트**
   - 새 스크립트 `FinderTest.cs` 생성:
```csharp
using UnityEngine;

public class FinderTest : MonoBehaviour
{
    void Start()
    {
        TargetObject target = FindObjectOfType<TargetObject>();
        if (target != null)
        {
            Debug.Log("TargetObject를 찾았습니다! value = " + target.value);
        }
        else
        {
            Debug.Log("TargetObject를 찾지 못했습니다. 씬에 TargetObject를 가진 오브젝트를 추가하세요.");
        }
    }
}
```

3. **씬 구성**
   - 빈 GameObject 생성 → 이름 "Target", **TargetObject** 스크립트 추가
   - 빈 GameObject 생성 → 이름 "Finder", **FinderTest** 스크립트 추가

4. **Play 후 Console 확인**
   - "TargetObject를 찾았습니다! value = 42" 출력
   - → FindObjectOfType으로 씬 안의 컴포넌트를 찾을 수 있음을 확인!

5. **직접 해보기**: Hierarchy에서 "Target" 오브젝트를 비활성화(체크 해제)한 뒤 Play하면 null이 나오는지 확인해 보세요.

---

[← 개념 목록으로](../개념설명.md#-unity-개념)
