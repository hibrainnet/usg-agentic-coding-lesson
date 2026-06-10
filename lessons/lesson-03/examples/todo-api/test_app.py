"""
Todo API 테스트

실행:
    pytest test_app.py -v
"""

import pytest
from app import app, store


@pytest.fixture(autouse=True)
def reset_store():
    """각 테스트 전 저장소 초기화."""
    store._todos = {}
    store._next_id = 1


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_create_todo(client):
    resp = client.post("/todos", json={"title": "우유 사기"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["title"] == "우유 사기"
    assert data["done"] is False
    assert "id" in data


def test_get_all_todos(client):
    client.post("/todos", json={"title": "우유 사기"})
    client.post("/todos", json={"title": "빵 사기"})
    resp = client.get("/todos")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 2


def test_get_single_todo(client):
    client.post("/todos", json={"title": "우유 사기"})
    resp = client.get("/todos/1")
    assert resp.status_code == 200
    assert resp.get_json()["id"] == 1


def test_get_nonexistent_todo(client):
    resp = client.get("/todos/999")
    assert resp.status_code == 404
    assert "error" in resp.get_json()


def test_update_todo(client):
    client.post("/todos", json={"title": "우유 사기"})
    resp = client.put("/todos/1", json={"done": True})
    assert resp.status_code == 200
    assert resp.get_json()["done"] is True


def test_update_nonexistent_todo(client):
    resp = client.put("/todos/999", json={"done": True})
    assert resp.status_code == 404


def test_delete_todo(client):
    client.post("/todos", json={"title": "우유 사기"})
    resp = client.delete("/todos/1")
    assert resp.status_code == 204
    assert client.get("/todos/1").status_code == 404


def test_delete_nonexistent_todo(client):
    resp = client.delete("/todos/999")
    assert resp.status_code == 404
