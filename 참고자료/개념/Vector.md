---
layout: default
title: Vector
---

# Vector2, Vector3, Vector2Int

## 📖 개념 설명

**Vector**는 위치나 방향을 나타내는 수학적 개념입니다.

```csharp
Vector2 position2D = new Vector2(5, 10);      // 2D (x, y)
Vector3 position3D = new Vector3(5, 10, 0);  // 3D (x, y, z)
Vector2Int gridPos = new Vector2Int(5, 10);  // 정수만 (게임 보드에 적합)

// 자주 쓰는 방향
Vector3.right  // (1, 0, 0)
Vector3.left   // (-1, 0, 0)
Vector3.up     // (0, 1, 0)
Vector3.down   // (0, -1, 0)
```

**테트리스 예시**:
```csharp
position = new Vector2Int(5, 10);
transform.position += Vector3.down;  // 아래로 이동
```

---

## 🛠️ 실습: Vector로 위치·방향 사용하기

**목표**: Vector2Int와 Vector3를 사용해 위치를 설정하고 이동합니다.

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

**이 실습만** 할 전용 씬이 없으면 아래 순서로 **한 번만** 만듭니다. (이미 `ConceptTest_Vector` 씬이 있으면 **File → Open Scene**으로 열고 아래 실습만 이어서 하세요.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Vector** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다. (다른 문서로 왔다 갔다 하지 않습니다.)

---

### 수행 과정

1. **Unity에서 새 C# 스크립트 생성**
   - 이름: `VectorTest`

2. **다음 코드 작성**
```csharp
using UnityEngine;

public class VectorTest : MonoBehaviour
{
    void Start()
    {
        // Vector2Int (정수 좌표)
        Vector2Int gridPos = new Vector2Int(5, 10);
        Debug.Log("그리드 위치: " + gridPos);
        
        // Vector3 (Unity 위치)
        transform.position = new Vector3(gridPos.x, gridPos.y, 0);
        
        // 방향 벡터
        Debug.Log("오른쪽: " + Vector3.right);
        Debug.Log("아래: " + Vector3.down);
        
        // 한 칸 이동
        transform.position += Vector3.right;
        Debug.Log("이동 후 위치: " + transform.position);
    }
}
```

3. **빈 GameObject에 스크립트 추가 후 Play**
   - Console에서 그리드 위치, 방향, 이동 후 위치 확인
   - Scene 뷰에서 오브젝트가 (5, 10)에서 (6, 10)으로 이동한 것 확인

4. **직접 해보기**: `transform.position += Vector3.down;` 을 추가해 아래로 한 칸 이동시켜 보세요.

---

[← 개념 목록으로](../개념설명.md#-unity-개념)
