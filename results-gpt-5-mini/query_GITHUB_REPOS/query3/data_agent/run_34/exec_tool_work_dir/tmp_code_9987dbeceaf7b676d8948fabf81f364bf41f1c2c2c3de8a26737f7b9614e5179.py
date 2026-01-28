code = """import json
from pathlib import Path
# var_call_1sX8tQU6i238bWeSZ48JyTi2 is provided by previous query_db and contains the file path
p = Path(var_call_1sX8tQU6i238bWeSZ48JyTi2)
records = json.loads(p.read_text())
repo_names = sorted({r['repo_name'] for r in records if 'repo_name' in r})
# Output as JSON array string
out = json.dumps(repo_names)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1sX8tQU6i238bWeSZ48JyTi2': 'file_storage/call_1sX8tQU6i238bWeSZ48JyTi2.json'}

exec(code, env_args)
