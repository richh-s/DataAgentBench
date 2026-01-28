code = """import json, pandas as pd, re
from pathlib import Path

funding_records = var_call_pFXere82HlneUPFR9Z0EZnD3
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

civic_source = var_call_qTHMu8Sg1GnOSHHwciX5xuJ5
if isinstance(civic_source, str) and Path(civic_source).suffix == '.json':
    with open(civic_source, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_source

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

projects = []
for line in full_text.split('\n'):
    s = line.strip()
    if not s:
        continue
    if len(s) < 5:
        continue
    if ':' in s:
        continue
    lowered = s.lower()
    if any(w in lowered for w in ['agenda', 'item #', 'page ', 'meeting date', 'subject', 'recommended action', 'discussion:', 'updates:', 'project description']):
        continue
    keywords = ['project', 'road', 'park', 'storm', 'drain', 'improvements', 'repairs', 'facility', 'playground', 'signals', 'study', 'warning', 'walkway', 'median', 'slope', 'treatment', 'roof', 'culvert', 'bridge']
    if not any(k in lowered for k in keywords):
        continue
    projects.append(s)

projects = sorted(set(projects))

status_map = {}
status_sections = [
    ('design', 'Capital Improvement Projects (Design)'),
    ('completed', 'Capital Improvement Projects (Construction)'),
    ('not started', 'Capital Improvement Projects (Not Started)')
]

for status, marker in status_sections:
    idx = full_text.find(marker)
    if idx == -1:
        continue
    segment = full_text[idx: idx+4000]
    lines = [l.strip() for l in segment.split('\n') if l.strip()]
    for l in lines:
        low = l.lower()
        if any(k in low for k in ['project', 'road', 'park', 'storm', 'drain', 'improvements', 'repairs', 'facility', 'playground', 'signals', 'study', 'warning', 'walkway', 'median', 'slope']):
            if 'capital improvement projects' in low:
                continue
            status_map[l] = status

proj_rows = []
for p in projects:
    p_lower = p.lower()
    if any(tag in p_lower for tag in ['fema', 'caloes', 'caljpia']):
        p_type = 'disaster'
    else:
        p_type = 'capital'
    status = status_map.get(p)
    proj_rows.append({'Project_Name': p, 'status': status, 'type': p_type})

proj_df = pd.DataFrame(proj_rows)

capital_design = proj_df[(proj_df['type'] == 'capital') & (proj_df['status'] == 'design')]
merged = pd.merge(capital_design, funding_df, on='Project_Name', how='inner')

result_count = int((merged['Amount'] > 50000).sum())

out = json.dumps(result_count)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_pFXere82HlneUPFR9Z0EZnD3': 'file_storage/call_pFXere82HlneUPFR9Z0EZnD3.json', 'var_call_qTHMu8Sg1GnOSHHwciX5xuJ5': 'file_storage/call_qTHMu8Sg1GnOSHHwciX5xuJ5.json'}

exec(code, env_args)
