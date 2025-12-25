code = """import json, pandas as pd, re
from pathlib import Path

# Load full result from file
path = Path(var_call_iF1qIj6vf1p2PTLgvZ0dtWk1)
with open(path, 'r') as f:
    data = json.load(f)

# Extract publication numbers (assignee UNIV CALIFORNIA)
uc_pubs = []
for rec in data:
    txt = rec.get('Patents_info','')
    m = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', txt)
    if m:
        uc_pubs.append(m.group(1))

uc_pubs = sorted(set(uc_pubs))

result = json.dumps(uc_pubs)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_EzMxUAYF0MisoIx0hDfWhVXV': [], 'var_call_iF1qIj6vf1p2PTLgvZ0dtWk1': 'file_storage/call_iF1qIj6vf1p2PTLgvZ0dtWk1.json'}

exec(code, env_args)
