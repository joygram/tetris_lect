---
layout: default
title: Unity 에디터 사용 가이드
---

# Unity 에디터 사용 가이드

## 📖 이 가이드를 사용하는 방법

이 가이드는 Unity 에디터를 처음 사용하는 중학생을 위해 작성되었습니다.  
각 기능을 단계별로 상세하게 설명하므로, 처음부터 차근차근 따라해보세요.

---

## 🖥️ Unity 에디터 화면 구성

### 전체 화면 레이아웃

```
┌─────────────────────────────────────────────────────────────────┐
│ File  Edit  Assets  GameObject  Component  Window  Help        │ ← 메뉴 바
├──────────┬──────────────────────────────┬───────────────────────┤
│          │                              │                       │
│ Scene    │      Scene 뷰                │   Inspector           │
│ Game     │      (게임 세계)             │   (속성 창)           │
│          │                              │                       │
│          │                              │                       │
│          │                              │                       │
├──────────┴──────────────────────────────┴───────────────────────┤
│ Hierarchy (오브젝트 목록)  │  Project (파일 목록)  │  Console    │
│                          │                    │              │
│ Main Camera              │  Assets            │  (에러 메시지)│
│ Directional Light        │    Scenes          │              │
│                          │    Scripts         │              │
└──────────────────────────┴────────────────────┴──────────────┘
```

---

## 📍 주요 창 위치 및 설명

### 1. Scene 뷰 (왼쪽 상단 큰 창)

**위치**: 화면 왼쪽 상단의 가장 큰 창

**역할**: 
- 게임 세계를 보는 창 (3D 공간)
- 오브젝트를 배치하고 이동시킬 수 있음
- 게임을 만들 때 사용하는 작업 공간

**사용법**:
- **마우스 휠**: 확대/축소
- **마우스 중간 버튼 드래그**: 화면 이동
- **마우스 오른쪽 버튼 드래그**: 카메라 회전
- **마우스 왼쪽 버튼**: 오브젝트 선택

**확인 방법**: 
- Scene 뷰 상단에 "Scene" 탭이 보임
- "Main Camera"라는 텍스트가 보이면 정상

**창이 안 보여요?**
- 메뉴: **Window > General > Scene**
- 단축키: 없음 (기본적으로 항상 표시됨)

---

### 2. Game 뷰 (Scene 뷰 옆 탭)

**위치**: Scene 뷰 옆에 있는 탭

**역할**: 
- 실제 게임이 실행될 때 보이는 화면
- Play 버튼을 누르면 이 화면으로 전환됨

**사용법**:
- Play 버튼(▶)을 누르면 자동으로 Game 뷰로 전환
- 게임이 실행되는 모습을 확인할 수 있음

**확인 방법**: 
- Scene 뷰 상단에 "Scene" 탭 옆에 "Game" 탭이 보임

**창이 안 보여요?**
- 메뉴: **Window > General > Game**
- 단축키: 없음

---

### 3. Hierarchy 창 (왼쪽 하단)

**위치**: 화면 왼쪽 하단의 작은 창

**역할**: 
- 씬에 있는 모든 오브젝트 목록
- 나무 구조로 표시됨 (부모-자식 관계)

**기본 오브젝트**:
- **Main Camera**: 게임을 찍는 카메라
- **Directional Light**: 조명

**사용법**:
- 오브젝트를 클릭하면 선택됨
- Inspector 창에 정보가 표시됨
- 오브젝트를 우클릭하면 메뉴가 나타남

**확인 방법**: 
- 왼쪽 하단에 "Hierarchy"라는 제목이 보임
- Main Camera와 Directional Light가 보임

**창이 안 보여요?**
- 메뉴: **Window > General > Hierarchy**
- 단축키: 없음 (기본적으로 항상 표시됨)

---

### 4. Inspector 창 (오른쪽)

**위치**: 화면 오른쪽의 긴 창

**역할**: 
- 선택한 오브젝트의 속성을 보는 창
- 컴포넌트를 추가/제거할 수 있음

