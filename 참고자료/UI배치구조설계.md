---
layout: default
title: UI 배치 구조 설계
---

# UI 배치 구조 설계

## 📖 이 문서는?

테트리스 게임의 UI(사용자 인터페이스)를 어떻게 배치할지 설계한 문서입니다.  
중학생도 이해할 수 있도록 단계별로 설명합니다.

---

## 🎨 전체 UI 레이아웃

### 화면 구성

**전체 화면 레이아웃**:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ┌──────────────────┐    ┌─────────────────────────┐ │
│  │                  │    │  Score: 1000            │ │
│  │                  │    │  Lines: 15              │ │
│  │   게임 보드       │    │  Level: 2               │ │
│  │   (10x20 그리드)  │    │                         │ │
│  │                  │    │  [다음 블록 미리보기]   │ │
│  │                  │    │  (선택사항)             │ │
│  │                  │    │                         │ │
│  │                  │    │  [홀드 블록]            │ │
│  │                  │    │  (선택사항)             │ │
│  │                  │    │                         │ │
│  └──────────────────┘    └─────────────────────────┘ │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**설명**:
- **왼쪽**: 게임 보드 (10x20 그리드) - 실제 게임이 진행되는 영역
- **오른쪽**: UI 정보 패널
  - 점수, 줄 수, 레벨 표시 (필수)
  - 다음 블록 미리보기 (선택사항)
  - 홀드 블록 (선택사항)

**좌표 기준**:
- 화면 중앙: (0, 0)
- 왼쪽: 음수 X
- 오른쪽: 양수 X
- 위: 양수 Y
- 아래: 음수 Y

---

## 📐 Canvas 구조

### Hierarchy 구조

**기본 구조 (필수)**:
```
Canvas
├─ EventSystem (자동 생성됨 - 건드리지 않음)
├─ ScoreText
├─ LinesText
└─ LevelText
```

**고급 구조 (선택사항 - Panel 사용)**:
```
Canvas
├─ EventSystem (자동 생성)
├─ GameInfoPanel (게임 정보 패널)
│  ├─ ScoreText
│  ├─ LinesText
│  └─ LevelText
├─ NextPiecePanel (다음 블록 미리보기 - 선택사항)
│  └─ NextPiecePreview
└─ HoldPiecePanel (홀드 블록 - 선택사항)
   └─ HoldPiecePreview
```

**설명**:
- **Canvas**: 모든 UI의 부모 오브젝트
- **EventSystem**: UI 이벤트 처리 (자동 생성, 건드리지 않음)
- **Panel**: 관련 UI를 묶는 그룹 (선택사항)
  - Panel을 사용하면 여러 UI를 한 번에 이동/관리 가능
  - 배경색 추가 가능

**초보자를 위한 권장 구조**:
- 처음에는 Panel 없이 Canvas 아래에 직접 Text 배치
- 나중에 Panel을 사용하여 정리

---

## 🎯 기본 UI 배치 (필수)

### 1. Canvas 설정

**위치**: Hierarchy 최상위

**설정**:
- **Render Mode**: Screen Space - Overlay (기본값)
- **Canvas Scaler**: Scale With Screen Size
  - Reference Resolution: 1920 x 1080
  - Match: 0.5 (가로 세로 비율 유지)

**설정 방법**:
1. Hierarchy에서 "Canvas" 선택
2. Inspector에서 Canvas 컴포넌트 확인
3. Render Mode: "Screen Space - Overlay" (기본값)
4. Canvas Scaler 컴포넌트 추가 (없으면)
5. UI Scale Mode: "Scale With Screen Size" 선택

---

### 2. 점수 표시 (ScoreText)

**위치**: 화면 오른쪽 상단

**설정**:
- **이름**: ScoreText
- **부모**: Canvas (직접)
- **위치**: 
  - Pos X: 400 (오른쪽)
  - Pos Y: 200 (위)
- **크기**: 
  - Width: 200
  - Height: 50
- **텍스트**:
  - Text: "Score: 0"
  - Font Size: 24
  - Color: 흰색
  - Alignment: 왼쪽 정렬

