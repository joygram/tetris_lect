---
layout: default
title: 스코어 UI 표시 가이드
---

# 스코어 UI 표시 가이드

## 📚 이 가이드를 사용하는 방법

이 가이드는 Unity에서 테트리스 게임의 스코어, 줄 수, 레벨을 화면에 표시하는 UI를 만드는 방법을 단계별로 안내합니다.  
각 단계를 차근차근 따라하면 완전한 스코어 UI를 만들 수 있습니다.

**중요**: 각 단계를 완료한 후 반드시 테스트해보세요!

---

## 🎯 목표

게임 화면에 다음 정보를 표시합니다:
- **Score (점수)**: 현재 점수
- **Lines (줄 수)**: 제거한 줄의 개수
- **Level (레벨)**: 현재 레벨

---

## 📖 1단계: Canvas 생성

### 실습 1-1: Canvas 자동 생성

**목표**: Unity에서 UI를 사용하기 위한 Canvas를 만듭니다.

**단계**:

1. **Hierarchy 창 확인**
   - Unity 에디터 왼쪽 하단의 "Hierarchy" 창 확인
   - 현재 씬에 있는 모든 GameObject가 표시됨

2. **Canvas 자동 생성**
   - Hierarchy 창의 **빈 공간**에서 **우클릭**
   - 메뉴에서 **"UI > Canvas"** 선택
   - Unity가 자동으로 다음을 생성합니다:
     - **Canvas**: 모든 UI의 부모 오브젝트
     - **EventSystem**: UI 이벤트 처리 (자동 생성, 건드리지 않음)

3. **Canvas 확인**
   - Hierarchy에서 "Canvas" 클릭
   - Inspector 창에 **Canvas** 컴포넌트가 보이는지 확인
   - **Render Mode**: "Screen Space - Overlay" (기본값)

**설명**:
- **Canvas**: Unity에서 모든 UI 요소의 부모가 되는 오브젝트
- **Screen Space - Overlay**: UI가 항상 화면 맨 위에 표시됨 (게임 오브젝트 위에)
- **EventSystem**: 버튼 클릭 등 UI 이벤트를 처리 (자동 생성, 수정 불필요)

**확인 사항**:
- ✅ Hierarchy에 "Canvas"가 생성되었는가?
- ✅ Hierarchy에 "EventSystem"이 생성되었는가?
- ✅ Canvas의 Render Mode가 "Screen Space - Overlay"인가?

---

## 📖 2단계: 점수 표시 Text 생성

### 실습 2-1: ScoreText 생성

**목표**: 점수를 표시할 Text UI를 만듭니다.

**단계**:

1. **Canvas 선택**
   - Hierarchy에서 **"Canvas"** 클릭 (파란색으로 선택됨)

2. **Text 생성**
   - **Canvas를 선택한 상태**에서 Hierarchy 창의 빈 공간에서 **우클릭**
   - 메뉴에서 **"UI > Text - TextMeshPro"** 선택
     - 또는 **"UI > Legacy > Text"** 선택 (간단한 버전)
   - Unity가 TextMeshPro를 처음 사용하면 Import 창이 나타남
     - **"Import TMP Essentials"** 버튼 클릭
     - 잠시 기다리면 자동으로 Import 완료

3. **이름 변경**
   - Hierarchy에서 생성된 Text를 클릭
   - 이름을 **"ScoreText"**로 변경
   - 변경 방법:
     - Text를 클릭하고 잠시 기다린 후 다시 클릭
     - 또는 F2 키 누르기
     - 또는 Inspector 창 상단의 이름 필드에서 직접 입력

4. **텍스트 내용 설정**
   - Inspector 창에서 **Text (TextMeshPro)** 또는 **Text (Legacy)** 컴포넌트 찾기
   - **Text** 필드에 **"Score: 0"** 입력
   - **Font Size**: **24** 입력
   - **Color**: 흰색 선택 (색상 칸 클릭하여 Color Picker에서 흰색 선택)

5. **위치 조정 (Rect Transform)**
   - Inspector의 **Rect Transform** 컴포넌트에서:
     - **Pos X**: **400** (오른쪽으로 이동)
     - **Pos Y**: **200** (위로 이동)
     - **Width**: **200** (텍스트 영역 너비)
     - **Height**: **50** (텍스트 영역 높이)

