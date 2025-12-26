code = """import json, re

# Load civic docs
import builtins
with open(var_call_ZGxPsl3QZckLx5Aftdn8Sa0X, 'r') as f:
    civic_docs = json.load(f)

# Load funding
with open(var_call_vzEtHYEO2mxMyHPnsAC47tFQ, 'r') as f:
    funding_records = json.load(f)

# Build funding dict map from project name to amount (sum if multiple entries for same name)
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name')
    amt = rec.get('Amount')
    try:
        val = int(amt)
    except Exception:
        try:
            val = int(float(amt))
        except Exception:
            val = 0
    if name is None:
        continue
    funding_map[name] = funding_map.get(name, 0) + val

# Helper to find a plausible project title line above a given index

def find_project_title(lines, idx):
    for j in range(idx-1, max(-1, idx-11), -1):
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

park_related_projects_2022 = set()
pattern_completed = re.compile(r'\bcompleted\b', re.IGNORECASE)
pattern_2022 = re.compile(r'2022')

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if pattern_completed.search(line) and pattern_2022.search(line):
            title = find_project_title(lines, i)
            if not title:
                continue
            tl = title.lower()
            if ('park' in tl) or ('playground' in tl):
                park_related_projects_2022.add(title)

# Sum funding for these projects
total_funding = 0
missing = []
for proj in sorted(park_related_projects_2022):
    if proj in funding_map:
        total_funding += funding_map[proj]
    else:
        # try case-insensitive exact and startswith matches
        matches = [name for name in funding_map if name.lower() == proj.lower() or name.lower().startswith(proj.lower())]
        if matches:
            total_funding += sum(funding_map[m] for m in matches)
        else:
            missing.append(proj)

result = {
    'park_completed_2022_projects': sorted(list(park_related_projects_2022)),
    'total_funding': total_funding,
    'missing_in_funding': missing
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZGxPsl3QZckLx5Aftdn8Sa0X': 'file_storage/call_ZGxPsl3QZckLx5Aftdn8Sa0X.json', 'var_call_vzEtHYEO2mxMyHPnsAC47tFQ': 'file_storage/call_vzEtHYEO2mxMyHPnsAC47tFQ.json'}

exec(code, env_args)