**생성 방법**:
1. Canvas 선택
2. 우클릭 > UI > Text - TextMeshPro (또는 Legacy > Text)
3. 이름을 "ScoreText"로 변경
4. Inspector에서 위치와 텍스트 설정

---

### 3. 줄 수 표시 (LinesText)

**위치**: ScoreText 아래

**설정**:
- **이름**: LinesText
- **부모**: Canvas
- **위치**: 
  - Pos X: 400 (ScoreText와 같은 X)
  - Pos Y: 150 (ScoreText 아래 50픽셀)
- **크기**: 
  - Width: 200
  - Height: 50
- **텍스트**:
  - Text: "Lines: 0"
  - Font Size: 24
  - Color: 흰색

**생성 방법**:
1. Canvas 선택
2. 우클릭 > UI > Text
3. 이름을 "LinesText"로 변경
4. Inspector에서 위치 설정 (Pos Y를 ScoreText보다 작게)

---

### 4. 레벨 표시 (LevelText)

**위치**: LinesText 아래

**설정**:
- **이름**: LevelText
- **부모**: Canvas
- **위치**: 
  - Pos X: 400
  - Pos Y: 100 (LinesText 아래 50픽셀)
- **크기**: 
  - Width: 200
  - Height: 50
- **텍스트**:
  - Text: "Level: 1"
  - Font Size: 24
  - Color: 흰색

**생성 방법**:
1. Canvas 선택
2. 우클릭 > UI > Text
3. 이름을 "LevelText"로 변경
4. Inspector에서 위치 설정

---

## 📊 UI 배치 좌표 시스템

### Anchor와 Pivot 이해

**Anchor (앵커)**:
- UI 요소가 어디에 고정될지 결정
- 예: 오른쪽 상단에 고정

**Pivot (피벗)**:
- UI 요소의 중심점
- 기본값: (0.5, 0.5) = 중앙

**Rect Transform 설명**:
```
Rect Transform
├─ Anchor Presets: 어디에 고정할지
├─ Pos X, Y: 위치 (앵커 기준)
├─ Width, Height: 크기
└─ Pivot: 중심점
```

---

### 권장 배치 좌표

**화면 기준 좌표** (1920 x 1080 기준):

| UI 요소 | Pos X | Pos Y | 설명 |
|---------|-------|-------|------|
| ScoreText | 400 | 200 | 오른쪽 상단 |
| LinesText | 400 | 150 | ScoreText 아래 |
| LevelText | 400 | 100 | LinesText 아래 |

**다른 해상도에서도 작동하도록**:
- Canvas Scaler 사용
- 또는 Anchor를 오른쪽 상단으로 설정

---

## 🎨 UI 스타일 가이드

### 색상

**기본 색상**:
- **텍스트**: 흰색 (Color.white)
- **배경**: 투명 또는 반투명 검정

**강조 색상** (선택사항):
- **점수**: 노란색 (레벨 업 시)
- **레벨**: 주황색

---

### 폰트

**기본 폰트**:
- Unity 기본 폰트 또는 TextMeshPro
- **크기**: 24pt (가독성 좋음)

**제목 폰트** (선택사항):
- **크기**: 32pt
- **스타일**: Bold

---

## 🔧 고급 UI 배치 (선택사항)

### Panel 사용하기

**Panel이란?**
- 여러 UI 요소를 묶는 컨테이너
- 배경색과 테두리 추가 가능

**GameInfoPanel 생성**:
1. Canvas 선택
2. 우클릭 > UI > Panel
3. 이름: "GameInfoPanel"
4. Inspector에서:
   - Image 컴포넌트의 Color를 반투명 검정으로 설정
   - Rect Transform에서 크기 조정

**Text를 Panel 안으로 이동**:
1. Hierarchy에서 ScoreText, LinesText, LevelText 선택
2. GameInfoPanel로 드래그 앤 드롭
3. 자동으로 Panel의 자식이 됨

