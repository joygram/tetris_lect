---
layout: default
title: MonoBehaviour 이해하기
---

# MonoBehaviour 이해하기 - 중학생을 위한 쉬운 가이드

## 📖 이 문서는?

MonoBehaviour는 Unity에서 가장 중요한 개념 중 하나입니다.  
처음에는 어려워 보일 수 있지만, 비유와 예시를 통해 쉽게 이해할 수 있습니다!

---

## 🎯 MonoBehaviour란 무엇인가?

### 간단한 비유

**MonoBehaviour = 게임 오브젝트에 붙일 수 있는 "스마트 부품"**

```
게임 오브젝트 (GameObject)
  = 자동차의 차체

MonoBehaviour 스크립트
  = 자동차의 엔진, 브레이크, 핸들 등
  = 차체에 붙여서 기능을 추가하는 부품
```

**예시**:
- 자동차 차체만으로는 움직일 수 없음
- 엔진을 붙이면 움직일 수 있음
- 브레이크를 붙이면 멈출 수 있음

**Unity에서**:
- GameObject만으로는 아무것도 못함
- MonoBehaviour 스크립트를 붙이면 기능이 생김
- TetrisBlock 스크립트를 붙이면 블록이 움직임

---

## 🔍 MonoBehaviour의 특징

### 1. MonoBehaviour는 "부모 클래스"입니다

**일반 클래스**:
```csharp
public class Calculator
{
    // 그냥 클래스 - Unity와 연결 안 됨
}
```

**MonoBehaviour 클래스**:
```csharp
public class TetrisBlock : MonoBehaviour
{
    // MonoBehaviour를 상속받음
    // Unity가 자동으로 관리해줌
}
```

**차이점**:
- 일반 클래스: Unity가 모름 (사용 불가)
- MonoBehaviour: Unity가 알아서 관리 (사용 가능)

---

### 2. MonoBehaviour는 GameObject에 붙여야 합니다

**단계별 설명**:

```
1단계: 스크립트 작성
  └─ public class TetrisBlock : MonoBehaviour { ... }
  ↓
2단계: GameObject 생성
  └─ Hierarchy에서 Create Empty
  ↓
3단계: 스크립트를 GameObject에 붙이기
  └─ Inspector에서 Add Component > TetrisBlock
  ↓
4단계: Unity가 자동으로 관리
  └─ Start(), Update() 자동 호출
```

**중요**: MonoBehaviour 스크립트는 반드시 GameObject에 붙여야 작동합니다!

---

## 🎮 MonoBehaviour의 주요 함수들

### 💡 Awake / Start / Update 용도 한눈에

| 함수 | 언제? | 용도 (쉽게 말하면) |
|------|--------|---------------------|
| **Awake()** | 게임이 켜질 때 **가장 먼저**, 딱 한 번 | "다른 것보다 먼저 준비할 일" (예: 빈 배열 만들기, 값 세팅) |
| **Start()** | Awake 다음에, **한 번만** | "준비가 끝난 뒤 할 일" (예: 다른 오브젝트 찾기, 처음 위치 정하기) |
| **Update()** | 게임이 도는 동안 **매 프레임** 반복 | "계속 확인하거나 바꿔 줄 일" (예: 키 입력, 타이머, 이동) |

**비유**:
- **Awake** = 출근해서 책상 정리 (한 번만, 맨 먼저)
- **Start** = 업무 시작 버튼 누르기 (한 번만)
- **Update** = 업무하는 동안 계속 반복하는 일 (입력 확인, 화면 갱신)

---

### 1. Start() - 게임 시작 시 한 번만 실행

**비유**: 자동차 시동을 거는 것

```csharp
public class TetrisBlock : MonoBehaviour
{
    void Start()
    {
        Debug.Log("게임이 시작되었습니다!");
        // 여기서 초기화 작업을 합니다
    }
}
```

**언제 실행되나요?**
- 게임이 시작될 때 (Play 버튼을 눌렀을 때)
- GameObject가 활성화되었을 때
- **한 번만** 실행됩니다

**실행 순서**:
```
게임 시작
  ↓
GameObject 생성
  ↓
Start() 실행 ← 여기서 한 번만!
  ↓
Update() 반복 실행...
```

