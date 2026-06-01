"""
Todo 데이터 저장소 (인메모리)
"""


class TodoStore:
    """메모리 기반 Todo 저장소."""

    def __init__(self) -> None:
        self._todos: dict[int, dict] = {}
        self._next_id: int = 1

    def get_all(self) -> list[dict]:
        """저장된 모든 Todo를 반환한다."""
        return list(self._todos.values())

    def get(self, todo_id: int) -> dict | None:
        """ID에 해당하는 Todo를 반환한다. 없으면 None."""
        return self._todos.get(todo_id)

    def create(self, title: str, done: bool = False) -> dict:
        """새 Todo를 생성하고 반환한다."""
        todo = {"id": self._next_id, "title": title, "done": done}
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo

    def update(self, todo_id: int, data: dict) -> dict:
        """ID에 해당하는 Todo를 업데이트하고 반환한다."""
        todo = self._todos[todo_id]
        if "title" in data:
            todo["title"] = data["title"]
        if "done" in data:
            todo["done"] = data["done"]
        return todo

    def delete(self, todo_id: int) -> bool:
        """ID에 해당하는 Todo를 삭제한다. 성공 여부를 반환한다."""
        if todo_id not in self._todos:
            return False
        del self._todos[todo_id]
        return True
