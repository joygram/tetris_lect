---
layout: default
title: Transform
---

# Transform

## 📖 개념 설명

**Transform**은 GameObject의 **위치(position)**, **회전(rotation)**, **크기(scale)** 정보를 담는 Unity 컴포넌트입니다. 모든 GameObject는 Transform을 하나씩 가지며, `transform`으로 접근합니다.

```csharp
// 위치 변경
transform.position = new Vector3(5, 10, 0);

// 이동
transform.position += Vector3.right;  // 오른쪽으로 이동

// 회전
transform.rotation = Quaternion.Euler(0, 90, 0);

// 크기
transform.localScale = new Vector3(2, 2, 2);
```

**테트리스 예시** (4단계):  
- 블록 이동: `transform.position += Vector3.down;`  
- 자식 블록 위치: `child.localPosition`, `transform.GetChild(i)`  
→ 자세한 사용은 [4단계: 블록 이동 구현](../../단계별-학습/4단계-블록-이동-구현.md)을 참고하세요.

---

## 📐 Transform에서 쓰는 것들 (확장 설명)

4단계에서 **position**, **localPosition**을 쓰고, 이후 단계에서 **scale**, **rotation** 등도 자주 씁니다. 아래는 그 개념을 한눈에 정리한 것입니다.

### 1. 위치 (Position)

| 속성 | 설명 | 언제 쓰나요 |
|------|------|-------------|
| **position** | **월드(씬) 기준** 위치. 부모가 있어도 “전체 씬에서의 좌표”. | 오브젝트를 씬에서 어디에 둘지, 이동할 때. |
| **localPosition** | **부모 기준** 위치. 부모가 (5,0,0)이면 자식 localPosition (1,0,0)은 실제로 (6,0,0). | 테트리스처럼 “부모 블록 기준으로 칸 위치”를 다룰 때. |

```csharp
transform.position = new Vector3(5, 10, 0);   // 씬에서의 위치
transform.localPosition = new Vector3(1, 0, 0); // 부모 기준 위치
transform.position += Vector3.down;            // 아래로 한 칸 이동
```

- **4단계 연결**: `MoveLeft/Right/Down`은 부모의 `transform.position`을 바꾸고, 회전은 자식의 `localPosition`을 90도 돌립니다. → [4단계 Rotate 코드](../../단계별-학습/4단계-블록-이동-구현.md#4-회전-기능-구현) 참고.

### 2. 크기 (Scale)

| 속성 | 설명 | 언제 쓰나요 |
|------|------|-------------|
| **localScale** | 이 오브젝트의 **크기** (x, y, z 배율). 1이면 원래 크기. | 오브젝트를 키우거나 줄일 때. |
| **lossyScale** | 부모까지 반영된 **실제 보이는 크기** (읽기 전용). | “화면상 실제 크기”가 필요할 때. |

```csharp
transform.localScale = new Vector3(2, 2, 2);  // 2배로 키움
transform.localScale = Vector3.one;            // (1,1,1) 원래 크기
```

- **주의**: `position`처럼 `scale`만 있는 게 아니라 **localScale**을 주로 씁니다.

### 3. 회전 (Rotation)

| 속성 | 설명 | 언제 쓰나요 |
|------|------|-------------|
| **rotation** | **월드 기준** 회전. Unity는 내부적으로 **Quaternion** 사용. | 씬에서 “전체 방향”을 정할 때. |
| **localRotation** | **부모 기준** 회전. | 부모 오브젝트에 매달린 물체의 “부모 기준 방향”. |
| **eulerAngles** | 도(°) 단위 각도 (x, y, z). 읽기/쓰기 가능. | “90도 돌리기”처럼 각도로 생각할 때. |
| **localEulerAngles** | 부모 기준 도(°) 각도. | UI나 자식 오브젝트만 도 단위로 돌릴 때. |

**각도로 회전 넣기** (자주 쓰는 방법):

```csharp
// X=0, Y=90도, Z=0 으로 회전 (Y축 기준 90도)
transform.rotation = Quaternion.Euler(0, 90, 0);

// 읽을 때는 도(°) 단위로
Vector3 angles = transform.eulerAngles;
Debug.Log("각도: " + angles);
```

- **테트리스 4단계**: 2D 회전은 **자식 localPosition**을 (x,y)→(-y,x)로 바꿔서 “90도 돌린 좌표”로 표현합니다. 3D `rotation`을 쓰지 않아도 됩니다. → [회전 수학](./회전수학.md) 참고.

### 4. 부모·자식 (Hierarchy)

| 속성/메서드 | 설명 | 언제 쓰나요 |
|-------------|------|-------------|
| **parent** | 부모 Transform. 없으면 null. | “이 오브젝트의 부모가 누구인지” 알 때. |
| **childCount** | 자식 개수. | “자식이 몇 개인지”로 for문 돌릴 때. |
| **GetChild(int i)** | i번째 자식 Transform (0부터 시작). | 테트리스에서 “각 칸(자식)의 위치”를 읽거나 바꿀 때. |

```csharp
for (int i = 0; i < transform.childCount; i++)
{
    Transform child = transform.GetChild(i);
    Vector3 localPos = child.localPosition;  // 부모 기준 위치
    // 회전 시 새 위치: (x,y) → (-y,x)
}
```

- **4단계 연결**: `ValidMove`, `Rotate`에서 `transform.childCount`, `transform.GetChild(i)`, `child.localPosition`을 사용합니다.

---

## 📋 한눈에 보기

| 구분 | 월드(씬) 기준 | 부모 기준 (Local) |
|------|----------------|-------------------|
| **위치** | position | localPosition |
| **크기** | (lossyScale 읽기 전용) | localScale |
| **회전** | rotation, eulerAngles | localRotation, localEulerAngles |
| **계층** | parent | GetChild(i), childCount |

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

6. **확장 해보기**: `transform.rotation = Quaternion.Euler(0, 45, 0);` 를 Start()에 넣어 보세요. Y축 기준 45도 회전한 것을 확인할 수 있습니다.

---

## 🔗 4단계 이후로 더 실습하고 싶다면

- **변수 + Transform**으로 위치·스케일을 변수에 넣고 다루는 실습 → [4단계 확장 실습 01: 변수와 Transform](../4단계-확장-실습/01-변수와Transform.md)  
- **멤버 + Transform**으로 저장소와 이동 메소드를 짝으로 쓰는 실습 → [4단계 확장 실습 02: 멤버와 Transform](../4단계-확장-실습/02-멤버와Transform.md)  
- **배열 + Transform**으로 자식 위치를 배열에 담아 회전하는 실습 → [4단계 확장 실습 03: 배열과 Transform](../4단계-확장-실습/03-배열과Transform.md)  

위 실습은 **4단계를 다 보지 않았어도** 개별 파일만 따라 하면 진행할 수 있도록 되어 있습니다. 이전 단계 링크는 각 실습 문서에 적어 두었습니다.

---

[← 개념 목록으로](../개념설명.md#-unity-개념)
