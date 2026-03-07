from pathlib import Path
import json


class DataFormatError(Exception):
    """Raised when input data format is invalid."""


def safe_read_json(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
        return json.loads(text)
    except FileNotFoundError as e:
        raise DataFormatError(f"File not found: {path}") from e
    except json.JSONDecodeError as e:
        raise DataFormatError(f"Invalid JSON in file: {path}") from e


def parse_int(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:
        raise DataFormatError(f"Not an integer: {s!r}") from e


def main():
    data_dir = Path(__file__).resolve().parent / "data"
    good = data_dir / "good.json"
    bad = data_dir / "bad.json"

    data_dir.mkdir(parents=True, exist_ok=True)
    good.write_text('{"ok": true, "n": 123}', encoding="utf-8")
    bad.write_text("{not-json}", encoding="utf-8")

    # 1) Good case
    print("good:", safe_read_json(good))

    # 2) Bad case (will raise DataFormatError)
    try:
        safe_read_json(bad)
    except DataFormatError as e:
        print("caught:", e)

    # 3) parse int demo
    try:
        print(parse_int("42"))
        print(parse_int("3.14"))
    except DataFormatError as e:
        print("caught:", e)


if __name__ == "__main__":
    main()