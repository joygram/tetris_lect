---
layout: default
title: MonoBehaviour
---

# MonoBehaviour

## 💡 Awake / Start / Update 용도 (한 줄씩)

| 함수 | 용도 (쉽게 말하면) |
|------|---------------------|
| **Awake()** | **가장 먼저 한 번** – 다른 스크립트보다 먼저 "준비할 일" (예: 빈 배열 만들기) |
| **Start()** | **한 번만** – 준비 끝난 뒤 "시작할 일" (예: 다른 오브젝트 찾기, 처음 위치 정하기) |
| **Update()** | **매 프레임 반복** – "계속 할 일" (예: 키 입력 확인, 타이머, 이동) |

**비유**: Awake = 책상 정리(한 번), Start = 업무 시작(한 번), Update = 업무하는 동안 계속 반복.

---

## 📖 개념 설명

**MonoBehaviour**는 Unity에서 사용하는 특별한 클래스입니다. 스크립트가 GameObject에 붙어 동작하려면 이 클래스를 상속해야 합니다.

```csharp
public class TetrisBlock : MonoBehaviour
{
    void Awake() { ... }   // 가장 먼저 한 번 (준비)
    void Start() { ... }   // 그 다음 한 번 (시작)
    void Update() { ... } // 매 프레임 반복 (계속 할 일)
}
```

---

## 🛠️ 실습: Start와 Update 구분하기

**목표**: Start는 한 번, Update는 매 프레임 실행되는 것을 확인합니다.

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

**이 실습만** 할 전용 씬이 없으면 아래 순서로 **한 번만** 만듭니다. (이미 `ConceptTest_MonoBehaviour` 씬이 있으면 **File → Open Scene**으로 열고 아래 실습만 이어서 하세요.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_MonoBehaviour** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다. (다른 문서로 왔다 갔다 하지 않습니다.)

---

### 수행 과정

1. **Unity에서 새 C# 스크립트 생성**
   - 이름: `MonoBehaviourTest`

2. **다음 코드 작성**
```csharp
using UnityEngine;

public class MonoBehaviourTest : MonoBehaviour
{
    void Awake()
    {
        Debug.Log("1. Awake (가장 먼저, 한 번)");
    }
    
    void Start()
    {
        Debug.Log("2. Start (한 번)");
    }
    
    void Update()
    {
        // 매 프레임 실행되므로 로그가 너무 많음 - 60프레임마다 한 번만
        if (Time.frameCount % 60 == 0)
        {
            Debug.Log("3. Update (매 프레임, 여기서는 60프레임마다 출력)");
        }
    }
}
```

3. **빈 GameObject에 스크립트 추가 후 Play**
   - Console: "1. Awake" → "2. Start" → "3. Update"가 반복
   - Awake, Start는 한 번씩, Update는 매 프레임 호출됨을 확인!

4. **더 자세한 설명**: [MonoBehaviour이해하기](../MonoBehaviour이해하기.md) 문서를 참고하세요.

---

[← 개념 목록으로](../개념설명.md#-unity-개념)
