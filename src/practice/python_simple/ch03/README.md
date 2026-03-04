## Chapter 03 – Control Flow, Functions, and Standard Library

### Overview
This chapter focuses on core programming building blocks in Python:
- Conditional branching (`if / elif / else`)
- Repetition (`for` and `while`)
- Packaging logic into reusable functions
- Using common modules from the Python standard library

### Files
- `if_rules.py`  
  Demonstrates `if / elif / else` with common boundary cases (e.g., grade rules, discount rules).

- `loops.py`  
  Shows `for` loops, `while` loops, and how to avoid infinite loops (includes a simple safety guard).  
  Also includes `break` and `continue` examples.

- `functions.py`  
  Wraps logic into functions with clear inputs/outputs, basic validation, and reusable helpers.

- `stdlib_demo.py`  
  Practical standard library examples:
  - `datetime` for timestamps
  - `pathlib` for file paths
  - `json` for structured data output

### Key Takeaways
- Condition order matters (especially around boundaries).
- A `while` loop must always move toward its stopping condition; use safeguards when needed.
- Functions should have a single responsibility and validate inputs.
- The standard library is powerful—prefer it before installing external packages.

### How to Run
From the repository root:

```bash
python src/practice/python_simple/ch03/if_rules.py
python src/practice/python_simple/ch03/loops.py
python src/practice/python_simple/ch03/functions.py
python src/practice/python_simple/ch03/stdlib_demo.py