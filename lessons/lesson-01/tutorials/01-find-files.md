# 실습 1: 터미널 명령어 사용하여 파일 찾기


## 소스코드 다운로드
> 사이트 방문해서 소스코드 다운로드
https://github.com/anthropics/claude-code


### 파일 갯수 확인
```
git ls-files | wc -l
```


### 스크린샷 디렉토리에서 파일 찾기

3일전 까지 생성된 파일 조회
```bash
find . -type f -mtime 3
```

6시간전 까지 생성된 파일 조회 (6 X 60)
```bash
find . -type f -mmin -360
```

6시간전 까지 생성된 파일 다른 경로로 복사
```bash
find . -type f -mmin -360 -exec cp {} ~/Projects/Workspaces/Screenshots/ \;
```

Claude Code 의 -p 옵션을 사용하여 찾기
```bash
find . -type f -mmin -360 | claude -p “이 파일중에서 사과게임 스크린샷을 찾아줘”
```