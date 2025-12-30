code = """import json, re
from collections import defaultdict

# Load funding records (> 50000)
funding_records = var_call_Zt23CqLTy7mMoHl9YsBn40Uf

# Load civic docs (may be file path or list)
import os
if isinstance(var_call_4uceinGyYaO22kHnN5TGdn3p, str) and os.path.isfile(var_call_4uceinGyYaO22kHnN5TGdn3p):
    with open(var_call_4uceinGyYaO22kHnN5TGdn3p, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_call_4uceinGyYaO22kHnN5TGdn3p

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Very simple heuristic parser: find project names under "Capital Improvement Projects (Design)" section
# and treat them as capital projects with status 'design'.

sections = re.split(r"Capital Improvement Projects \(Design\)", full_text, flags=re.IGNORECASE)
capital_design_projects = set()
if len(sections) > 1:
    design_block = sections[1]
    # stop at next major heading
    design_block = re.split(r"Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)", design_block, flags=re.IGNORECASE)[0]
    # project names typically appear as standalone lines between blank lines
    for line in design_block.split('\n'):
        line = line.strip()
        if not line:
            continue
        # skip non-title lines
        if len(line.split()) < 2:
            continue
        if any(kw in line.lower() for kw in ['updates', 'project schedule', 'estimated schedule', 'cid:']):
            continue
        # crude filter: title case-ish and not a sentence ending with period
        if line.endswith('.'):
            continue
        # store as project name
        capital_design_projects.add(line)

# Now join with funding records (>50000)
project_name_to_amount = {r['Project_Name']: int(r['Amount']) for r in funding_records}

count = 0
matched_projects = []
for pname in capital_design_projects:
    if pname in project_name_to_amount and project_name_to_amount[pname] > 50000:
        count += 1
        matched_projects.append({'Project_Name': pname, 'Amount': project_name_to_amount[pname]})

result = {'count': count, 'matched_projects': matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Zt23CqLTy7mMoHl9YsBn40Uf': 'file_storage/call_Zt23CqLTy7mMoHl9YsBn40Uf.json', 'var_call_4uceinGyYaO22kHnN5TGdn3p': 'file_storage/call_4uceinGyYaO22kHnN5TGdn3p.json'}

exec(code, env_args)