**표시되는 정보**:
- **Transform**: 위치, 회전, 크기
- **Component**: 추가된 컴포넌트들 (Camera, Light 등)

**사용법**:
1. Hierarchy에서 오브젝트를 클릭
2. Inspector 창에 정보가 표시됨
3. 값을 변경하면 오브젝트가 변경됨

**확인 방법**: 
- Hierarchy에서 Main Camera를 클릭하면 Inspector에 정보가 나타남

**창이 안 보여요?**
- 메뉴: **Window > General > Inspector**
- 단축키: 없음 (기본적으로 항상 표시됨)

---

### 5. Project 창 (아래 중앙)

**위치**: 화면 아래 중앙의 창

**역할**: 
- 프로젝트의 모든 파일을 보는 창
- 폴더 구조로 파일 관리

**기본 폴더**:
- **Assets**: 모든 게임 파일
- **Scenes**: 씬 파일
- **Scripts**: 스크립트 파일 (우리가 만들 폴더)

**사용법**:
- 폴더를 더블클릭하면 열림
- 파일을 더블클릭하면 열림 (스크립트는 에디터에서 열림)
- 우클릭하면 메뉴가 나타남

**확인 방법**: 
- 아래 중앙에 "Project"라는 제목이 보임
- Assets 폴더가 보임

**창이 안 보여요?**
- 메뉴: **Window > General > Project**
- 단축키: **Ctrl + 5** (Windows) 또는 **Cmd + 5** (Mac)

---

### 6. Console 창 (아래, Project 창 옆)

**위치**: Project 창 옆 또는 아래

**역할**: 
- 에러 메시지 확인
- Debug.Log 출력 확인
- 경고 메시지 확인

**사용법**:
- 에러가 발생하면 빨간색으로 표시
- Debug.Log는 흰색으로 표시
- 경고는 노란색으로 표시

**확인 방법**: 
- 창이 열리면 "Console"이라는 제목이 보임

**창이 안 보여요?**
- 메뉴: **Window > General > Console**
- 단축키: **Ctrl + Shift + C** (Windows) 또는 **Cmd + Shift + C** (Mac)

---

## 🎯 자주 사용하는 메뉴

### File 메뉴

**위치**: 화면 상단 맨 왼쪽

**주요 기능**:
- **New Scene**: 새 씬 생성
- **Open Scene**: 씬 열기
- **Save**: 저장 (Ctrl + S)
- **Save As**: 다른 이름으로 저장
- **Build Settings**: 게임 빌드 설정

---

### GameObject 메뉴

**위치**: 메뉴 바에서 "GameObject"

**주요 기능**:
- **Create Empty**: 빈 오브젝트 생성
- **3D Object**: 3D 오브젝트 생성 (Cube, Sphere 등)
- **2D Object**: 2D 오브젝트 생성
- **UI**: UI 요소 생성 (Canvas, Text, Button 등)

**사용 예시**:
1. 메뉴에서 **GameObject** 클릭
2. **Create Empty** 선택
3. Hierarchy에 "GameObject" 생성됨

---

### Component 메뉴

**위치**: 메뉴 바에서 "Component"

**주요 기능**:
- 오브젝트에 컴포넌트 추가
- 스크립트 추가

**사용 예시**:
1. Hierarchy에서 오브젝트 선택
2. 메뉴에서 **Component** 클릭
3. 원하는 컴포넌트 선택

**더 쉬운 방법**:
- Inspector 창에서 **"Add Component"** 버튼 클릭
- 검색창에 컴포넌트 이름 입력
- 선택하여 추가

---

### Window 메뉴

**위치**: 메뉴 바에서 "Window"

**주요 기능**:
- **General > Hierarchy**: Hierarchy 창 열기
- **General > Scene**: Scene 뷰 열기
- **General > Game**: Game 뷰 열기
- **General > Inspector**: Inspector 창 열기
- **General > Project**: Project 창 열기
- **General > Console**: Console 창 열기
- **Layouts > Default**: 기본 레이아웃으로 복원

---

## 🛠️ 자주 하는 작업

