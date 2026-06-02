# Claude Code를 활용한 Agentic Coding

> 컴퓨터공학 전공 4학년 대상 · 6시간 온라인 강의 · 실습 따라하기 중심

## 강의 개요

- **대상**: 컴퓨터공학 전공 4학년 (기본적인 프로그래밍/Git/터미널 사용 경험 보유 가정)
- **목표**: Claude Code를 활용해 "에이전트와 함께 코딩하는(Agentic Coding)" 방법을 익히고, 실제 개발 워크플로우에 적용할 수 있다.
- **방식**: 매 시간 강사가 개념을 설명한 뒤, 학생이 동일한 실습을 따라하며 진행 (이론 30% + 실습 70%)
- **사전 준비물**: 노트북, Node.js 설치, 터미널, 코드 에디터(VS Code 권장), Anthropic 계정/API 접근

## 학습 흐름

```
1교시 소개·환경설정 → 2교시 기본 워크플로우 → 3교시 프롬프팅·컨텍스트
   → 4교시 실전 개발(기능·디버깅·테스트) → 5교시 자동화·확장 → 6교시 종합 프로젝트
```

---

## 1교시. Agentic Coding 입문

- **핵심 개념**: Agentic Coding이란 무엇인가 (자동완성 → 에이전트 협업으로의 패러다임 변화), LLM 코딩 도구의 종류와 Claude Code의 위치
- **학습 목표**
  - Agentic Coding의 개념과 일반 코드 자동완성(Copilot 등)과의 차이를 설명할 수 있다.
  - 에이전트의 탐색→계획→실행→검증 루프를 이해하고, 사람의 역할이 무엇인지 설명할 수 있다.
