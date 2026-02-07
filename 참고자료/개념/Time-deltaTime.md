---
layout: default
title: Time.deltaTime
---

# Time.deltaTime

## 📖 개념 설명

**Time.deltaTime**은 이전 프레임과 현재 프레임 사이의 시간(초)입니다.

```csharp
timer += Time.deltaTime;

if (timer >= 1.0f)
{
    DoSomething();
    timer = 0f;
}
```

**테트리스 예시**:
```csharp
fallTimer += Time.deltaTime;
if (fallTimer >= fallTime)
{
    MoveDown();
    fallTimer = 0f;
}
```

---

## 🛠️ 실습: deltaTime으로 1초마다 실행하기

**목표**: Time.deltaTime을 누적해 1초마다 로그를 출력합니다.

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

**이 실습만** 할 전용 씬이 없으면 아래 순서로 **한 번만** 만듭니다. (이미 `ConceptTest_deltaTime` 씬이 있으면 **File → Open Scene**으로 열고 아래 실습만 이어서 하세요.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_deltaTime** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다. (다른 문서로 왔다 갔다 하지 않습니다.)

---

### 수행 과정

1. **Unity에서 새 C# 스크립트 생성**
   - 이름: `DeltaTimeTest`

2. **다음 코드 작성**
```csharp
using UnityEngine;

public class DeltaTimeTest : MonoBehaviour
{
    private float timer = 0f;
    
    void Update()
    {
        timer += Time.deltaTime;
        
        if (timer >= 1f)
        {
            Debug.Log("1초가 지났습니다! (deltaTime 누적)");
            timer = 0f;
        }
    }
}
```

3. **빈 GameObject에 스크립트 추가 후 Play**
   - Console에서 약 1초마다 "1초가 지났습니다!" 출력 확인
   - → deltaTime을 누적해 시간을 재는 방식 확인!

4. **직접 해보기**: `if (timer >= 2f)` 로 바꿔서 2초마다 출력되게 해 보세요.

---

[← 개념 목록으로](../개념설명.md#-unity-개념)
