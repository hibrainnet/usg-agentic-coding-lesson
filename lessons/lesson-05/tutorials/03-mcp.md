# 실습 3: MCP 서버 연결 (10분)

## 이번 실습 목표

MCP(Model Context Protocol) 서버를 연결해서, 에이전트가 task-manager 디렉토리 파일에 직접 접근하게 합니다.

---

## Step 1: Node.js 설치 확인

MCP 서버 대부분이 Node.js 기반입니다.

```bash
node --version   # v18 이상 권장
npm --version
```

없다면 [nodejs.org](https://nodejs.org)에서 설치합니다.

---

## Step 2: filesystem MCP 서버 연결

task-manager 프로젝트 디렉토리를 MCP 서버로 등록합니다.

```bash
claude mcp add task-manager -- npx -y @modelcontextprotocol/server-filesystem \
  $(pwd)/lessons/lesson-05/examples/task-manager
```

연결 확인:
```bash
claude mcp list
```

`task-manager`가 목록에 나오면 성공입니다.

---

## Step 3: MCP 도구로 task-manager 파일 조회

Claude Code를 새로 열고(또는 `/reset`) 에이전트에게 요청합니다.

```
"task-manager 폴더에 있는 파일 목록을 보여줘."
```

에이전트가 MCP를 통해 파일 시스템에 직접 접근해서 응답하는 것을 확인합니다.

이어서 더 구체적인 요청을 해봅니다.

```
"task_manager.py 파일의 내용을 읽어줘."
```

```
"test_task_manager.py를 읽고 어떤 함수들이 테스트되고 있는지 목록을 만들어줘."
```

---

## Step 4: (선택) SQLite MCP 서버로 task-manager 데이터 저장

task-manager 데이터를 SQLite 파일로 영속화하는 실습입니다.  
시간이 남을 경우 진행합니다.

```bash
claude mcp add sqlite -- npx -y @modelcontextprotocol/server-sqlite \
  $(pwd)/lessons/lesson-05/examples/task-manager/tasks.db
```

연결 후 에이전트에게 요청:
```
"tasks 테이블을 만들고, id(INTEGER), title(TEXT), done(INTEGER) 컬럼을 추가해줘."
```

```
"'pytest 테스트 작성' 태스크를 tasks 테이블에 추가해줘."
```

---

## Step 5: (선택) GitHub MCP 서버

GitHub 계정이 있다면 GitHub MCP 서버도 연결해볼 수 있습니다.

```bash
# GitHub Personal Access Token 필요
claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

연결 후:
```
"내 GitHub 저장소 목록을 보여줘."
```

---

## 체크리스트

- [ ] `claude mcp add`로 task-manager MCP 서버를 등록했다
- [ ] `claude mcp list`로 등록된 서버를 확인했다
- [ ] 에이전트가 MCP를 통해 task-manager 파일에 접근하는 것을 확인했다
- [ ] (선택) SQLite 또는 GitHub MCP 서버도 연결해봤다
