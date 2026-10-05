# Eben Taljaard
import json
from pathlib import Path

DB_FILE = Path("iap_state.json")


DEFAULT_STATE = {
    "orders": {},
    "inventory": {},
}


def load_state():
    if not DB_FILE.exists():
        return DEFAULT_STATE.copy()

    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(
            state,
            f,
            indent=2
        )
