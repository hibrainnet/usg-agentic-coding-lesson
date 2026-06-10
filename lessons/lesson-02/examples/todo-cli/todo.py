"""
간단한 할 일 관리 CLI

사용법:
    python3 todo.py add "할 일 내용"
    python3 todo.py list
    python3 todo.py done <번호>
"""

import json
import os
import sys

DATA_FILE = "todos.json"


def load_todos():
    """저장된 할 일 목록을 불러온다."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_todos(todos):
    """할 일 목록을 파일에 저장한다."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add_todo(text):
    """새 할 일을 추가한다."""
    todos = load_todos()
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print(f"추가됨: {text}")


def list_todos():
    """저장된 할 일 목록을 출력한다."""
    todos = load_todos()
    if not todos:
        print("할 일이 없습니다.")
        return
    for i, todo in enumerate(todos, start=1):
        status = "✓" if todo["done"] else "○"
        print(f"{i}. [{status}] {todo['text']}")


def complete_todo(n):
    """n번 할 일을 완료 처리한다."""
    todos = load_todos()
    if n < 1 or n > len(todos):
        print(f"오류: 1~{len(todos)} 사이의 번호를 입력하세요.")
        return
    todos[n]["done"] = True
    save_todos(todos)
    print(f"완료: {todos[n]['text']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python3 todo.py [add|list|done] [인수]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("오류: 할 일 내용을 입력하세요.")
        else:
            add_todo(" ".join(sys.argv[2:]))
    elif command == "list":
        list_todos()
    elif command == "done":
        if len(sys.argv) < 3:
            print("오류: 완료할 항목 번호를 입력하세요.")
        else:
            complete_todo(int(sys.argv[2]))
    else:
        print(f"알 수 없는 명령: {command}")
        print("사용법: python3 todo.py [add|list|done] [인수]")