### 1. 빈 GameObject 생성하기

**방법 1: Hierarchy에서**
1. Hierarchy 창의 빈 공간에서 **우클릭**
2. **"Create Empty"** 선택
3. "GameObject"가 생성됨
4. 이름 변경: 클릭 후 잠시 기다린 후 다시 클릭하거나 F2 키

**방법 2: 메뉴에서**
1. 메뉴에서 **GameObject > Create Empty** 클릭

---

### 2. 스크립트 추가하기

**1단계: 스크립트 파일 생성**
1. Project 창에서 **Scripts** 폴더 선택 (없으면 만들기)
2. **우클릭** > **Create > C# Script**
3. 이름 입력 (예: "GameController")
4. Enter 키로 확인

**2단계: 스크립트를 오브젝트에 추가**
1. Hierarchy에서 오브젝트 선택
2. Inspector 창에서 **"Add Component"** 버튼 클릭
3. 검색창에 스크립트 이름 입력 (예: "GameController")
4. 스크립트 클릭하여 추가

**또는**:
1. Project 창에서 스크립트 파일을 찾기
2. **드래그 앤 드롭**하여 Hierarchy의 오브젝트에 넣기

---

### 3. UI 요소 생성하기 (Canvas, Text 등)

**Canvas 생성**:
1. Hierarchy 창의 빈 공간에서 **우클릭**
2. **"UI > Canvas"** 선택
3. Canvas가 생성됨

**Text 생성**:
1. Hierarchy에서 **"Canvas"** 선택
2. Canvas를 선택한 상태에서 Hierarchy 창에서 **우클릭**
3. **"UI > Text - TextMeshPro"** 또는 **"UI > Legacy > Text"** 선택
4. Text가 Canvas 아래에 생성됨

**Button 생성**:
1. Canvas 선택 후 우클릭
2. **"UI > Button - TextMeshPro"** 또는 **"UI > Legacy > Button"** 선택

---

### 4. 오브젝트 위치 이동하기

**방법 1: Inspector에서**
1. Hierarchy에서 오브젝트 선택
2. Inspector의 **Transform** 컴포넌트에서
3. **Position**의 X, Y, Z 값을 변경

**방법 2: Scene 뷰에서**
1. Hierarchy에서 오브젝트 선택
2. Scene 뷰에서 화살표(이동 도구) 아이콘 클릭
3. Scene 뷰에서 오브젝트를 드래그하여 이동

**이동 도구 단축키**: **W** 키

---

### 5. 오브젝트 회전하기

**방법 1: Inspector에서**
1. Hierarchy에서 오브젝트 선택
2. Inspector의 **Transform** 컴포넌트에서
3. **Rotation**의 X, Y, Z 값을 변경

**방법 2: Scene 뷰에서**
1. Hierarchy에서 오브젝트 선택
2. Scene 뷰에서 회전 아이콘 클릭
3. Scene 뷰에서 오브젝트를 드래그하여 회전

**회전 도구 단축키**: **E** 키

---

### 6. 오브젝트 크기 조정하기

**방법 1: Inspector에서**
1. Hierarchy에서 오브젝트 선택
2. Inspector의 **Transform** 컴포넌트에서
3. **Scale**의 X, Y, Z 값을 변경

**방법 2: Scene 뷰에서**
1. Hierarchy에서 오브젝트 선택
2. Scene 뷰에서 크기 조정 아이콘 클릭
3. Scene 뷰에서 오브젝트를 드래그하여 크기 조정

**크기 조정 도구 단축키**: **R** 키

---

### 7. 컴포넌트 연결하기 (드래그 앤 드롭)

**예시: GameController에 Text 연결**

1. **GameController 선택**
   - Hierarchy에서 "GameController" 클릭
   - Inspector에 GameController 컴포넌트가 보임

2. **Text 찾기**
   - Hierarchy에서 "ScoreText" 찾기

3. **드래그 앤 드롭**
   - Hierarchy에서 "ScoreText"를 **클릭하고 잡은 상태**로
   - Inspector의 "Score Text" 필드까지 **드래그**
   - 필드에 "ScoreText"가 표시되면 성공

