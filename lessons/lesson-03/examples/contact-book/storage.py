"""
JSON 파일 기반 연락처 데이터 저장·불러오기
"""

import json
import os
from typing import Any

DATA_FILE = "contacts.json"


def load_contacts() -> list[dict[str, Any]]:
    """저장된 연락처 목록을 불러온다. 파일이 없으면 빈 목록을 반환한다."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_contacts(contacts: list[dict[str, Any]]) -> None:
    """연락처 목록을 파일에 저장한다."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
