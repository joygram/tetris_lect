---
layout: default
title: Component
---

# Component (컴포넌트)

## 📖 개념 설명

**Component**는 GameObject에 추가되는 기능입니다.

```csharp
gameObject.AddComponent<TetrisBlock>();
```

**주요 컴포넌트**:
- **Transform**: 위치, 회전, 크기
- **Renderer**: 화면에 그리기
- **Collider**: 충돌 감지
- **Rigidbody**: 물리 효과

**테트리스 예시**:
- TetrisBlock 컴포넌트: 블록 이동 기능
- GameBoard 컴포넌트: 보드 관리 기능

---

## 🛠️ 실습: 컴포넌트 추가·확인하기

**목표**: GameObject에 스크립트(컴포넌트)를 추가하고 Inspector에서 확인합니다.

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

**이 실습만** 할 전용 씬이 없으면 아래 순서로 **한 번만** 만듭니다. (이미 `ConceptTest_Component` 씬이 있으면 **File → Open Scene**으로 열고 아래 실습만 이어서 하세요.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_Component** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다. (다른 문서로 왔다 갔다 하지 않습니다.)

---

### 수행 과정

1. **빈 GameObject 생성**
   - Hierarchy에서 우클릭 → Create Empty
   - 이름: **"ComponentTest"**

2. **스크립트 컴포넌트 추가**
   - Hierarchy에서 "ComponentTest" 클릭
   - Inspector에서 **Add Component** 버튼 클릭
   - 검색창에 **"Transform"** 입력 (이미 있음)
   - **Add Component**에서 **"Scripts"** → **"Hello World"** 또는 아무 스크립트 선택
   - (HelloWorld가 없다면) Project에서 아무 C# 스크립트를 ComponentTest에 **드래그 앤 드롭**

3. **Inspector에서 확인**
   - ComponentTest를 선택한 상태에서 Inspector 확인
   - **Transform** 컴포넌트 (항상 있음)
   - **스크립트** 컴포넌트 (방금 추가한 것)
   - → 하나의 GameObject에 여러 **Component**가 붙어 있음을 확인!

4. **컴포넌트 제거**
   - Inspector에서 스크립트 컴포넌트 우측 **⋮** (또는 우클릭) → **Remove Component**
   - 해당 컴포넌트만 사라지고 GameObject는 남음

5. **정리**: GameObject는 빈 상자이고, **Component**를 붙여야 기능이 생깁니다.

---

[← 개념 목록으로](../개념설명.md#-unity-개념)
