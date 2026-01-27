# GitHub Pages 배포 가이드

이 강의 자료를 GitHub Pages 블로그로 게시하는 방법입니다.

## 📋 사전 준비

1. GitHub 계정이 있어야 합니다
2. 이 저장소를 GitHub에 푸시해야 합니다

## 🚀 배포 방법

### 방법 1: GitHub Actions (자동 배포) - 추천

1. GitHub 저장소의 **Settings** → **Pages**로 이동
2. **Source**에서 **GitHub Actions** 선택
3. 저장소에 `.github/workflows/jekyll.yml` 파일이 자동으로 생성됩니다
4. `main` 브랜치에 푸시하면 자동으로 배포됩니다

### 방법 2: GitHub Pages 직접 설정

1. GitHub 저장소의 **Settings** → **Pages**로 이동
2. **Source**에서 **Deploy from a branch** 선택
3. **Branch**를 `main` 또는 `gh-pages`로 선택
4. **Folder**를 `/ (root)`로 선택
5. **Save** 클릭

### 방법 3: 로컬에서 빌드 후 배포

```bash
# Jekyll 설치 (Ruby 필요)
gem install bundler
bundle install

# 로컬에서 미리보기
bundle exec jekyll serve

# 빌드
bundle exec jekyll build

# _site 폴더의 내용을 gh-pages 브랜치에 푸시
```

## 🔧 설정 확인

배포 후 다음 URL에서 확인할 수 있습니다:
- `https://[사용자명].github.io/[저장소명]/`

예: `https://username.github.io/tetris/`

## 📝 주의사항

- 마크다운 파일의 경로가 올바른지 확인하세요
- 한국어 파일명이 제대로 작동하는지 확인하세요
- `_config.yml`의 `baseurl`이 저장소 이름과 일치하는지 확인하세요

## 🐛 문제 해결

### 페이지가 표시되지 않는 경우

1. GitHub Pages 설정에서 올바른 브랜치가 선택되었는지 확인
2. `_config.yml`의 설정 확인
3. Actions 탭에서 빌드 오류 확인

### 한국어가 깨지는 경우

1. `_config.yml`에 `encoding: utf-8`이 설정되어 있는지 확인
2. 마크다운 파일이 UTF-8 인코딩인지 확인

### 링크가 작동하지 않는 경우

1. 파일 경로가 올바른지 확인 (대소문자 구분)
2. `.md` 확장자 없이 링크 작성 확인
