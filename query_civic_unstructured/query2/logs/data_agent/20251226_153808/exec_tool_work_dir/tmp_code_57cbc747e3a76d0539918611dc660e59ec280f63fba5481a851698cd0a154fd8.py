code = """import json
# Load files
with open(var_call_ZGxPsl3QZckLx5Aftdn8Sa0X, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_vzEtHYEO2mxMyHPnsAC47tFQ, 'r') as f:
    funding_records = json.load(f)

# Build funding map
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name')
    amt = rec.get('Amount')
    if not name:
        continue
    try:
        val = int(amt)
    except Exception:
        try:
            val = int(float(amt))
        except Exception:
            val = 0
    funding_map[name] = funding_map.get(name, 0) + val

# Helper: find title above a line index

def find_title(lines, idx):
    for j in range(idx - 1, max(-1, idx - 11), -1):
        line = lines[j].strip()
        if not line:
            continue
        low = line.lower()
        if low.startswith('updates') or low.startswith('project schedule') or low.startswith('estimated schedule') or low.startswith('project description'):
            continue
        if ':' in line:
            continue
        if 'capital improvement projects' in low or 'disaster recovery projects' in low:
            continue
        if 'agenda item' in low or 'page ' in low:
            continue
        if len(line) > 120:
            continue
        return line
    return None

# Scan documents for lines indicating completed in 2022 and park-related titles
park_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        low = line.lower()
        if ('completed' in low) and ('2022' in line):
            title = find_title(lines, i)
            if not title:
                continue
            tlow = title.lower()
            if ('park' in tlow) or ('playground' in tlow):
                park_projects.add(title)

# Match park projects to funding names
matched_funding = set()
for proj in park_projects:
    p = proj.lower()
    for fname in funding_map.keys():
        f = fname.lower()
        if p == f or p in f or f in p:
            matched_funding.add(fname)

# Sum total funding for matched names
total_funding = sum(funding_map[name] for name in matched_funding)

result = {
    'park_completed_2022_projects': sorted(list(park_projects)),
    'matched_funding_records': sorted(list(matched_funding)),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ZGxPsl3QZckLx5Aftdn8Sa0X': 'file_storage/call_ZGxPsl3QZckLx5Aftdn8Sa0X.json', 'var_call_vzEtHYEO2mxMyHPnsAC47tFQ': 'file_storage/call_vzEtHYEO2mxMyHPnsAC47tFQ.json', 'var_call_vPZiNK1ZwTOX2UZ4GF6PIA6T': {'num_docs': 5, 'num_funding': 500}}

exec(code, env_args)
