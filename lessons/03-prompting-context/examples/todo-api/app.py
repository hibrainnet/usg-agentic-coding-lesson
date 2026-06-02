"""
Todo REST API (Flask)

엔드포인트:
    GET    /todos          — 전체 목록
    POST   /todos          — 새 항목 생성
    GET    /todos/<id>     — 단일 항목 조회
    PUT    /todos/<id>     — 항목 수정
    DELETE /todos/<id>     — 항목 삭제
"""

from flask import Flask, jsonify, request
from models import TodoStore

app = Flask(__name__)
store = TodoStore()


@app.route("/todos", methods=["GET"])
def get_todos():
    """전체 Todo 목록을 반환한다."""
    return jsonify(store.get_all())


@app.route("/todos", methods=["POST"])
def create_todo():
    """새 Todo를 생성한다."""
    data = request.get_json(silent=True) or {}
    todo = store.create(
        title=data.get("title", ""),
        done=data.get("done", False),
    )
    return jsonify(todo), 201


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id: int):
    """단일 Todo를 반환한다."""
    todo = store.get(todo_id)
    if todo is None:
        return jsonify({"error": "항목을 찾을 수 없습니다."}), 404
    return jsonify(todo)


@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id: int):
    """Todo를 수정한다."""
    todo = store.get(todo_id)
    if todo is None:
        return jsonify({"error": "항목을 찾을 수 없습니다."}), 404
    data = request.get_json(silent=True) or {}
    updated = store.update(todo_id, data)
    return jsonify(updated)


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    """Todo를 삭제한다."""
    success = store.delete(todo_id)
    if not success:
        return jsonify({"error": "항목을 찾을 수 없습니다."}), 404
    return "", 204


if __name__ == "__main__":
    app.run(port=4000)
