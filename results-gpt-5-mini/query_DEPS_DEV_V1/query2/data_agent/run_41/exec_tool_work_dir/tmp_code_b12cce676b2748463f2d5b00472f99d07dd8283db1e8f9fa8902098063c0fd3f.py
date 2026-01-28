code = """import json
from pathlib import Path
p = Path(var_call_Iqly7QLfJkb6B2iGc5R4PejT)
data = json.loads(p.read_text())
names = sorted({r['Name'] for r in data if r.get('System')=='NPM'})
# limit safety: take unique names only
result = json.dumps(names)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Iqly7QLfJkb6B2iGc5R4PejT': 'file_storage/call_Iqly7QLfJkb6B2iGc5R4PejT.json'}

exec(code, env_args)