**장점**:
- Panel을 이동하면 모든 Text가 함께 이동
- 배경색으로 구분 가능

---

### Anchor 설정하기

**오른쪽 상단에 고정**:

1. **ScoreText 선택**
2. Inspector의 Rect Transform에서
3. **Anchor Presets** 아이콘 클릭 (왼쪽 상단의 작은 사각형)
4. **오른쪽 상단** 선택 (Shift + Alt 함께 누르면 위치도 함께 이동)
5. Pos X, Y를 0으로 설정 (앵커 기준)

**결과**:
- 화면 크기가 바뀌어도 항상 오른쪽 상단에 위치

---

## 📱 반응형 UI (다양한 화면 크기 대응)

### Canvas Scaler 설정

**목표**: 다양한 화면 크기에서도 UI가 올바르게 보이도록

**설정 방법**:
1. Canvas 선택
2. Inspector에서 Canvas Scaler 컴포넌트 확인
3. 설정:
   - **UI Scale Mode**: Scale With Screen Size
   - **Reference Resolution**: 
     - X: 1920
     - Y: 1080
   - **Screen Match Mode**: Match Width Or Height
   - **Match**: 0.5

**설명**:
- Reference Resolution: 기준 해상도
- Match: 0 = 너비 기준, 1 = 높이 기준, 0.5 = 둘 다 고려

---

## 🎯 UI 배치 체크리스트

### 기본 UI (필수)

- [ ] Canvas 생성
- [ ] ScoreText 생성 및 배치
- [ ] LinesText 생성 및 배치
- [ ] LevelText 생성 및 배치
- [ ] 모든 Text가 화면에 보이는지 확인
- [ ] GameController에 연결

### 고급 UI (선택사항)

- [ ] Panel 생성
- [ ] Anchor 설정
- [ ] Canvas Scaler 설정
- [ ] 다음 블록 미리보기
- [ ] 홀드 블록 표시

---

## 💡 UI 배치 팁

1. **일관성**: 모든 UI 요소의 간격을 동일하게
2. **가독성**: 폰트 크기를 충분히 크게
3. **위치**: 중요한 정보는 눈에 잘 띄는 곳에
4. **색상**: 배경과 대비가 명확하게
5. **테스트**: 다양한 화면 크기에서 테스트

---

## 📐 실제 배치 예시

### 단계별 배치

**1단계: Canvas 생성**
- Hierarchy > 우클릭 > UI > Canvas

**2단계: ScoreText 배치**
```
Canvas
└─ ScoreText
   - Pos X: 400
   - Pos Y: 200
   - Text: "Score: 0"
```

**3단계: LinesText 배치**
```
Canvas
├─ ScoreText (Y: 200)
└─ LinesText (Y: 150) ← 50픽셀 아래
```

**4단계: LevelText 배치**
```
Canvas
├─ ScoreText (Y: 200)
├─ LinesText (Y: 150)
└─ LevelText (Y: 100) ← 50픽셀 아래
```

---

## 🔍 UI 확인 방법

### Scene 뷰에서 확인

1. Scene 뷰에서 Canvas 선택
2. Canvas가 보이는지 확인
3. Text들이 올바른 위치에 있는지 확인

### Game 뷰에서 확인

1. Play 버튼 클릭
2. Game 뷰에서 UI가 보이는지 확인
3. 텍스트가 읽기 쉬운지 확인

---

## ❓ 자주 묻는 질문

**Q: UI가 화면 밖에 있어요.**  
A: Rect Transform의 Pos X, Y 값을 조정하세요. 음수 값도 가능합니다.

**Q: 화면 크기를 바꾸면 UI가 이상해져요.**  
A: Canvas Scaler를 설정하거나 Anchor를 사용하세요.

**Q: Text가 너무 작아요.**  
A: Font Size를 늘리세요 (예: 24 → 32).

**Q: 여러 Text를 한 번에 이동하고 싶어요.**  
A: Panel을 사용하여 묶으세요.

---

**이 가이드를 참고하여 UI를 배치하세요!** 🎨
