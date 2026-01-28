code = """import json
from pathlib import Path
p = Path(var_call_faxdiIQt980BBkyMR5n1KUWN)
data = json.loads(p.read_text())
# Extract unique (Name, Version)
pairs = []
seen = set()
for r in data:
    name = r.get('Name')
    version = r.get('Version')
    key = (name, version)
    if key not in seen:
        seen.add(key)
        pairs.append({'Name': name, 'Version': version})

import json
print("__RESULT__:")
print(json.dumps(pairs))"""

env_args = {'var_call_5AMYD8MyDFKO01JvVzZWn3eS': ['packageinfo'], 'var_call_BaSR9ijbE3x4QXyQoGOzRPFT': ['project_info', 'project_packageversion'], 'var_call_faxdiIQt980BBkyMR5n1KUWN': 'file_storage/call_faxdiIQt980BBkyMR5n1KUWN.json'}

exec(code, env_args)
