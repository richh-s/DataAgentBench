code = """import json, re
import pandas as pd

# Load funding project names > 50k
pn_src = var_call_bt5IyKTo3B5ZTAzV9d2si7XB
if isinstance(pn_src, str) and pn_src.endswith('.json'):
    with open(pn_src, 'r', encoding='utf-8') as f:
        pn_records = json.load(f)
else:
    pn_records = pn_src

project_names = [r['Project_Name'] for r in pn_records if r.get('Project_Name')]
# normalize
norm = lambda s: re.sub(r'\s+', ' ', s.strip()).lower()
name_map = {norm(n): n for n in project_names}

# Load civic docs
docs_src = var_call_zJNblZ68BW2mDtupKCIILMtG
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Find which funding project names appear in a 'Capital Improvement Projects (Design)' section
in_design = set()
for d in docs:
    text = d.get('text') or ''
    t = text.replace('\r','\n')
    m = re.search(r'Capital Improvement Projects\s*\(\s*Design\s*\)(.*?)(Capital Improvement Projects\s*\(|Disaster Recovery Projects\s*\(|$)', t, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        continue
    section = m.group(1)
    sec_norm = norm(section)
    for n in project_names:
        nn = norm(n)
        # exact phrase match in section
        if nn and nn in sec_norm:
            in_design.add(name_map.get(nn, n))

result = {"count": int(len(in_design)), "projects": sorted(in_design)[:50]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EuqteiITslIgV4uqQZX79Q3l': [{'cnt': '276'}], 'var_call_zJNblZ68BW2mDtupKCIILMtG': 'file_storage/call_zJNblZ68BW2mDtupKCIILMtG.json', 'var_call_bt5IyKTo3B5ZTAzV9d2si7XB': 'file_storage/call_bt5IyKTo3B5ZTAzV9d2si7XB.json'}

exec(code, env_args)
