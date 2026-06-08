# MCP(Model Context Protocol): 외부 도구 연결

## MCP란?

에이전트가 **외부 도구나 데이터 소스에 접근**할 수 있게 해주는 표준 프로토콜입니다.  
MCP 서버를 연결하면 에이전트가 파일시스템, 데이터베이스, 외부 API 등을 직접 사용할 수 있습니다.

```
Claude Code  ←→  MCP 서버  ←→  외부 도구/데이터
                               (GitHub, SQLite, 파일시스템 등)
```

훅이 "Claude Code 내부 이벤트에 반응"한다면,  
MCP는 **Claude가 외부 세계에 직접 손을 뻗는** 방법입니다.

---

## MCP 서버 연결 방법

### CLI로 추가

```bash
claude mcp add 서버이름 -- 실행명령어
```

### settings.json에 직접 추가

```json
{
  "mcpServers": {
    "서버이름": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-이름", "옵션"]
    }
  }
}
```

### 연결 확인

```bash
claude mcp list
```

---

## 공개 MCP 서버 예시

| 서버 패키지 | 기능 | 연결 예시 |
|------------|------|-----------|
| `@modelcontextprotocol/server-filesystem` | 로컬 파일시스템 읽기/쓰기 | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem ~/projects` |
| `@modelcontextprotocol/server-github` | GitHub 이슈·PR·저장소 | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| `@modelcontextprotocol/server-sqlite` | SQLite DB 쿼리 | `claude mcp add db -- npx -y @modelcontextprotocol/server-sqlite ./tasks.db` |
| `@modelcontextprotocol/server-brave-search` | 웹 검색 | `claude mcp add search -- npx -y @modelcontextprotocol/server-brave-search` |

---

## task-manager + MCP 연결 예시

task-manager 디렉토리를 MCP 서버로 등록하면, 에이전트가 파일을 직접 읽고 씁니다.

```bash
claude mcp add task-manager -- npx -y @modelcontextprotocol/server-filesystem \
  $(pwd)/lessons/05-automation-extension/examples/task-manager
```

연결 후 에이전트에게 요청:
```
"task_manager.py 파일을 읽고 구현된 함수 목록을 알려줘."
"test_task_manager.py를 읽고 테스트가 없는 함수가 있는지 확인해줘."
```

에이전트가 MCP 도구를 통해 파일에 직접 접근해서 응답합니다.

---

## MCP 제거

```bash
claude mcp remove 서버이름
```

---

## 핵심 정리

```
✅ MCP = 에이전트가 외부 도구에 접근하는 표준 방법
✅ claude mcp add 로 서버 등록, claude mcp list 로 확인
✅ 파일시스템·GitHub·DB 등 다양한 공개 서버 존재
✅ 설정: settings.json의 mcpServers 또는 CLI
```
