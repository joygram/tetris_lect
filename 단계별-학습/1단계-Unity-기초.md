---
layout: default
title: 1단계 - Unity와 C# 기초
---

# 1단계: Unity와 C# 기초

## 🎯 이 단계에서 배울 것

- Unity 프로젝트 생성
- Unity 에디터 기본 사용법
- C# 스크립트 작성 및 실행
- 변수, 함수, 조건문 기초

## 📝 실습 내용

### 1. Unity 프로젝트 생성

#### 1-1. Unity Hub 실행

1. **Unity Hub 프로그램 실행**
   - 바탕화면의 Unity Hub 아이콘 더블클릭
   - 또는 시작 메뉴에서 "Unity Hub" 검색 후 실행

2. **Unity Hub 화면 확인**
   - 왼쪽에 "Projects", "Installs", "Learn" 메뉴가 보임
   - 중앙에 프로젝트 목록이 보임 (처음이면 비어있음)

#### 1-2. 새 프로젝트 생성

1. **"New Project" 버튼 클릭**
   - Unity Hub 화면 오른쪽 상단의 **"New Project"** 버튼 클릭
   - 또는 왼쪽 상단의 **"New"** 버튼 클릭

2. **템플릿 선택**
   - 나타난 화면에서 **"2D"** 템플릿 선택
   - 템플릿 아이콘을 클릭하면 선택됨 (파란색 테두리 표시)

3. **프로젝트 이름 입력**
   - 화면 아래쪽 **"Project name"** 필드에 **"Tetris"** 입력
   - 한글 이름도 가능하지만 영문 권장

4. **프로젝트 위치 확인**
   - **"Location"** 필드에 프로젝트가 저장될 폴더 경로가 표시됨
   - 기본값으로 두거나 원하는 위치로 변경 가능

5. **"Create project" 버튼 클릭**
   - 화면 오른쪽 하단의 **"Create project"** 버튼 클릭
   - Unity 에디터가 자동으로 실행됨 (처음이면 시간이 걸릴 수 있음)

#### 1-3. Unity 에디터 화면 확인

Unity 에디터가 열리면 다음 창들이 보입니다:

- **Scene 뷰** (왼쪽 상단 큰 창): 게임 세계를 보는 창
- **Game 뷰** (Scene 뷰 옆 탭): 게임 실행 화면
- **Hierarchy 창** (왼쪽 하단): 씬의 오브젝트 목록
- **Inspector 창** (오른쪽): 선택한 오브젝트의 속성
- **Project 창** (아래 중앙): 프로젝트 파일 목록
- **Console 창** (Project 창 옆): 에러 메시지 확인

**창이 안 보이면?**
- 메뉴: **Window > General > [창 이름]** 클릭
- 또는 **Window > Layouts > Default**로 기본 레이아웃 복원

### 2. Scripts 폴더 만들기

#### 2-1. Project 창에서 폴더 생성

1. **Project 창 확인**
   - 화면 아래 중앙에 **"Project"** 창이 보임
   - "Assets" 폴더가 보임

2. **Assets 폴더 선택**
   - Project 창에서 **"Assets"** 폴더 클릭 (파란색으로 선택됨)

3. **폴더 생성**
   - **우클릭** → **"Create"** → **"Folder"** 선택
   - 또는 **Assets** 폴더 선택 상태에서 **우클릭** → **"Create > Folder"**

4. **폴더 이름 변경**
   - 생성된 "New Folder"를 **"Scripts"**로 변경
   - 방법:
     - 폴더를 클릭하고 잠시 기다린 후 다시 클릭
     - 또는 **F2** 키 누르기
     - 또는 폴더 선택 후 Inspector 창 상단의 이름 필드에서 변경

### 3. 첫 번째 스크립트 작성

#### 3-1. 스크립트 파일 생성

1. **Scripts 폴더 선택**
   - Project 창에서 **"Scripts"** 폴더 클릭

2. **C# 스크립트 생성**
   - **우클릭** → **"Create"** → **"C# Script"** 선택
   - 또는 **Scripts** 폴더 선택 상태에서 **우클릭** → **"Create > C# Script"**

3. **스크립트 이름 입력**
   - 생성된 "NewBehaviourScript"가 선택된 상태에서
   - **"HelloWorld"** 입력 후 **Enter** 키
   - 이름은 반드시 영문으로 (한글 사용 불가)

4. **스크립트 파일 확인**
   - Project 창의 Scripts 폴더에 **"HelloWorld.cs"** 파일이 생성됨
   - 파일 확장자 `.cs`는 C# 스크립트를 의미

