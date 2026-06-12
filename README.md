# Claude Code를 활용한 Agentic Coding

> 대상 : USG 공유대학교
> 컴퓨터공학 전공 4학년 대상 · 6시간 온라인 강의 · 실습 따라하기 중심
>
> 강사 : 하이브레인넷 (http://www.hibrain.net) 연구원



## 강의 개요

- **대상**: 컴퓨터공학 전공 4학년 (기본적인 프로그래밍/Git/터미널 사용 경험 보유 가정)
- **목표**: Claude Code를 활용해 "에이전트와 함께 코딩하는(Agentic Coding)" 방법을 익히고, 실제 개발 워크플로우에 적용할 수 있다.
- **방식**: 매 시간 강사가 개념을 설명한 뒤, 학생이 동일한 실습을 따라하며 진행 (이론 30% + 실습 70%)
- **사전 준비물**: 노트북, Node.js 설치, 터미널, 코드 에디터(VS Code 권장), Anthropic 계정/API 접근


---

## [1교시. Agentic Coding 입문](lessons/lesson-01/README.md)

- **핵심 개념**: Agentic Coding이란 무엇인가 (자동완성 → 에이전트 협업으로의 패러다임 변화), LLM 코딩 도구의 종류와 Claude Code의 위치
- **학습 목표**
  - Agentic Coding의 개념과 일반 코드 자동완성(Copilot 등)과의 차이를 설명할 수 있다.
  - 에이전트의 탐색→계획→실행→검증 루프를 이해하고, 사람의 역할이 무엇인지 설명할 수 있다.
- **발표자료**
  - [USG 공유대학 Agentic Coding 특강 - Lesson 1](https://drive.google.com/file/d/1GDb72t-8lCKDdlQT-pbHayfGrJKLtz4R/view?usp=share_link)
- **강의 문서**
  - [Agentic Coding이란 무엇인가?](lessons/lesson-01/docs/01-what-is-agentic-coding.md)
  - [Claude Code 깊이 들여다보기](lessons/lesson-01/docs/02-why-claude-code.md)
- **실습**
  - [실습 1: 터미널 명령어 사용하여 파일 찾기](lessons/lesson-01/tutorials/01-find-files.md)
- **산출물**: Agentic Coding 개념 이해 및 에이전트 루프 설명 가능

## [2교시. 개발 환경 설정과 기본 워크플로우](lessons/lesson-02/README.md)

- **핵심 개념**: OS별 개발 환경 구성 (macOS · Windows), Claude Code와 함께하는 코드 탐색·수정·질문 사이클, 에이전트의 작업 루프 실물 체험
- **학습 목표**
  - macOS 또는 Windows 환경에 개발 도구(터미널·Git·Python·VSCode·Claude Code)를 설치하고 동작을 확인할 수 있다.
  - 기존 코드베이스를 Claude Code로 탐색하고 이해할 수 있다.
  - 자연어 요청으로 코드를 수정하고 변경 사항을 리뷰할 수 있다.
- **발표자료**
  - [USG 공유대학 Agentic Coding 특강 - Lesson 2](https://drive.google.com/file/d/1iqumZuaDQuqSnqOOk22DRNZsnGzHBEM7/view?usp=share_link)
- **강의 문서**
  - [개발 환경 구성 개요](lessons/lesson-02/docs/01-environment-setup.md)
  - [기본 워크플로우: 탐색·질문·수정·검증](lessons/lesson-02/docs/02-basic-workflow.md)
  - [슬래시 커맨드 & CLI 개요](lessons/lesson-02/docs/03-slash-commands.md)
  - [슬래시 커맨드 심화 가이드](lessons/lesson-02/docs/04-slash-commands-deepdive.md)
- **실습**
  - [실습 1: macOS 환경 설정](lessons/lesson-02/tutorials/01-macos-setup.md)
  - [실습 2: Windows 환경 설정](lessons/lesson-02/tutorials/02-windows-setup.md)
  - [실습 3: 첫 번째 워크플로우](lessons/lesson-02/tutorials/03-first-workflow.md)
- **산출물**: 완성된 개발 환경 + 샘플 프로젝트 코드 설명 + 1건의 버그 수정

## [3교시. 효과적인 프롬프팅과 컨텍스트 관리](lessons/lesson-03/README.md)

- **핵심 개념**: 좋은 요청 작성법(명확성·범위·예시), CLAUDE.md를 통한 프로젝트 컨텍스트 주입, 컨텍스트 윈도우 관리, 계획 모드(Plan Mode)
- **학습 목표**
  - 모호한 요청과 좋은 요청의 차이를 이해하고 효과적인 프롬프트를 작성할 수 있다.
  - CLAUDE.md로 프로젝트 규칙·관례를 에이전트에게 전달할 수 있다.
- **발표자료**
  - [USG 공유대학 Agentic Coding 특강 - Lesson 3](https://drive.google.com/file/d/1ukd3EidqjSuSXDZ0akfK0I_ZRyE5wzVm/view?usp=share_link)
- **강의 문서**
  - [효과적인 프롬프팅](lessons/lesson-03/docs/01-effective-prompting.md)
  - [컨텍스트 관리: CLAUDE.md와 계획 모드](lessons/lesson-03/docs/02-context-management.md)
- **실습**
  - [실습 1: 핵심 슬래시 커맨드 실전 활용](lessons/lesson-03/tutorials/00-key-commands.md)
  - [실습 2: 나쁜 프롬프트 vs 좋은 프롬프트 비교](lessons/lesson-03/tutorials/01-prompt-comparison.md)
  - [심화 실습: 프롬프트 차이가 만드는 결과 비교](lessons/lesson-03/tutorials/01b-prompt-comparison-advanced.md)
  - [실습 3: CLAUDE.md 작성하기](lessons/lesson-03/tutorials/02-create-claude-md.md)
  - [실습 4: 계획 모드로 복잡한 작업 설계하기](lessons/lesson-03/tutorials/03-plan-mode.md)
- **산출물**: 프로젝트용 CLAUDE.md 파일 + 프롬프트 작성 체크리스트

## [4교시. 실전 개발: 기능 구현부터 디버깅·테스트까지](lessons/lesson-04/README.md)

- **핵심 개념**: TDD 스타일 협업, 점진적 기능 구현, 에러 메시지/스택트레이스 기반 디버깅, 테스트 작성·실행, Git 연동(커밋·PR)
- **학습 목표**
  - 작은 기능을 요구사항부터 구현·테스트까지 에이전트와 함께 완성할 수 있다.
  - 버그를 재현·진단·수정하는 디버깅 루프를 수행할 수 있다.
- **발표자료**
  - [USG 공유대학 Agentic Coding 특강 - Lesson 4](https://drive.google.com/file/d/1VN3vF8pDaECyjLN-5kkqZuNTIJLicsOe/view?usp=share_link)
- **강의 문서**
  - [TDD 스타일 에이전트 협업](lessons/lesson-04/docs/01-tdd-with-agent.md)
  - [에러 기반 디버깅 루프](lessons/lesson-04/docs/02-debugging-loop.md)
- **실습**
  - [실습 1: TDD 스타일 기능 구현](lessons/lesson-04/tutorials/01-feature-implementation.md)
  - [실습 2: 버그 찾기와 수정](lessons/lesson-04/tutorials/02-debugging-practice.md)
  - [실습 3: Git 커밋과 PR](lessons/lesson-04/tutorials/03-git-workflow.md)
- **산출물**: 테스트를 포함한 신규 기능 1건 + 커밋 이력

## [5교시. 자동화와 확장: 커스텀 커맨드·훅·MCP·서브에이전트](lessons/lesson-05/README.md)

- **핵심 개념**: 반복 작업 자동화(커스텀 슬래시 커맨드), 훅(Hooks)으로 동작 제어, MCP 서버로 외부 도구·데이터 연결, 서브에이전트로 작업 분리
- **학습 목표**
  - 자주 쓰는 작업을 커스텀 커맨드/훅으로 자동화할 수 있다.
  - MCP와 서브에이전트의 개념을 이해하고 간단히 활용할 수 있다.
- **발표자료**
  - [USG 공유대학 Agentic Coding 특강 - Lesson 5](https://drive.google.com/file/d/1qJBM20sazQwDqmG1JMuGhFsDU24AATJ5/view?usp=share_link)
- **강의 문서**
  - [스킬(Skill): 나만의 명령어 만들기](lessons/lesson-05/docs/01-skills.md)
  - [훅(Hooks): 특정 시점에 자동 실행](lessons/lesson-05/docs/02-hooks.md)
  - [MCP(Model Context Protocol): 외부 도구 연결](lessons/lesson-05/docs/03-mcp.md)
  - [서브에이전트: 탐색 작업 위임](lessons/lesson-05/docs/04-subagents.md)
- **실습**
  - [실습 1: 스킬(Skill) 만들기](lessons/lesson-05/tutorials/01-skills.md)
  - [실습 2: 훅(Hooks) 설정](lessons/lesson-05/tutorials/02-hooks.md)
  - [실습 3: MCP 서버 연결](lessons/lesson-05/tutorials/03-mcp.md)
  - [실습 4: 서브에이전트](lessons/lesson-05/tutorials/04-subagents.md)
- **산출물**: 커스텀 커맨드 1개 + 훅 설정 + MCP 연결 데모

## [6교시. 종합 프로젝트와 베스트 프랙티스](lessons/lesson-06/README.md)

- **핵심 개념**: 앞선 모든 내용을 결합한 미니 프로젝트, 안전한 사용·검증 습관, 한계와 주의점, 효율적 협업 워크플로우 정립
- **학습 목표**
  - 처음부터 끝까지 작은 프로젝트를 에이전트와 함께 완성할 수 있다.
  - Claude Code 활용의 베스트 프랙티스와 주의점을 설명할 수 있다.
- **발표자료**
  - [USG 공유대학 Agentic Coding 특강 - Lesson 6](https://drive.google.com/file/d/1KvR9OwVGZAvIxWgRK1TmvfIrHDmNb9cr/view?usp=share_link)
- **강의 문서**
  - [베스트 프랙티스와 주의점](lessons/lesson-06/docs/01-best-practices.md)
- **실습**
  - [실습 1: 미니 프로젝트 기획](lessons/lesson-06/tutorials/01-mini-project-planning.md)
  - [실습 2: 구현·테스트·문서화](lessons/lesson-06/tutorials/02-mini-project-implement.md)
  - [실습 3: 회고](lessons/lesson-06/tutorials/03-retrospective.md)
- **산출물**: 완성된 미니 프로젝트 + README + 회고 노트

---

## 디렉토리 구조

각 교시별 자료는 `lessons/` 하위에 저장한다.

```
lessons/
├── lesson-01/  # 1교시. Agentic Coding 입문
├── lesson-02/  # 2교시. 개발 환경 설정과 기본 워크플로우
├── lesson-03/  # 3교시. 효과적인 프롬프팅과 컨텍스트 관리
├── lesson-04/  # 4교시. 실전 개발: 기능 구현부터 디버깅·테스트까지
├── lesson-05/  # 5교시. 자동화와 확장: 커스텀 커맨드·훅·MCP·서브에이전트
└── lesson-06/  # 6교시. 종합 프로젝트와 베스트 프랙티스
```

각 lesson 디렉토리는 다음 하위 구조를 가진다.

- `docs/`      : 강의 설명 자료(개념·슬라이드용 마크다운)
- `tutorials/` : 단계별 실습 가이드(따라하기)
- `examples/`  : 예제 코드·샘플 프로젝트
- `assets/`    : 이미지·다이어그램 등 보조 자료

## 발표자료

- [USG 공유대학 Agentic Coding 특강 - Lesson 1](https://drive.google.com/file/d/1GDb72t-8lCKDdlQT-pbHayfGrJKLtz4R/view?usp=share_link)
- [USG 공유대학 Agentic Coding 특강 - Lesson 2](https://drive.google.com/file/d/1iqumZuaDQuqSnqOOk22DRNZsnGzHBEM7/view?usp=share_link)
- [USG 공유대학 Agentic Coding 특강 - Lesson 3](https://drive.google.com/file/d/1ukd3EidqjSuSXDZ0akfK0I_ZRyE5wzVm/view?usp=share_link)
- [USG 공유대학 Agentic Coding 특강 - Lesson 4](https://drive.google.com/file/d/1VN3vF8pDaECyjLN-5kkqZuNTIJLicsOe/view?usp=share_link)
- [USG 공유대학 Agentic Coding 특강 - Lesson 5](https://drive.google.com/file/d/1qJBM20sazQwDqmG1JMuGhFsDU24AATJ5/view?usp=share_link)
- [USG 공유대학 Agentic Coding 특강 - Lesson 6](https://drive.google.com/file/d/1KvR9OwVGZAvIxWgRK1TmvfIrHDmNb9cr/view?usp=share_link)