**테트리스 예시**:
```csharp
void Start()
{
    // 블록의 초기 위치 설정
    position = new Vector2Int(5, 19);
    
    // 랜덤 모양 선택
    shapeIndex = Random.Range(0, 7);
    
    // 블록 생성
    CreateVisualBlocks();
}
```

---

### 2. Update() - 매 프레임마다 실행

**비유**: 자동차의 엔진이 계속 돌아가는 것

```csharp
public class TetrisBlock : MonoBehaviour
{
    void Update()
    {
        Debug.Log("매 프레임마다 실행됩니다!");
        // 여기서 계속 확인하고 업데이트합니다
    }
}
```

**언제 실행되나요?**
- 게임이 실행 중일 때
- **매 프레임마다** 실행 (초당 약 60회)
- 게임이 끝날 때까지 계속 반복

**실행 순서**:
```
게임 시작
  ↓
Start() 실행 (한 번만)
  ↓
Update() 실행 (프레임 1)
  ↓
Update() 실행 (프레임 2)
  ↓
Update() 실행 (프레임 3)
  ↓
... 계속 반복 ...
```

**테트리스 예시**:
```csharp
void Update()
{
    // 시간 누적
    fallTimer += Time.deltaTime;
    
    // 1초가 지났으면
    if (fallTimer >= fallTime)
    {
        MoveDown();  // 블록을 아래로 이동
        fallTimer = 0f;  // 타이머 초기화
    }
}
```

**중요**: Update()는 매우 자주 실행되므로, 무거운 작업은 피해야 합니다!

---

### 3. Awake() - Start()보다 먼저 실행

**비유**: 자동차를 만들 때 가장 먼저 부품을 준비하는 것

```csharp
public class GameBoard : MonoBehaviour
{
    void Awake()
    {
        Debug.Log("Awake가 먼저 실행됩니다!");
        // 여기서 초기화 작업을 합니다
    }
    
    void Start()
    {
        Debug.Log("Start가 나중에 실행됩니다!");
    }
}
```

**실행 순서**:
```
게임 시작
  ↓
Awake() 실행 ← 가장 먼저!
  ↓
Start() 실행 ← 그 다음!
  ↓
Update() 반복 실행...
```

**언제 사용하나요?**
- **다른 스크립트보다 먼저** 초기화해야 할 때 (예: GameBoard의 grid 배열은 다른 스크립트가 Start에서 찾기 전에 있어야 함)
- "한 번만 준비해 두면 되는 값"을 세팅할 때

**테트리스 예시**:
```csharp
void Awake()
{
    // 게임 보드 배열 초기화
    grid = new Transform[width, height];
    // Start()보다 먼저 실행되어야 함!
}
```

---

## 🔗 MonoBehaviour와 GameObject의 관계

### 관계도

```
GameObject (게임 오브젝트)
  ├─ Transform (위치, 회전, 크기)
  ├─ TetrisBlock (MonoBehaviour 스크립트)
  │   ├─ Start() 함수
  │   ├─ Update() 함수
  │   └─ MoveLeft() 함수 등
  └─ Renderer (화면에 그리기)
```

**설명**:
- GameObject는 "컨테이너" (상자)
- MonoBehaviour는 "기능" (상자 안의 물건)
- 여러 MonoBehaviour를 하나의 GameObject에 붙일 수 있음

---

### 실제 예시

**테트리스 블록 (TetrisBlock)**:

```
GameObject: "TetrisBlock"
  ├─ Transform: 위치는 (5, 19, 0)
  ├─ TetrisBlock (MonoBehaviour)
  │   ├─ position = (5, 19)
  │   ├─ cells = [블록들의 위치]
  │   ├─ Start(): 블록 초기화
  │   └─ Update(): 자동 낙하
  └─ 여러 개의 Block (자식 GameObject)
```

---

## 💡 MonoBehaviour를 사용하는 이유

### 1. Unity가 자동으로 관리해줍니다

**일반 클래스**:
```csharp
public class Calculator
{
    void Calculate()
    {
        // 이 함수를 언제 호출해야 할지 모름
        // 직접 호출해야 함
    }
}
```

**MonoBehaviour**:
```csharp
public class TetrisBlock : MonoBehaviour
{
    void Update()
    {
        // Unity가 자동으로 매 프레임마다 호출해줌!
        // 신경 쓸 필요 없음
    }
}
```

---

### 2. GameObject와 쉽게 연결됩니다