#### 3-2. 스크립트 코드 작성

1. **스크립트 파일 열기**
   - Project 창에서 **"HelloWorld.cs"** 더블클릭
   - Visual Studio 또는 기본 에디터가 열림

2. **코드 작성**
   - 에디터에 기본 코드가 있음
   - 다음 코드로 **전체 교체**:

```csharp
using UnityEngine;

public class HelloWorld : MonoBehaviour
{
    void Start()
    {
        Debug.Log("안녕하세요, Unity!");
    }
}
```

### 4. 스크립트 실행

#### 4-1. 빈 GameObject 생성

1. **Hierarchy 창 확인**
   - 화면 왼쪽 하단의 **"Hierarchy"** 창 확인
   - "Main Camera"와 "Directional Light"가 보임

2. **빈 GameObject 생성**
   - **방법 1**: Hierarchy 창의 빈 공간에서 **우클릭** → **"Create Empty"** 선택
   - **방법 2**: 메뉴 바에서 **"GameObject"** → **"Create Empty"** 클릭

3. **이름 확인**
   - Hierarchy에 "GameObject"가 생성됨
   - 이름은 그대로 두어도 되고, 원하면 변경 가능

#### 4-2. 스크립트를 GameObject에 추가

1. **스크립트 드래그 앤 드롭**
   - Project 창에서 **"HelloWorld.cs"** 파일을 찾기
   - **HelloWorld.cs**를 **클릭하고 잡은 상태**로
   - Hierarchy의 **"GameObject"** 위로 **드래그**
   - GameObject 위에 놓으면 스크립트가 추가됨

2. **스크립트 추가 확인**
   - Hierarchy에서 **"GameObject"** 클릭
   - Inspector 창(오른쪽)을 확인
   - **"Hello World (Script)"** 컴포넌트가 보이면 성공!

**또는 Add Component 방법**:
1. Hierarchy에서 **"GameObject"** 선택
2. Inspector 창에서 **"Add Component"** 버튼 클릭
3. 검색창에 **"HelloWorld"** 입력
4. **"Hello World"** 클릭하여 추가

#### 4-3. 게임 실행 및 확인

1. **Play 버튼 클릭**
   - Unity 에디터 상단 중앙의 **▶ (Play)** 버튼 클릭
   - 버튼이 파란색으로 변하고 게임이 실행됨

2. **Console 창 확인**
   - 화면 아래 **"Console"** 창 확인
   - Console 창이 안 보이면: **Window > General > Console** 클릭
   - 또는 단축키: **Ctrl + Shift + C** (Windows) 또는 **Cmd + Shift + C** (Mac)

3. **메시지 확인**
   - Console 창에 **"안녕하세요, Unity!"** 메시지가 보이면 성공!
   - 메시지는 흰색으로 표시됨

4. **게임 정지**
   - **▶ (Play)** 버튼을 다시 클릭하여 정지
   - 또는 단축키: **Ctrl + P** (Windows) 또는 **Cmd + P** (Mac)

## ✅ 확인 사항

- [ ] Unity 프로젝트가 정상적으로 생성되었는가?
- [ ] 스크립트가 정상적으로 실행되는가?
- [ ] Console에 메시지가 출력되는가?

## ⚠️ 이 블로그와 참고 블로그의 차이점

**참고 블로그 방식** (웹사이트 기반 가이드):
- Unity 월드 좌표를 직접 사용: 블록 위치를 (5, 17)처럼 숫자로 직접 지정
- 간단한 방식: `transform.position`을 직접 변경
- Mathf.RoundToInt()로 소수점을 정수로 반올림하여 사용

**이 블로그 방식**:
- 논리적 좌표와 Unity 월드 좌표를 분리: 게임 보드 좌표계를 별도로 관리
- 더 정확한 방식: 논리적 좌표로 게임 로직 처리, Unity 좌표는 화면 표시용
- 정수 좌표만 사용: 소수점 문제 없이 정확한 위치 관리

**왜 이렇게 하나요?**
- 참고 블로그: 초보자가 쉽게 이해할 수 있도록 단순화
- 이 블로그: 더 정확하고 확장 가능한 방식으로 구현

## 📚 참고 자료

- [Unity 에디터 사용 가이드](../참고자료/Unity-에디터-사용가이드.md)
- [개념 설명 - C# 기초](../참고자료/개념설명.md#c-프로그래밍-개념)

---

[다음 단계: 2단계 - 게임 보드 만들기 →](./2단계-게임-보드-만들기.md)
