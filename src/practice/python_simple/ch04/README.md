## Chapter 04 – File IO, Modules, and Exception Handling

### Overview
This chapter introduces practical file handling and error handling patterns:
- Using objects to encapsulate file storage (read/write)
- Handling different file formats using standard library modules
- Writing robust code with `try/except` and custom exceptions

### Files
- `file_store.py`
  - Defines `Note` and `NoteStore`
  - Demonstrates storing structured data into a JSON file via an object

- `file_formats.py`
  - Demonstrates common format handling:
    - text (`Path.read_text` / `write_text`)
    - JSON (`json`)
    - CSV (`csv`)

- `exceptions_demo.py`
  - Demonstrates:
    - catching common exceptions (FileNotFoundError / JSONDecodeError / ValueError)
    - raising a custom exception (`DataFormatError`)
    - using `raise ... from e` to preserve the original traceback

### How to Run
From the repository root:

```bash
python src/practice/python_simple/ch04/file_store.py
python src/practice/python_simple/ch04/file_formats.py
python src/practice/python_simple/ch04/exceptions_demo.py