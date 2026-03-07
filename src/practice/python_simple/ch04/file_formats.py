from pathlib import Path
import json
import csv


def demo_text(path: Path) -> None:
    path.write_text("hello\nworld\n", encoding="utf-8")
    content = path.read_text(encoding="utf-8")
    print("[text]\n", content)


def demo_json(path: Path) -> None:
    data = {"app": "aios-cli", "chapter": 4, "items": [1, 2, 3]}
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    loaded = json.loads(path.read_text(encoding="utf-8"))
    print("[json]", loaded)


def demo_csv(path: Path) -> None:
    rows = [
        {"name": "Alice", "age": 28},
        {"name": "Bob", "age": 31},
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(rows)

    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        loaded = list(reader)
    print("[csv]", loaded)


def main():
    data_dir = Path(__file__).resolve().parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    demo_text(data_dir / "sample.txt")
    demo_json(data_dir / "sample.json")
    demo_csv(data_dir / "sample.csv")


if __name__ == "__main__":
    main()