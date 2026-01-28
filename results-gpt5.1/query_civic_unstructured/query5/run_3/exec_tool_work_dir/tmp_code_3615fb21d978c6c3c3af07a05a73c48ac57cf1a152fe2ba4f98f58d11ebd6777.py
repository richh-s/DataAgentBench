code = """import re, json
from pathlib import Path

# Load full civic docs result
path = Path(var_call_vwNCMyZd6RCd2x0nP85Z01Xo)
import json as _json
with open(path, 'r') as f:
    civic_docs = _json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

# Very rough heuristic: capture lines that look like project titles followed by (FEMA/CalOES etc) and dates
projects = {}
for line in texts.split('\n'):
    line = line.strip()
    if not line:
        continue
    # Treat any line ending with 'Project' or containing '(FEMA' etc as a project name
    if 'Project' in line or '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
        name = line
        # look ahead for date info containing 2022 within 3 subsequent lines
        # (simplified: just check same line for 2022)
        if '2022' in line:
            projects[name] = True

# We don't have explicit structured st/et; instead approximate: any project mentioned with '2022' in title is 2022-started

# Load funding table (already previewed, but here assume var_call_wpJLH0Lcq31Qvok3AECwbmsk is a path)
path2 = Path(var_call_wpJLH0Lcq31Qvok3AECwbmsk)
with open(path2, 'r') as f:
    funding = _json.load(f)

# Disaster-related projects: names containing FEMA, CalOES, CalJPIA, or the word 'Disaster'

disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster']

def is_disaster(name):
    up = name.upper()
    return any(k in up for k in disaster_keywords)

# Projects started in 2022: from civic docs heuristic: project name contains '2022'

funding_2022_disaster = 0
for row in funding:
    name = row['Project_Name']
    if not is_disaster(name):
        continue
    if '2022' not in name:
        # also allow if our civic-derived project list says it's 2022-started (by exact match or substring)
        if not any(name in p or p in name for p in projects):
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
