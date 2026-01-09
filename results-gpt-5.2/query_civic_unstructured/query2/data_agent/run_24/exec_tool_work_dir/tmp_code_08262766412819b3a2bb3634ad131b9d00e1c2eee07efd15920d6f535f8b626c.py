code = """import json, re
from pathlib import Path

p=Path(var_call_990QjnLpYNipFGlrpvba9P6S)
docs=json.loads(p.read_text())

hits=[]
for d in docs:
    for ln in d.get('text','').splitlines():
        if ('completed' in ln.lower()) and ('2022' in ln):
            hits.append({'filename': d.get('filename'), 'line': ln.strip()})

print('__RESULT__:')
print(json.dumps(hits[:100], ensure_ascii=False))"""

env_args = {'var_call_bj6z98fjH5u3abeSfc8CTfv8': ['Funding'], 'var_call_XhroUxAsfCyHp0eY88ACVcNh': ['civic_docs'], 'var_call_990QjnLpYNipFGlrpvba9P6S': 'file_storage/call_990QjnLpYNipFGlrpvba9P6S.json', 'var_call_J1ylmyIUyXF6iOhWBk1dyPNp': {'park_completed_2022': [], 'all_completed_2022': []}, 'var_call_UvwfRpanUXVlxQ3fZAtVWHQg': []}

exec(code, env_args)