**💡 초보자를 위한 설명**:
- **Rect Transform**: UI 요소의 위치와 크기를 설정하는 컴포넌트
- **Pos X, Y**: UI 요소의 위치 (앵커 기준)
- **Width, Height**: UI 요소의 크기
- **양수 X**: 오른쪽, **음수 X**: 왼쪽
- **양수 Y**: 위, **음수 Y**: 아래

**확인 사항**:
- ✅ Hierarchy에 "ScoreText"가 생성되었는가?
- ✅ Canvas의 자식으로 있는가? (Canvas 아래에 들여쓰기되어 표시)
- ✅ Inspector에서 Text가 "Score: 0"으로 설정되었는가?
- ✅ Game 뷰에서 텍스트가 보이는가?

---

## 📖 3단계: 줄 수 표시 Text 생성

### 실습 3-1: LinesText 생성

**목표**: 제거한 줄 수를 표시할 Text UI를 만듭니다.

**단계**:

1. **Canvas 선택**
   - Hierarchy에서 "Canvas" 클릭

2. **Text 생성**
   - Canvas 선택 후 우클릭
   - **"UI > Text - TextMeshPro"** 또는 **"UI > Legacy > Text"** 선택

3. **이름 변경**
   - Hierarchy에서 생성된 Text를 **"LinesText"**로 변경

4. **텍스트 내용 설정**
   - Inspector에서:
     - **Text**: **"Lines: 0"** 입력
     - **Font Size**: **24**
     - **Color**: 흰색

5. **위치 조정**
   - Inspector의 **Rect Transform**에서:
     - **Pos X**: **400** (ScoreText와 같은 X 위치)
     - **Pos Y**: **150** (ScoreText 아래 50픽셀)
     - **Width**: **200**
     - **Height**: **50**

**설명**:
- Pos Y를 ScoreText(200)보다 작게(150) 설정하여 아래에 배치
- Pos X는 같게 설정하여 세로로 정렬

**확인 사항**:
- ✅ "LinesText"가 생성되었는가?
- ✅ ScoreText 아래에 위치하는가?
- ✅ Game 뷰에서 두 텍스트가 세로로 정렬되어 보이는가?

---

## 📖 4단계: 레벨 표시 Text 생성

### 실습 4-1: LevelText 생성

**목표**: 현재 레벨을 표시할 Text UI를 만듭니다.

**단계**:

1. **Canvas 선택**
   - Hierarchy에서 "Canvas" 클릭

2. **Text 생성**
   - Canvas 선택 후 우클릭
   - **"UI > Text - TextMeshPro"** 또는 **"UI > Legacy > Text"** 선택

3. **이름 변경**
   - Hierarchy에서 생성된 Text를 **"LevelText"**로 변경

4. **텍스트 내용 설정**
   - Inspector에서:
     - **Text**: **"Level: 1"** 입력
     - **Font Size**: **24**
     - **Color**: 흰색

5. **위치 조정**
   - Inspector의 **Rect Transform**에서:
     - **Pos X**: **400** (다른 Text와 같은 X 위치)
     - **Pos Y**: **100** (LinesText 아래 50픽셀)
     - **Width**: **200**
     - **Height**: **50**

**확인 사항**:
- ✅ "LevelText"가 생성되었는가?
- ✅ LinesText 아래에 위치하는가?
- ✅ Game 뷰에서 세 개의 텍스트가 세로로 정렬되어 보이는가?

---

## 📖 5단계: GameController에 UI 연결

### 실습 5-1: Inspector에서 연결

**목표**: 만든 Text UI를 GameController 스크립트에 연결합니다.

**단계**:

1. **GameController GameObject 찾기**
   - Hierarchy에서 **"GameController"** GameObject 찾기
   - 없으면 빈 GameObject 생성 후 GameController 스크립트 추가

2. **GameController 선택**
   - Hierarchy에서 "GameController" 클릭
   - Inspector 창에 GameController 컴포넌트가 보이는지 확인