**또는**:
1. Inspector의 "Score Text" 필드 옆에 있는 **원형 버튼** 클릭
2. 나타난 창에서 "ScoreText" 선택

---

## ⌨️ 유용한 단축키

| 단축키 | 기능 |
|--------|------|
| **Ctrl + S** (Cmd + S) | 저장 |
| **Ctrl + P** (Cmd + P) | 게임 실행/정지 |
| **Ctrl + Shift + C** (Cmd + Shift + C) | Console 창 열기 |
| **W** | 이동 도구 |
| **E** | 회전 도구 |
| **R** | 크기 조정 도구 |
| **F** | 선택한 오브젝트에 카메라 맞추기 |
| **Ctrl + Z** (Cmd + Z) | 실행 취소 |
| **Ctrl + Y** (Cmd + Shift + Z) | 다시 실행 |
| **Delete** | 선택한 오브젝트 삭제 |

---

## 🔧 문제 해결

### 창이 안 보여요

**해결 방법**:
1. 메뉴에서 **Window** 클릭
2. **General** 메뉴에서 원하는 창 이름 클릭
3. 또는 **Window > Layouts > Default**로 기본 레이아웃 복원

---

### 창 위치가 이상해요

**해결 방법**:
1. 창 제목을 **드래그**하여 원하는 위치로 이동
2. 창을 다른 창 옆에 가져가면 자동으로 붙음
3. **Window > Layouts > Default**로 기본 레이아웃 복원

---

### 메뉴를 찾을 수 없어요

**해결 방법**:
1. 메뉴 바를 왼쪽에서 오른쪽으로 천천히 확인
2. 메뉴가 화면 밖에 있을 수 있으므로 스크롤
3. 메뉴 이름을 정확히 확인 (대소문자 구분)

---

### 우클릭 메뉴가 안 나타나요

**해결 방법**:
1. 올바른 위치에서 우클릭했는지 확인
   - Hierarchy: 빈 공간에서 우클릭
   - Project: 폴더나 파일에서 우클릭
2. 오브젝트를 선택한 상태에서 우클릭
3. 마우스 오른쪽 버튼이 제대로 작동하는지 확인

---

### 드래그 앤 드롭이 안 돼요

**해결 방법**:
1. 마우스 왼쪽 버튼을 **누른 상태**로 드래그
2. 목적지까지 **끌어간 후** 버튼 놓기
3. 목적지가 드래그를 받을 수 있는지 확인 (필드가 활성화되어 있어야 함)

---

### 오브젝트가 Scene 뷰에서 안 보여요

**해결 방법**:
1. Scene 뷰에서 **F** 키를 눌러 오브젝트에 카메라 맞추기
2. Scene 뷰의 확대/축소 조정 (마우스 휠)
3. 오브젝트의 위치 확인 (Inspector의 Transform)
4. 오브젝트가 너무 작거나 큰지 확인 (Scale 확인)

---

## 💡 유용한 팁

1. **창 레이아웃 저장**: 
   - 원하는 레이아웃으로 조정한 후
   - **Window > Layouts > Save Layout**으로 저장

2. **빠른 검색**:
   - Hierarchy나 Project 창에서 이름을 입력하면 자동으로 검색

3. **오브젝트 복사**:
   - Hierarchy에서 오브젝트 선택 후 **Ctrl + D** (Cmd + D)

4. **오브젝트 이름 변경**:
   - 오브젝트 클릭 후 잠시 기다린 후 다시 클릭
   - 또는 **F2** 키

5. **모든 창 닫기/열기**:
   - **Window > Layouts > Default**로 기본 레이아웃 복원

---

## 📚 추가 학습 자료

- Unity 공식 문서: https://docs.unity3d.com/
- Unity Learn: https://learn.unity.com/
- 개념설명.md 파일 참고

---

**이 가이드를 자주 참고하세요!**  
**모르는 것이 있으면 언제든 질문하세요!** 🎓
