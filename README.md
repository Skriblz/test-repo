# textstats

Tiny sandbox repo for testing the Multica Code Engineer ↔ Code Reviewer loop.

## Dev setup
```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
pytest
ruff check .
```
