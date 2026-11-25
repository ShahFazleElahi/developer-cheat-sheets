# Python

```python
from pathlib import Path
import json
records = [{"name": "Ada", "active": True}]
active = [r["name"] for r in records if r["active"]]
print(active)
Path("example.json").write_text(json.dumps(records), encoding="utf-8")
```

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip --version
python -m unittest discover -s tests
```
Use virtual environments, explicit encodings, and context managers for resources.

## Official reference

[Python documentation](https://docs.python.org/3/tutorial/)
