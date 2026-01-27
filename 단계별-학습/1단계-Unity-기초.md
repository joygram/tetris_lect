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

1. Unity Hub 실행
2. **New Project** 클릭
3. **2D** 템플릿 선택
4. 프로젝트 이름: "Tetris"
5. **Create Project** 클릭

### 2. 첫 번째 스크립트 작성

`Assets/Scripts` 폴더에 `HelloWorld.cs` 생성:

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

### 3. 스크립트 실행

1. 빈 GameObject 생성 (GameObject > Create Empty)
2. `HelloWorld` 스크립트를 GameObject에 드래그
3. **Play** 버튼 클릭
4. Console 창에서 메시지 확인

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
