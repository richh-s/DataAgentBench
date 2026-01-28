code = """import json, re
from pathlib import Path

path = Path(var_call_vwNCMyZd6RCd2x0nP85Z01Xo)
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

projects = {}
for line in texts.split('\n'):
    line = line.strip()
    if not line:
        continue
    if 'Project' in line or '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
        if '2022' in line:
            projects[line] = True

path2 = Path(var_call_wpJLH0Lcq31Qvok3AECwbmsk)
with open(path2, 'r') as f:
    funding = json.load(f)

keywords = ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER']

def is_disaster(name: str) -> bool:
    up = name.upper()
    return any(k in up for k in keywords)

funding_2022_disaster = 0
for row in funding:
    name = row['Project_Name']
    if not is_disaster(name):
        continue
    if '2022' not in name and not any(name in p or p in name for p in projects):
        continue
    try:
        amt = int(row['Amount'])
    except Exception:
        try:
            amt = int(float(row['Amount']))
        except Exception:
            amt = 0
    funding_2022_disaster += amt

result = funding_2022_disaster

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vwNCMyZd6RCd2x0nP85Z01Xo': 'file_storage/call_vwNCMyZd6RCd2x0nP85Z01Xo.json', 'var_call_wpJLH0Lcq31Qvok3AECwbmsk': 'file_storage/call_wpJLH0Lcq31Qvok3AECwbmsk.json'}

exec(code, env_args)
