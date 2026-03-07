from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json
from datetime import datetime


@dataclass
class Note:
    title: str
    content: str
    created_at: str


class NoteStore:
    """
    Store notes into a JSON file. This is a tiny example of:
    - object encapsulating file IO
    - read/write JSON safely
    """
    def __init__(self, path: Path):
        self.path = path

    def load(self) -> list[Note]:
        if not self.path.exists():
            return []
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return [Note(**item) for item in data]

    def save(self, notes: list[Note]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = [asdict(n) for n in notes]
        self.path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def add(self, title: str, content: str) -> Note:
        notes = self.load()
        note = Note(
            title=title,
            content=content,
            created_at=datetime.now().isoformat(timespec="seconds"),
        )
        notes.append(note)
        self.save(notes)
        return note


def main():
    data_dir = Path(__file__).resolve().parent / "data"
    store = NoteStore(data_dir / "notes.json")

    note = store.add("ch04 note", "This note was saved by NoteStore.")
    print("Added:", note)

    all_notes = store.load()
    print(f"Total notes: {len(all_notes)}")
    print("Latest:", all_notes[-1])


if __name__ == "__main__":
    main()