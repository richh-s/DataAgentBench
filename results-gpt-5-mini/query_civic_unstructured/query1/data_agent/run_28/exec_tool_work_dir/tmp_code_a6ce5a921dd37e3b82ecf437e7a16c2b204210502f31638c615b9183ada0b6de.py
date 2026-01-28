code = """import json
import re

# Load tool results from storage file paths
with open(var_call_fRlJXidfU4kMf8AifkF5FRKq, 'r') as f:
    funding_records = json.load(f)
with open(var_call_tR8HMqH4CqiPqlurYgoNEblP, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding records and build a mapping of funding project names to amounts
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name', '').strip()
    try:
        amt = int(rec.get('Amount', 0))
    except:
        try:
            amt = int(float(rec.get('Amount', 0)))
        except:
            amt = 0
    if name:
        funding_map.setdefault(name, []).append(amt)

# Extract project names from 'Capital Improvement Projects (Design)' sections across documents
project_names = set()
pattern = re.compile(r'Capital Improvement Projects\s*\(Design\)(.*?)(?:Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Capital Improvement Projects\s*\(Construction\)|$)', re.S | re.I)
for doc in civic_docs:
    text = doc.get('text', '')
    m = pattern.search(text)
    if not m:
        continue
    section = m.group(1)
    lines = section.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Exclusion heuristics for non-title lines
        if line.startswith('(cid') or line.lower().startswith('updates') or line.lower().startswith('project schedule'):
            continue
        if line.lower().startswith('page') or line.lower().startswith('agenda'):
            continue
        if ':' in line:
            continue
        if any(kw in line for kw in ['Complete Design', 'Advertise', 'Begin Construction', 'Project is', 'Staff is', 'On ', 'City will', 'Project Schedule', 'Project Description', 'Project Updates']):
            continue
        if len(line) > 200:
            continue
        # Filter out lines that look like sentences (contain multiple clauses with periods)
        if '.' in line and len(line.split('.')) > 2:
            continue
        # Likely a project title
        project_names.add(line)

# Match extracted project names to funding records (consider exact and substring matches)
matched = {}
for pname in project_names:
    pname_l = pname.lower()
    for fname, amts in funding_map.items():
        fname_l = fname.lower()
        if pname_l == fname_l or pname_l in fname_l or fname_l in pname_l:
            # ensure at least one funding amount > 50000
            if any(a > 50000 for a in amts):
                matched[pname] = sorted(list(set(amts)), reverse=True)

# Prepare result
count = len(matched)
projects_list = []
for p, amts in matched.items():
    projects_list.append({'project_name': p, 'funding_amounts': amts})

result = {'count': count, 'projects': projects_list}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_iDBursbEDCmJaDQy90JslkBv': ['civic_docs'], 'var_call_nAtrXrjoNClMh4yMdoGelnBG': ['Funding'], 'var_call_fRlJXidfU4kMf8AifkF5FRKq': 'file_storage/call_fRlJXidfU4kMf8AifkF5FRKq.json', 'var_call_tR8HMqH4CqiPqlurYgoNEblP': 'file_storage/call_tR8HMqH4CqiPqlurYgoNEblP.json'}

exec(code, env_args)
