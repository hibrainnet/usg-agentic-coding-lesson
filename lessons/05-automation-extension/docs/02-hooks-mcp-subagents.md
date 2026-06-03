# 훅(Hooks), MCP, 서브에이전트

## 훅(Hooks): 특정 시점에 자동 실행

### 훅이란?

Claude Code가 특정 이벤트를 처리할 때 **자동으로 실행되는 쉘 명령어**입니다.  
에이전트에게 지시하지 않아도, 설정한 시점에 항상 실행됩니다.

### 설정 위치

`~/.claude/settings.json` (글로벌) 또는 `.claude/settings.json` (프로젝트)

```json
{
  "hooks": {
    "이벤트이름": [
      {
        "matcher": "매칭 조건 (선택)",
        "hooks": [
          {
            "type": "command",
            "command": "실행할 쉘 명령어"
          }
        ]
      }
    ]
  }
}
```

### 주요 이벤트

| 이벤트 | 발생 시점 |
|--------|-----------|
| `PostToolUse` | 에이전트가 도구를 사용한 직후 |
| `Stop` | 에이전트가 응답을 완료한 후 |
| `PreToolUse` | 에이전트가 도구를 사용하기 직전 |
| `Notification` | 에이전트가 알림을 보낼 때 |

### 예시 1: 작업 완료 시 소리 알림 (macOS)

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff"
          }
        ]
      }
    ]
  }
}
```

### 예시 2: Python 파일 수정 후 자동 포맷

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "black . --quiet 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

### 훅 사용 시 주의사항

- 훅은 **에이전트가 제어하지 못합니다** — 설정된 명령어가 항상 실행됩니다.
- 무거운 명령어(빌드, 테스트 전체 실행)를 훅에 넣으면 매우 느려집니다.
- `|| true`를 붙이면 훅 실패 시 에이전트 동작이 중단되지 않습니다.

---

## MCP(Model Context Protocol): 외부 도구 연결

### MCP란?

에이전트가 **외부 도구나 데이터 소스에 접근**할 수 있게 해주는 표준 프로토콜입니다.  
MCP 서버를 연결하면 에이전트가 파일시스템, 데이터베이스, 외부 API 등을 직접 사용할 수 있습니다.

```
Claude Code ←→ MCP 서버 ←→ 외부 도구/데이터
                             (GitHub, Slack, DB, 파일시스템 등)
```

### MCP 서버 연결 방법

Claude Code 설정에서 MCP 서버를 추가합니다.

```bash
# CLI로 추가
claude mcp add 서버이름 -- 실행명령어

# 예: filesystem MCP 서버
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /path/to/dir
```

또는 `settings.json`에 직접 추가:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/user/projects"]
    }
  }
}
```

### 공개 MCP 서버 예시

| 서버 | 기능 |
|------|------|
| `@modelcontextprotocol/server-filesystem` | 로컬 파일시스템 접근 |
| `@modelcontextprotocol/server-github` | GitHub 이슈·PR 조회/생성 |
| `@modelcontextprotocol/server-sqlite` | SQLite 데이터베이스 쿼리 |
| `@modelcontextprotocol/server-brave-search` | 웹 검색 |

---

## 서브에이전트: 탐색 작업 위임

### 서브에이전트란?

메인 에이전트가 **독립적인 하위 에이전트를 생성해 작업을 분리**하는 패턴입니다.  
긴 탐색 작업이나 독립적인 분석을 분리하면 메인 컨텍스트를 깔끔하게 유지할 수 있습니다.

Claude Code에서는 `/agent` 커맨드나 특정 프롬프트 패턴으로 서브에이전트를 활용합니다.

### 서브에이전트가 유용한 상황

```
✅ "이 디렉토리 전체에서 deprecated API 사용 패턴을 찾아줘"
✅ "50개 파일을 모두 읽고 의존성 맵을 그려줘"
✅ "테스트 파일을 전부 분석해서 커버리지 현황을 정리해줘"
```

이런 작업은 메인 대화 컨텍스트에서 직접 하면 컨텍스트가 금방 차서 대화가 느려집니다.

### 사용 방법

```
"넓은 탐색은 서브에이전트에 맡겨줘: 
 lessons/ 디렉토리 전체에서 파이썬 파일을 찾고
 각 파일에 테스트가 있는지 없는지 정리해줘."
```

에이전트가 별도 컨텍스트에서 탐색을 수행하고 결과만 돌려줍니다.

---

## 세 도구의 차이

| | 커스텀 커맨드 | 훅 | MCP | 서브에이전트 |
|--|--|--|--|--|
| **누가 실행하나** | 사람이 `/커맨드`로 호출 | 이벤트 발생 시 자동 | 에이전트가 요청 시 | 에이전트가 위임 |
| **무엇을 하나** | 반복 프롬프트 저장 | 쉘 명령어 자동 실행 | 외부 도구 접근 | 독립 탐색/분석 |
| **주요 사용처** | 코드 리뷰, 커밋 | 포맷, 알림 | DB, GitHub, 파일 | 대용량 탐색 |