3. **UI 연결 (드래그 앤 드롭)**
   - Inspector의 GameController 컴포넌트에서:
     - **Score Text** 필드 찾기
     - Hierarchy에서 **"ScoreText"**를 **드래그**하여 Score Text 필드에 **드롭**
     - **Lines Text** 필드 찾기
     - Hierarchy에서 **"LinesText"**를 **드래그**하여 Lines Text 필드에 **드롭**
     - **Level Text** 필드 찾기
     - Hierarchy에서 **"LevelText"**를 **드롭**하여 Level Text 필드에 **드롭**

4. **연결 확인**
   - Inspector에서 각 필드에 Text 오브젝트가 연결되었는지 확인
   - 필드에 "None (Text)" 대신 "ScoreText (Text)" 등으로 표시되어야 함

**💡 초보자를 위한 설명**:
- **드래그 앤 드롭**: Hierarchy에서 Inspector로 직접 끌어다 놓기
- 이렇게 연결하면 GameController가 UI를 업데이트할 수 있음
- 연결하지 않으면 UI가 업데이트되지 않음 (null 체크로 안전)

**확인 사항**:
- ✅ Score Text 필드에 ScoreText가 연결되었는가?
- ✅ Lines Text 필드에 LinesText가 연결되었는가?
- ✅ Level Text 필드에 LevelText가 연결되었는가?

---

## 📖 6단계: 테스트 및 확인

### 실습 6-1: 게임 실행 및 확인

**목표**: UI가 제대로 작동하는지 확인합니다.

**단계**:

1. **게임 실행**
   - Unity 에디터 상단의 **Play 버튼** 클릭 (▶)
   - 게임이 시작됨

2. **초기 UI 확인**
   - Game 뷰에서 다음이 표시되는지 확인:
     - **Score: 0** (오른쪽 상단)
     - **Lines: 0** (Score 아래)
     - **Level: 1** (Lines 아래)

3. **게임 플레이**
   - 블록을 조작하여 줄을 채우기
   - 줄이 가득 차면 자동으로 제거됨

4. **UI 업데이트 확인**
   - 줄을 제거하면:
     - **Score**가 증가하는지 확인
     - **Lines**가 증가하는지 확인
     - 10줄마다 **Level**이 증가하는지 확인

5. **게임 정지**
   - **Stop 버튼** 클릭 (■)하여 게임 정지

**확인 사항**:
- ✅ 게임 시작 시 UI가 올바르게 표시되는가?
- ✅ 줄을 제거하면 점수가 증가하는가?
- ✅ 줄 수가 올바르게 표시되는가?
- ✅ 레벨이 올바르게 증가하는가?

---

## 🎨 고급 설정 (선택사항)

### 7단계: UI 스타일 개선

#### 실습 7-1: 폰트 크기 및 색상 조정

**목표**: UI를 더 보기 좋게 만듭니다.

**단계**:

1. **폰트 크기 조정**
   - 각 Text 선택
   - Inspector에서 **Font Size** 조정:
     - 작은 화면: 20~24
     - 큰 화면: 28~32

2. **색상 변경**
   - 각 Text 선택
   - Inspector에서 **Color** 변경:
     - Score: 노란색 (점수 강조)
     - Lines: 청록색
     - Level: 주황색

3. **정렬 설정**
   - Inspector에서 **Alignment** 설정:
     - 왼쪽 정렬: 왼쪽 아이콘 클릭
     - 중앙 정렬: 중앙 아이콘 클릭
     - 오른쪽 정렬: 오른쪽 아이콘 클릭

---

### 8단계: Panel 사용 (선택사항)

#### 실습 8-1: UI를 Panel로 그룹화

**목표**: 관련 UI를 Panel로 묶어서 관리하기 쉽게 만듭니다.

**단계**:

1. **Panel 생성**
   - Canvas 선택 후 우클릭
   - **"UI > Panel"** 선택
   - 이름을 **"GameInfoPanel"**로 변경

2. **Text를 Panel 자식으로 이동**
   - Hierarchy에서 **ScoreText**를 **드래그**하여 **GameInfoPanel** 위에 **드롭**
   - 같은 방법으로 **LinesText**, **LevelText**도 Panel 자식으로 이동

3. **Panel 위치 조정**
   - GameInfoPanel 선택
   - Inspector의 **Rect Transform**에서:
     - **Pos X**: 400
     - **Pos Y**: 150
   - Panel의 배경색은 Inspector의 **Image** 컴포넌트에서 **Color** 조정