**일반 클래스**:
```csharp
public class Calculator
{
    // GameObject의 위치를 어떻게 알지?
    // 직접 찾아야 함
}
```

**MonoBehaviour**:
```csharp
public class TetrisBlock : MonoBehaviour
{
    void Start()
    {
        // transform은 자동으로 연결됨!
        transform.position = new Vector3(5, 10, 0);
        
        // gameObject도 자동으로 연결됨!
        Debug.Log(gameObject.name);  // "TetrisBlock"
    }
}
```

---

### 3. Inspector에서 쉽게 설정할 수 있습니다

**public 변수**:
```csharp
public class GameBoard : MonoBehaviour
{
    public int width = 10;   // Inspector에서 변경 가능!
    public int height = 20;  // Inspector에서 변경 가능!
}
```

**Inspector 창**:
```
GameBoard (Script)
  ├─ Width: 10  ← 여기서 변경 가능!
  └─ Height: 20 ← 여기서 변경 가능!
```

---

## 🎓 단계별 이해하기

### 1단계: 기본 이해

**MonoBehaviour = Unity가 알아서 관리해주는 스크립트**

```csharp
public class HelloWorld : MonoBehaviour
{
    void Start()
    {
        Debug.Log("안녕하세요!");
    }
}
```

**이해 체크**:
- ✅ MonoBehaviour를 상속받으면 Unity가 알아서 관리한다
- ✅ GameObject에 붙여야 작동한다
- ✅ Start()는 게임 시작 시 한 번만 실행된다

---

### 2단계: Update() 이해

**Update() = 매 프레임마다 실행되는 함수**

```csharp
public class Counter : MonoBehaviour
{
    private int count = 0;
    
    void Update()
    {
        count++;
        Debug.Log("카운트: " + count);
    }
}
```

**이해 체크**:
- ✅ Update()는 매 프레임마다 실행된다
- ✅ 게임이 끝날 때까지 계속 반복된다
- ✅ 무거운 작업은 피해야 한다

---

### 3단계: 실제 사용

**테트리스 블록 예시**:

```csharp
public class TetrisBlock : MonoBehaviour
{
    private Vector2Int position;
    private float fallTimer = 0f;
    private float fallTime = 1f;
    
    void Start()
    {
        // 게임 시작 시: 초기 위치 설정
        position = new Vector2Int(5, 19);
        Debug.Log("블록이 생성되었습니다!");
    }
    
    void Update()
    {
        // 매 프레임마다: 시간 누적
        fallTimer += Time.deltaTime;
        
        // 1초가 지났으면: 블록을 아래로 이동
        if (fallTimer >= fallTime)
        {
            MoveDown();
            fallTimer = 0f;
        }
    }
    
    void MoveDown()
    {
        position.y--;
        Debug.Log("블록이 아래로 이동했습니다!");
    }
}
```

**이해 체크**:
- ✅ Start()에서 초기화를 한다
- ✅ Update()에서 계속 확인하고 업데이트한다
- ✅ 다른 함수도 자유롭게 만들 수 있다

---

## ❓ 자주 묻는 질문

### Q1: MonoBehaviour 없이도 스크립트를 만들 수 있나요?

**A**: 네, 만들 수 있습니다. 하지만 Unity가 자동으로 관리해주지 않습니다.

```csharp
// 일반 클래스 - Unity가 모름
public class Calculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }
}

// MonoBehaviour - Unity가 알아서 관리
public class GameManager : MonoBehaviour
{
    void Start()
    {
        Calculator calc = new Calculator();
        int result = calc.Add(5, 3);
        Debug.Log(result);  // 8
    }
}
```

**결론**: Unity 기능을 사용하려면 MonoBehaviour가 필요합니다!

---

### Q2: Start()와 Awake()의 차이가 뭔가요?

**A**: 실행 순서가 다릅니다.

```
Awake() → Start() → Update()
  (먼저)    (나중)     (반복)
```

**Awake()**: 
- 다른 스크립트보다 먼저 실행
- 변수 초기화에 사용

**Start()**: 
- Awake() 다음에 실행
- 다른 스크립트가 준비된 후 작업에 사용

**대부분의 경우 Start()만 사용해도 됩니다!**

---

### Q3: Update()가 너무 자주 실행되는데 괜찮나요?

