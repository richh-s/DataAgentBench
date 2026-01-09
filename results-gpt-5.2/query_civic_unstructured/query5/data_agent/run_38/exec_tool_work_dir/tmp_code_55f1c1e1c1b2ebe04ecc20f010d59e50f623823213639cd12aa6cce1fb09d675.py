code = """import json, re
import pandas as pd

docs_path = var_call_osN1aBustPtFa70A04jgfTvr
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Find disaster section project names in the large 03-22-23 doc previewed
sample = None
for d in docs:
    if d.get('filename') == 'malibucity_agenda_03222023-2060.txt':
        sample = d.get('text','')
        break

lines = [ln.strip() for ln in (sample or '').splitlines()]

# Locate disaster section portion
idx = None
for i, ln in enumerate(lines):
    if re.search(r'Disaster\s+Recovery\s+Projects', ln, re.IGNORECASE):
        idx = i
        break

# Collect 200 lines after
snippet = lines[idx:idx+250] if idx is not None else lines[:250]

print('__RESULT__:')
print(json.dumps({'found_disaster_section': idx is not None, 'idx': idx, 'snippet': snippet[:200]}))"""

env_args = {'var_call_Kg6NqBoEPX5FZHGCn6pWJjjb': 'file_storage/call_Kg6NqBoEPX5FZHGCn6pWJjjb.json', 'var_call_osN1aBustPtFa70A04jgfTvr': 'file_storage/call_osN1aBustPtFa70A04jgfTvr.json', 'var_call_lLOTO8ea6JafFE0pIrYI8W4l': ['Funding'], 'var_call_gyvcQy86SYjXRmLjEdCLvi9g': {'total_funding_disaster_projects_started_2022': 0, 'matched_projects_count': 0, 'matched_projects': []}}

exec(code, env_args)
