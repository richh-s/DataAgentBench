code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_zkAeM3CUMUGUguAhPlhujnaQ
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
full_text = '\n'.join(texts)

# Heuristic: find project blocks with 'Park' in name and completion dates in 2022
projects = []
for line in full_text.split('\n'):
    line_stripped = line.strip()
    if not line_stripped:
        continue
    # consider lines that look like project titles containing 'Park'
    if 'Park' in line_stripped and len(line_stripped.split()) < 10:
        projects.append(line_stripped)

# Also search for explicit known park projects from preview
candidate_names = set(projects)
extra = [
    'Bluffs Park Shade Structure',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Trancas Canyon Park Playground',
    'Malibu Bluffs Park South Walkway',
    'Malibu Bluffs Park South Walkway Repairs',
    'Legacy Park Benches and Arbors Renovation',
    'Legacy Park Paver Repair Project',
]
for e in extra:
    if e in full_text:
        candidate_names.add(e)

# Determine which of these have completion/end dates in 2022 in surrounding text
completed_2022 = set()
for name in candidate_names:
    # find occurrences
    for m in re.finditer(re.escape(name), full_text):
        start = max(0, m.start()-500)
        end = m.end()+500
        ctx = full_text[start:end]
        # look for 'Construction was completed' or 'completed' with 2022 nearby
        if re.search(r'completed[^\n]*2022', ctx, re.IGNORECASE):
            completed_2022.add(name)
            break

# Load funding table
funding = var_call_DKfdbWO6gXhE9fyoZnVAAN41
with open(funding, 'r') as f:
    funding_records = json.load(f)

# Sum funding amounts for matching project names
names_lower = {n.lower() for n in completed_2022}

total = 0
for rec in funding_records:
    pname = rec['Project_Name']
    if pname.lower() in names_lower:
        total += int(rec['Amount'])

result = {"completed_2022_park_projects": sorted(list(completed_2022)), "total_funding": total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zkAeM3CUMUGUguAhPlhujnaQ': 'file_storage/call_zkAeM3CUMUGUguAhPlhujnaQ.json', 'var_call_DKfdbWO6gXhE9fyoZnVAAN41': 'file_storage/call_DKfdbWO6gXhE9fyoZnVAAN41.json'}

exec(code, env_args)
