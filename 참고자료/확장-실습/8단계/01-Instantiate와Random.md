---
layout: default
title: 8단계 확장 실습 01 - Instantiate와 Random
---

# 8단계 확장 실습 01: Instantiate와 Random

## 📌 이 실습은?

**Random.Range** 로 인덱스를 고르고, **Instantiate** 로 프리팹(또는 씬에 있는 오브젝트)을 복제해 생성하는 실습입니다.  
**이전 단계를 다 보지 않았어도** 이 파일만 따라 하면 진행할 수 있습니다.

**이전 단계 링크** (필요할 때만 참고):
- [8단계: 게임 완성](../../../단계별-학습/8단계-게임-완성.md) — Spawner, SpawnNext(), Instantiate, Random.Range
- [Instantiate / Destroy (개념)](../개념/Instantiate-Destroy.md) — 오브젝트 생성·삭제
- [배열 (개념)](../개념/배열.md) — GameObject[] 프리팹 배열
- [7단계 확장 실습 01](../7단계/01-점수변수와UI텍스트.md) — 점수와 UI (선택)

---

## 🎯 목표

- **GameObject[]** 배열에 Cube 프리팹(또는 씬의 Cube)을 넣고, **Random.Range(0, 배열.Length)** 로 인덱스를 고른다.
- **Instantiate(프리팹, 위치, 회전)** 로 그 위치에 오브젝트를 생성한다.

---

## 🛠️ 실습

### 이 실습 전용 씬 만들기 (환경 설정)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Stage8_InstantiateRandom** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다.

---

### 프리팹 준비 (간단한 방법)

1. **Hierarchy** 우클릭 → 3D Object → **Cube** → 이름: **"TemplateCube"**
2. **Project** 창에서 **Assets** 안에 **Prefabs** 폴더가 없으면 만들기
3. **TemplateCube** 를 Project의 **Prefabs** 폴더로 **끌어다 놓기** → 프리팹 생성됨
4. Hierarchy의 **TemplateCube** 는 삭제해도 됨 (프리팹만 있으면 됨)

---

### 수행 과정

1. **빈 GameObject 생성**  
   - Hierarchy 우클릭 → Create Empty → 이름: **"Stage8ExpandTest"**

2. **C# 스크립트 생성**  
   - 이름: `Stage8ExpandTest`

3. **다음 코드 작성**
```csharp
using UnityEngine;

public class Stage8ExpandTest : MonoBehaviour
{
    public GameObject[] prefabs;  // Inspector에서 프리팹 1개 이상 할당 (같은 Cube 여러 개여도 됨)
    public Transform spawnPoint;  // Inspector에서 빈 오브젝트 할당 (위치용)

    void Start()
    {
        if (prefabs == null || prefabs.Length == 0) return;
        if (spawnPoint == null) spawnPoint = transform;

        int index = Random.Range(0, prefabs.Length);
        Vector3 pos = spawnPoint.position + new Vector3(Random.Range(-2f, 2f), 0, 0);
        Instantiate(prefabs[index], pos, Quaternion.identity);
        Debug.Log("생성 인덱스: " + index + ", 위치: " + pos);
    }
}
```

4. **스크립트를 Stage8ExpandTest에 추가**  
   - **Spawn Point**: Hierarchy에서 빈 오브젝트 생성 (이름: SpawnPoint) 후 Inspector에서 할당  
   - **Prefabs**: 배열 크기 1, Element 0에 **TemplateCube** 프리팹 할당

5. **Play**  
   - 씬에 Cube가 하나 생성되고, Console에 생성 인덱스와 위치가 출력되는지 확인. 여러 번 Play 해 보면 위치가 랜덤으로 바뀜

6. **직접 해보기**: Prefabs 배열에 Cube 프리팹을 2번 넣고, Random.Range(0, prefabs.Length)로 0 또는 1이 나와 서로 다른 위치에 두 개가 생성되도록 해 보세요.

7. **정리**: 8단계 Spawner는 **tetrisBlockPrefabs** 배열에서 **Random.Range(0, tetrisBlockPrefabs.Length)** 로 블록을 고른 뒤 **Instantiate** 로 생성합니다.

---

[← 7단계 확장 실습](../7단계/01-점수변수와UI텍스트.md) | [단계별 확장 실습 목차](../README.md) | [8단계로](../../../단계별-학습/8단계-게임-완성.md)
