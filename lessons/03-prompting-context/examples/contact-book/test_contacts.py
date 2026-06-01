"""
contacts 모듈 테스트

실행:
    pytest test_contacts.py -v
"""

import os
import pytest
from contacts import add_contact, list_contacts, search_contacts, delete_contact
from storage import load_contacts

DATA_FILE = "contacts.json"


def setup_function():
    """테스트 전 데이터 파일 초기화."""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)


def test_add_contact():
    add_contact("홍길동", "010-1234-5678")
    contacts = load_contacts()
    assert len(contacts) == 1
    assert contacts[0]["name"] == "홍길동"
    assert contacts[0]["phone"] == "010-1234-5678"
    assert contacts[0]["email"] == ""


def test_add_contact_with_email():
    add_contact("김철수", "010-9999-0000", "kim@example.com")
    contacts = load_contacts()
    assert contacts[0]["email"] == "kim@example.com"


def test_add_multiple_contacts_assigns_unique_ids():
    add_contact("홍길동", "010-1111-1111")
    add_contact("김철수", "010-2222-2222")
    contacts = load_contacts()
    ids = [c["id"] for c in contacts]
    assert len(set(ids)) == 2


def test_list_contacts_empty(capsys):
    list_contacts()
    captured = capsys.readouterr()
    assert "없습니다" in captured.out


def test_list_contacts(capsys):
    add_contact("홍길동", "010-1234-5678")
    list_contacts()
    captured = capsys.readouterr()
    assert "홍길동" in captured.out
    assert "010-1234-5678" in captured.out


def test_search_by_name():
    add_contact("홍길동", "010-1234-5678")
    add_contact("김철수", "010-9999-0000")
    contacts = load_contacts()
    results = [c for c in contacts if "홍" in c["name"]]
    assert len(results) == 1
    assert results[0]["name"] == "홍길동"


def test_search_by_phone(capsys):
    add_contact("홍길동", "010-1234-5678")
    search_contacts("1234")
    captured = capsys.readouterr()
    assert "홍길동" in captured.out


def test_search_no_result(capsys):
    add_contact("홍길동", "010-1234-5678")
    search_contacts("없는키워드")
    captured = capsys.readouterr()
    assert "없습니다" in captured.out


def test_delete_contact():
    add_contact("홍길동", "010-1234-5678")
    contacts = load_contacts()
    contact_id = contacts[0]["id"]
    delete_contact(contact_id)
    assert len(load_contacts()) == 0


def test_delete_nonexistent(capsys):
    delete_contact(999)
    captured = capsys.readouterr()
    assert "오류" in captured.out
