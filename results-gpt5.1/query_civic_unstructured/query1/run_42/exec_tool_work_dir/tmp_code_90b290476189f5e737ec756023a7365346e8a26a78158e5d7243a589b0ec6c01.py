code = """import re, json, pandas as pd

# Load funding data
funding_records = var_call_pFXere82HlneUPFR9Z0EZnD3
funding_df = pd.DataFrame(funding_records)

# Normalize amounts to int
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Load civic docs (may be a file path or list)
from pathlib import Path
civic_source = var_call_qTHMu8Sg1GnOSHHwciX5xuJ5
if isinstance(civic_source, str) and Path(civic_source).suffix == '.json':
    import json as _json
    with open(civic_source, 'r') as f:
        civic_docs = _json.load(f)
else:
    civic_docs = civic_source

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Heuristic extraction: treat each line that looks like a project name as a project entry, then infer type/status.
projects = []
for line in full_text.split('\n'):
    s = line.strip()
    if not s:
        continue
    # skip headers/common words
    if len(s) < 5:
        continue
    # Heuristic: project name lines often have no colon and no long sentences (few spaces)
    if ':' in s:
        continue
    # exclude generic agenda labels
    if any(w in s.lower() for w in ['agenda', 'item #', 'page ', 'meeting date', 'subject', 'recommended action', 'discussion:', 'updates:', 'project description']):
        continue
    # We'll accept lines that contain keywords like 'project', 'road', 'park', 'storm', 'drain', 'improvements', 'repairs', 'facility', 'playground', 'signals', 'study', 'warning', 'walkway', 'median'
    keywords = ['project', 'road', 'park', 'storm', 'drain', 'improvements', 'repairs', 'facility', 'playground', 'signals', 'study', 'warning', 'walkway', 'median', 'slope', 'treatment', 'roof', 'culvert', 'bridge']
    if not any(k.lower() in s.lower() for k in keywords):
        continue
    projects.append(s)

# Deduplicate
projects = sorted(set(projects))

# Infer status from nearby headings in the text using simple search
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
    # take following 2000 chars as that section
    segment = full_text[idx: idx+4000]
    lines = [l.strip() for l in segment.split('\n') if l.strip()]
    for l in lines:
        if any(k.lower() in l.lower() for k in ['project', 'road', 'park', 'storm', 'drain', 'improvements', 'repairs', 'facility', 'playground', 'signals', 'study', 'warning', 'walkway', 'median', 'slope']):
            # skip marker line itself
            if 'Capital Improvement Projects' in l:
                continue
            status_map[l] = status

# Now build project dataframe with inferred status and types
proj_rows = []
for p in projects:
    status = status_map.get(p)
    # infer type: any FEMA/CalOES/CalJPIA => disaster, else capital if appears under capital headings
    p_lower = p.lower()
    if any(tag in p_lower for tag in ['fema', 'caloes', 'caljpia']):
        p_type = 'disaster'
    else:
        p_type = 'capital'
    proj_rows.append({'Project_Name': p, 'status': status, 'type': p_type})

proj_df = pd.DataFrame(proj_rows)

# We only care about capital projects with design status
capital_design = proj_df[(proj_df['type'] == 'capital') & (proj_df['status'] == 'design')]

# Join with funding on Project_Name (exact match)
merged = pd.merge(capital_design, funding_df, on='Project_Name', how='inner')

# Filter funding > 50000 (already done in SQL, but be safe)
result_count = int((merged['Amount'] > 50000).sum())

import json as json_module
out = json_module.dumps(result_count)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_pFXere82HlneUPFR9Z0EZnD3': 'file_storage/call_pFXere82HlneUPFR9Z0EZnD3.json', 'var_call_qTHMu8Sg1GnOSHHwciX5xuJ5': 'file_storage/call_qTHMu8Sg1GnOSHHwciX5xuJ5.json'}

exec(code, env_args)
