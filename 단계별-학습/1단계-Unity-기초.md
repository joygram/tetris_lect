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

## ⚠️ 블로그와 실제 구현

이 블로그는 **학습 목적**으로 작성되었으며, 실제 프로젝트의 모든 세부사항을 다루지 않을 수 있습니다. 각 단계에서 실제 구현과의 차이점이 있을 수 있으니, 실제 코드를 참고하시기 바랍니다.

## 📚 참고 자료

- [Unity 에디터 사용 가이드](../참고자료/Unity-에디터-사용가이드)
- [개념 설명 - C# 기초](../참고자료/개념설명#c-프로그래밍-개념)

---

[다음 단계: 2단계 - 게임 보드 만들기 →](./2단계-게임-보드-만들기)
