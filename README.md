# example_dep_repo

Minimal dependency examples for graphing and parsing.

Python:
- `pyproject.toml`
- `uv.lock`
- `main.py`

`main.py` includes tiny examples for `polars` and `pydantic`.

JavaScript:
- `package.json`
- `package-lock.json`
- `index.js`

The JavaScript example intentionally produces two versions of `ansi-styles`
in the dependency tree:
- root dependency: `ansi-styles@6.2.3`
- transitive via `chalk@4.1.2`: `ansi-styles@4.3.0`