**A**: 네, 괜찮습니다! 하지만 주의해야 합니다.

**좋은 예**:
```csharp
void Update()
{
    // 간단한 작업만
    if (Input.GetKeyDown(KeyCode.Space))
    {
        Jump();
    }
}
```

**나쁜 예**:
```csharp
void Update()
{
    // 무거운 작업 (매 프레임마다 실행되면 느려짐)
    for (int i = 0; i < 1000000; i++)
    {
        // 복잡한 계산...
    }
}
```

**결론**: Update()는 가볍게 유지하세요!

---

### Q4: MonoBehaviour 스크립트를 여러 개 붙일 수 있나요?

**A**: 네, 가능합니다!

```
GameObject: "Player"
  ├─ Transform
  ├─ PlayerController (MonoBehaviour)
  ├─ Health (MonoBehaviour)
  └─ Score (MonoBehaviour)
```

**각 스크립트가 독립적으로 작동합니다!**

---

### Q5: MonoBehaviour 없이 Start()나 Update()를 사용할 수 있나요?

**A**: 아니요, 불가능합니다!

```csharp
// ❌ 작동 안 함
public class Test
{
    void Start()  // Unity가 호출 안 해줌
    {
        Debug.Log("실행 안 됨!");
    }
}

// ✅ 작동함
public class Test : MonoBehaviour
{
    void Start()  // Unity가 자동으로 호출해줌
    {
        Debug.Log("실행됨!");
    }
}
```

**결론**: Start(), Update() 등을 사용하려면 반드시 MonoBehaviour를 상속받아야 합니다!

---

## 🎯 핵심 정리

### MonoBehaviour는...

1. **Unity가 알아서 관리해주는 스크립트**
   - Start(), Update() 등을 자동으로 호출
   - GameObject와 쉽게 연결

2. **GameObject에 붙여야 작동**
   - Inspector에서 Add Component로 붙임
   - 여러 개를 붙일 수 있음

3. **주요 함수들**
   - `Awake()`: 가장 먼저 실행 (초기화)
   - `Start()`: 게임 시작 시 한 번만 실행
   - `Update()`: 매 프레임마다 실행 (반복)

4. **편리한 기능들**
   - `transform`: 위치, 회전, 크기
   - `gameObject`: 자신이 붙은 GameObject
   - `public 변수`: Inspector에서 설정 가능

---

## 📚 다음 단계

MonoBehaviour를 이해했다면:

1. **실제로 사용해보기**
   - 1주차 강의안의 HelloWorld 스크립트 만들기
   - Start()와 Update()의 차이 확인하기

2. **더 배우기**
   - 개념설명.md의 MonoBehaviour 섹션 읽기
   - 단계별학습가이드.md의 실습 따라하기

3. **질문하기**
   - 이해가 안 되는 부분은 질문하기
   - 실제 코드를 보면서 이해하기

---

## 💪 연습 문제

### 문제 1: 기본 이해

다음 코드를 보고 질문에 답하세요.

```csharp
public class Test : MonoBehaviour
{
    void Start()
    {
        Debug.Log("시작!");
    }
    
    void Update()
    {
        Debug.Log("업데이트!");
    }
}
```

**질문**:
1. "시작!"은 몇 번 출력되나요?
2. "업데이트!"는 몇 번 출력되나요?
3. 이 스크립트를 사용하려면 어떻게 해야 하나요?

**답**:
1. 한 번만 (게임 시작 시)
2. 매 프레임마다 (초당 약 60회)
3. GameObject에 Add Component로 붙이기

---

### 문제 2: 실제 사용

다음 코드를 완성하세요.

```csharp
public class Counter : MonoBehaviour
{
    private int count = 0;
    
    void Start()
    {
        // 여기에 초기화 코드 작성
        Debug.Log("카운터 시작!");
    }
    
    void Update()
    {
        // 여기에 매 프레임마다 실행될 코드 작성
        count++;
        if (count % 60 == 0)  // 60프레임마다
        {
            Debug.Log("1초 경과!");
        }
    }
}
```

**과제**: 위 코드를 작성하고 실행해보세요!

---

**축하합니다! MonoBehaviour를 이해했습니다!** 🎉

이제 Unity 게임 개발의 기초를 다졌습니다.  
다음 단계로 나아가서 멋진 게임을 만들어보세요!