**장점**:
- 여러 UI를 한 번에 이동/관리 가능
- Panel 배경색으로 구분 가능
- 더 체계적인 구조

---

## 📐 UI 배치 좌표 참고

### 권장 위치 (1920 x 1080 해상도 기준)

**오른쪽 상단 배치**:
```
ScoreText:  Pos X: 400,  Pos Y: 200
LinesText:  Pos X: 400,  Pos Y: 150
LevelText:  Pos X: 400,  Pos Y: 100
```

**왼쪽 상단 배치**:
```
ScoreText:  Pos X: -400,  Pos Y: 200
LinesText:  Pos X: -400,  Pos Y: 150
LevelText:  Pos X: -400,  Pos Y: 100
```

**위치 조정 팁**:
- Game 뷰에서 직접 확인하며 조정
- Scene 뷰에서도 UI 위치 확인 가능
- Rect Transform의 Anchor Presets로 화면 비율에 맞게 자동 조정 가능

---

## ❓ 문제 해결 가이드

### 문제: UI가 보이지 않아요

**해결**:
1. Canvas가 생성되었는지 확인
2. Canvas의 Render Mode가 "Screen Space - Overlay"인지 확인
3. Game 뷰에서 확인 (Scene 뷰가 아닌 Game 뷰)
4. Text의 Color가 배경과 같은 색이 아닌지 확인

### 문제: UI가 업데이트되지 않아요

**해결**:
1. GameController의 Inspector에서 Text가 연결되었는지 확인
2. GameController 스크립트가 GameObject에 추가되었는지 확인
3. Console 창에서 에러 메시지 확인
4. Play 모드에서 확인 (에디터 모드에서는 업데이트 안 됨)

### 문제: UI 위치가 맞지 않아요

**해결**:
1. Rect Transform의 Pos X, Y 값 확인
2. Anchor Presets 설정 확인 (기본값: 중앙)
3. Game 뷰의 해상도 확인 (1920 x 1080 권장)
4. Canvas Scaler 설정 확인

### 문제: 텍스트가 잘려요

**해결**:
1. Rect Transform의 Width, Height 값 증가
2. Font Size를 줄이기
3. Text의 Overflow 설정 확인 (Inspector에서)

### 문제: 드래그 앤 드롭이 안 돼요

**해결**:
1. Hierarchy와 Inspector 창이 모두 보이는지 확인
2. 정확한 필드에 드롭하는지 확인
3. Text 컴포넌트가 있는 GameObject를 드롭하는지 확인
4. GameController가 선택된 상태인지 확인

---

## ✅ 체크리스트

가이드를 완료한 후 확인 사항:

- [ ] Canvas가 생성되었는가?
- [ ] ScoreText, LinesText, LevelText가 모두 생성되었는가?
- [ ] 각 Text가 Canvas의 자식으로 있는가?
- [ ] GameController에 모든 Text가 연결되었는가?
- [ ] 게임 실행 시 UI가 표시되는가?
- [ ] 줄을 제거하면 점수가 증가하는가?
- [ ] 줄 수가 올바르게 표시되는가?
- [ ] 레벨이 올바르게 증가하는가?

---

## 🎉 완성!

축하합니다! 이제 테트리스 게임에 완전한 스코어 UI가 추가되었습니다!

### 완성된 기능
- ✅ 점수 표시 (Score)
- ✅ 줄 수 표시 (Lines)
- ✅ 레벨 표시 (Level)
- ✅ 실시간 업데이트

### 다음 단계 아이디어
1. **다음 블록 미리보기**: 다음에 나올 블록 표시
2. **홀드 블록**: 현재 블록을 보관하는 기능
3. **게임 오버 UI**: 게임 종료 시 최종 점수 표시
4. **하이스코어**: 최고 점수 저장 및 표시
5. **애니메이션**: 점수 증가 시 애니메이션 효과

---

**이 가이드를 따라하면 완전한 스코어 UI를 만들 수 있습니다!**  
**각 단계를 천천히 따라하고, 문제가 생기면 문제 해결 가이드를 참고하세요!** 🎮
