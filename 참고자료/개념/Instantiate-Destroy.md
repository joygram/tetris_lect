---
layout: default
title: Instantiate와 Destroy
---

# Instantiate와 Destroy

## 📖 개념 설명

**Instantiate**: 게임 오브젝트를 복제(생성)합니다.
```csharp
GameObject newBlock = Instantiate(blockPrefab);
```

**Destroy**: 게임 오브젝트를 삭제합니다.
```csharp
Destroy(gameObject);  // 자기 자신 삭제
Destroy(otherObject); // 다른 오브젝트 삭제
```

**테트리스 예시**:
```csharp
GameObject newPiece = Instantiate(tetrisBlockPrefab);
Destroy(block);
```

---

## 🛠️ 실습: Instantiate로 오브젝트 복제하기

**목표**: Play 시 Cube를 Instantiate로 생성하고, 3초 후 Destroy로 삭제합니다.

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

**이 실습만** 할 전용 씬이 없으면 아래 순서로 **한 번만** 만듭니다. (이미 `ConceptTest_Instantiate` 씬이 있으면 **File → Open Scene**으로 열고 아래 실습만 이어서 하세요.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Instantiate** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다. (다른 문서로 왔다 갔다 하지 않습니다.)

---

### 수행 과정

1. **Cube 프리팹 준비**
   - Hierarchy에서 우클릭 → 3D Object → Cube
   - 이름: "SampleCube"
   - Project 창의 Assets 폴더에 **SampleCube**를 드래그하여 프리팹 생성
   - Hierarchy의 SampleCube는 삭제해도 됨 (프리팹은 Project에 있음)

2. **스크립트 생성**
   - 이름: `InstantiateTest`

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class InstantiateTest : MonoBehaviour
{
    public GameObject cubePrefab;  // Inspector에서 프리팹 연결
    private GameObject spawnedCube;
    
    void Start()
    {
        if (cubePrefab != null)
        {
            spawnedCube = Instantiate(cubePrefab);
            spawnedCube.transform.position = new Vector3(2, 0, 0);
            Debug.Log("Cube 생성됨 (Instantiate)");
        }
    }
    
    void Update()
    {
        if (spawnedCube != null && Time.time > 3f)
        {
            Destroy(spawnedCube);
            Debug.Log("Cube 삭제됨 (Destroy)");
            spawnedCube = null;
        }
    }
}
```

4. **빈 GameObject에 스크립트 추가**
   - Hierarchy에서 Create Empty → 이름: "Spawner"
   - InstantiateTest 스크립트 추가
   - Inspector에서 **Cube Prefab** 필드에 Project의 SampleCube 프리팹을 드래그

5. **Play**
   - 시작 시 (2, 0, 0) 위치에 Cube가 생성됨
   - 3초 후 Cube가 사라지고 Console에 "Cube 삭제됨" 출력

---

[← 개념 목록으로](../개념설명.md#-unity-개념)