- **발표자료**
  - [USG 공유대학 Agentic Coding 특강 - Lesson 1](https://drive.google.com/file/d/1GDb72t-8lCKDdlQT-pbHayfGrJKLtz4R/view?usp=share_link)  
- **실습**
  - 강사 라이브 데모 관찰: Claude Code가 버그를 찾고 수정하는 과정 (탐색→계획→실행→검증 루프 실물 확인)
  - 자동완성 vs Agentic Coding 비교 토론
- **산출물**: Agentic Coding 개념 이해 및 에이전트 루프 설명 가능

## 2교시. 개발 환경 설정과 기본 워크플로우

- **핵심 개념**: OS별 개발 환경 구성 (macOS · Windows), Claude Code와 함께하는 코드 탐색·수정·질문 사이클, 에이전트의 작업 루프 실물 체험
- **학습 목표**
  - macOS 또는 Windows 환경에 개발 도구(터미널·Git·Python·VSCode·Claude Code)를 설치하고 동작을 확인할 수 있다.
  - 기존 코드베이스를 Claude Code로 탐색하고 이해할 수 있다.
  - 자연어 요청으로 코드를 수정하고 변경 사항을 리뷰할 수 있다.
- **발표자료**
  - [USG 공유대학 Agentic Coding 특강 - Lesson 2](https://drive.google.com/file/d/1iqumZuaDQuqSnqOOk22DRNZsnGzHBEM7/view?usp=share_link)  
- **실습**
  - OS 선택 후 단계별 설치 진행 (Ghostty/Windows Terminal → Homebrew/Git → Python3 → VSCode → Claude Code)
  - 설치 검증 및 Claude Code 첫 실행·인증
  - 샘플 프로젝트(To-Do CLI)를 Claude Code로 탐색: 구조 설명 요청, 기능 파악
  - 버그가 있는 함수를 찾아 수정, 슬래시 커맨드(`/help`, `/clear`) 체험
- **산출물**: 완성된 개발 환경 + 샘플 프로젝트 코드 설명 + 1건의 버그 수정

## 3교시. 효과적인 프롬프팅과 컨텍스트 관리

- **핵심 개념**: 좋은 요청 작성법(명확성·범위·예시), CLAUDE.md를 통한 프로젝트 컨텍스트 주입, 컨텍스트 윈도우 관리, 계획 모드(Plan Mode)
- **학습 목표**
  - 모호한 요청과 좋은 요청의 차이를 이해하고 효과적인 프롬프트를 작성할 수 있다.
  - CLAUDE.md로 프로젝트 규칙·관례를 에이전트에게 전달할 수 있다.
- **발표자료**
  - [USG 공유대학 Agentic Coding 특강 - Lesson 3](https://drive.google.com/file/d/1ukd3EidqjSuSXDZ0akfK0I_ZRyE5wzVm/view?usp=share_link)  
- **실습**
  - 동일 작업을 나쁜 프롬프트 vs 좋은 프롬프트로 요청하여 결과 비교
  - `/init`으로 CLAUDE.md 생성 후 코딩 컨벤션·명령어 추가
  - 큰 작업을 계획 모드로 먼저 설계한 뒤 실행하기
- **산출물**: 프로젝트용 CLAUDE.md 파일 + 프롬프트 작성 체크리스트

## 4교시. 실전 개발: 기능 구현부터 디버깅·테스트까지

- **핵심 개념**: TDD 스타일 협업, 점진적 기능 구현, 에러 메시지/스택트레이스 기반 디버깅, 테스트 작성·실행, Git 연동(커밋·PR)
- **학습 목표**
  - 작은 기능을 요구사항부터 구현·테스트까지 에이전트와 함께 완성할 수 있다.
  - 버그를 재현·진단·수정하는 디버깅 루프를 수행할 수 있다.
- **실습**
  - 샘플 앱에 신규 기능 추가(요구사항 → 구현 → 테스트)
  - 의도적으로 심어둔 버그를 에러 로그와 함께 디버깅
  - 변경 사항 커밋 및 커밋 메시지 작성, (선택) PR 생성
- **산출물**: 테스트를 포함한 신규 기능 1건 + 커밋 이력

## 5교시. 자동화와 확장: 커스텀 커맨드·훅·MCP·서브에이전트

- **핵심 개념**: 반복 작업 자동화(커스텀 슬래시 커맨드), 훅(Hooks)으로 동작 제어, MCP 서버로 외부 도구·데이터 연결, 서브에이전트로 작업 분리
- **학습 목표**
  - 자주 쓰는 작업을 커스텀 커맨드/훅으로 자동화할 수 있다.
  - MCP와 서브에이전트의 개념을 이해하고 간단히 활용할 수 있다.
- **실습**
  - 나만의 슬래시 커맨드 만들기(예: 코드 리뷰, 커밋 메시지 생성)
  - 간단한 훅 설정(예: 작업 완료 알림, 포맷 자동 실행)
  - MCP 서버 1개 연결 체험 및 서브에이전트로 탐색 작업 위임
- **산출물**: 커스텀 커맨드 1개 + 훅 설정 + MCP 연결 데모

## 6교시. 종합 프로젝트와 베스트 프랙티스

- **핵심 개념**: 앞선 모든 내용을 결합한 미니 프로젝트, 안전한 사용·검증 습관, 한계와 주의점, 효율적 협업 워크플로우 정립
- **학습 목표**
  - 처음부터 끝까지 작은 프로젝트를 에이전트와 함께 완성할 수 있다.
  - Claude Code 활용의 베스트 프랙티스와 주의점을 설명할 수 있다.
- **실습**
  - 미니 프로젝트(예: 간단한 To-Do API 또는 CLI 도구) 기획→구현→테스트→문서화
  - CLAUDE.md·커스텀 커맨드 등 자신만의 설정을 적용
  - 결과 회고: 잘된 점/실수, 검증 체크리스트 점검
- **산출물**: 완성된 미니 프로젝트 + README + 회고 노트

---

## 디렉토리 구조

각 교시별 자료는 `lessons/` 하위에 저장한다.

```
lessons/
├── 01-intro-setup/
├── 02-basic-workflow/
├── 03-prompting-context/
├── 04-real-development/
├── 05-automation-extension/
└── 06-capstone-project/
```

각 lesson 디렉토리는 다음 하위 구조를 가진다.

- `docs/`      : 강의 설명 자료(개념·슬라이드용 마크다운)
- `tutorials/` : 단계별 실습 가이드(따라하기)
- `examples/`  : 예제 코드·샘플 프로젝트
- `assets/`    : 이미지·다이어그램 등 보조 자료

## 발표자료

- [USG 공유대학 Agentic Coding 특강 - Lesson 1](https://drive.google.com/file/d/1GDb72t-8lCKDdlQT-pbHayfGrJKLtz4R/view?usp=share_link)
- [USG 공유대학 Agentic Coding 특강 - Lesson 2](https://drive.google.com/file/d/1iqumZuaDQuqSnqOOk22DRNZsnGzHBEM7/view?usp=share_link)
- [USG 공유대학 Agentic Coding 특강 - Lesson 3](https://drive.google.com/file/d/1ukd3EidqjSuSXDZ0akfK0I_ZRyE5wzVm/view?usp=share_link)
