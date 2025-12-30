code = """import re, json
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_cYtPBoPJEqBtaBuqOXa54KJM)
import json as _json
with open(path_docs, 'r') as f:
    civic_docs = _json.load(f)

# Load funding table
path_fund = Path(var_call_173Zhogfsr6Mwl0PHnOH0sVp)
with open(path_fund, 'r') as f:
    funding = _json.load(f)

# Extract projects with 'park' topic & completed in 2022 from civic docs
park_completed_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Simple heuristic: split lines, look for lines with 'Park' and 'Completed' and '2022'
    for line in text.split('\n'):
        if 'park' in line.lower():
            # Look ahead a few lines for completion info
            # This is very heuristic given unstructured text
            pass

# Instead, we'll search globally for patterns like 'Park' and 'Construction was completed, 2022'
text_all = '\n'.join(d.get('text','') for d in civic_docs)

# Find sentences mentioning 'Park' and 'completed' and '2022'
for m in re.finditer(r'([A-Z][A-Za-z0-9\s&]+Park[^
]*?completed[^\n]*?2022)', text_all, flags=re.IGNORECASE):
    snippet = m.group(1)
    # Project name: take leading capitalized words ending with 'Park' plus optional trailing words
    name_match = re.match(r'([A-Z][A-Za-z0-9\s&]+Park(?: [A-Z][A-Za-z0-9]+)*)', snippet)
    if name_match:
        park_completed_2022.add(name_match.group(1).strip())

# Also handle known specific patterns from preview like 'Bluffs Park Shade Structure'
if 'Bluffs Park Shade Structure' in text_all and 'Construction was completed November 2022' in text_all:
    park_completed_2022.add('Bluffs Park Shade Structure')

# Now sum funding amounts for matching project names (exact match)
name_set_lower = {n.lower() for n in park_completed_2022}

total = 0
matched_projects = []
for row in funding:
    pname = row.get('Project_Name','')
    if pname.lower() in name_set_lower:
        try:
            amt = int(row.get('Amount',0))
        except ValueError:
            amt = 0
        total += amt
        matched_projects.append({'Project_Name': pname, 'Amount': amt})

result = {'total_funding_park_completed_2022': total, 'matched_projects': matched_projects, 'identified_projects_from_docs': sorted(park_completed_2022)}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_cYtPBoPJEqBtaBuqOXa54KJM': 'file_storage/call_cYtPBoPJEqBtaBuqOXa54KJM.json', 'var_call_173Zhogfsr6Mwl0PHnOH0sVp': 'file_storage/call_173Zhogfsr6Mwl0PHnOH0sVp.json'}

exec(code, env_args)
