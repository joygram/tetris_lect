---
layout: default
title: GameObject
---

# GameObject

## 📖 개념 설명

**GameObject**는 Unity 게임 세계의 모든 오브젝트입니다.

- 빈 GameObject: 아무것도 없는 빈 상자
- Cube, Sphere 등: 기본 모양
- 사용자가 만든 오브젝트

**예시**:
- 게임 보드 = GameObject
- 테트리스 블록 = GameObject
- 카메라 = GameObject

---

## 🛠️ 실습: GameObject 생성·이름 변경·삭제

**목표**: Hierarchy에서 GameObject를 만들고 이름을 바꿔 봅니다.

### 이 실습 전용 씬 만들기 (환경 설정)

**먼저 이 실습 전용 씬을 만든 뒤** 아래 순서로 진행합니다. (자세한 씬 만드는 방법은 [개념 실습 테스트 환경 가이드](../개념-실습-테스트-환경-가이드.md)의 **씬 만드는 방법** 참고.)

**이 실습만** 할 전용 씬이 없으면 아래 순서로 **한 번만** 만듭니다. (이미 `ConceptTest_GameObject` 씬이 있으면 **File → Open Scene**으로 열고 아래 실습만 이어서 하세요.)

1. **File** → **New Scene** → **Basic (Built-in)** 또는 **Empty** → Create
2. **File** → **Save As** → 저장 위치: **Assets/Scenes** → 파일 이름: **ConceptTest_GameObject** → Save
3. 아래 실습은 **모두 이 씬에서** 진행합니다. (다른 문서로 왔다 갔다 하지 않습니다.)

---

### 수행 과정

1. **빈 GameObject 생성**
   - Hierarchy 창의 빈 공간에서 **우클릭**
   - **Create Empty** 선택
   - "GameObject"가 생성됨

2. **이름 변경**
   - Hierarchy에서 생성된 GameObject 클릭
   - 잠시 후 다시 클릭하거나 **F2** 키
   - 이름을 **"TestObject"**로 변경

3. **3D 오브젝트 생성**
   - Hierarchy에서 **우클릭**
   - **3D Object** → **Cube** 선택
   - "Cube"가 생성됨
   - 이름을 **"MyCube"**로 변경

4. **Inspector 확인**
   - Hierarchy에서 "MyCube" 클릭
   - Inspector(오른쪽)에 **Transform** 컴포넌트가 보임
   - Position, Rotation, Scale 값 확인

5. **정리**: Hierarchy에 보이는 각 항목이 하나의 **GameObject**입니다.

---

[← 개념 목록으로](../개념설명.md#-unity-개념)
