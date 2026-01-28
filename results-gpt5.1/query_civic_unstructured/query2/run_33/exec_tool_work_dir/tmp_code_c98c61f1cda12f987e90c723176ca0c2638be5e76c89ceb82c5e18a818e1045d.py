code = """import re, json, os
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_cYtPBoPJEqBtaBuqOXa54KJM)
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
path_fund = Path(var_call_173Zhogfsr6Mwl0PHnOH0sVp)
with open(path_fund, 'r') as f:
    funding = json.load(f)

text_all = '\n'.join(d.get('text','') for d in civic_docs)

park_completed_2022 = set()

# from preview we clearly see: "Bluffs Park Shade Structure" with Construction completed November 2022
if 'Bluffs Park Shade Structure' in text_all and 'completed November 2022' in text_all:
    park_completed_2022.add('Bluffs Park Shade Structure')

# Also check for other "Park" project lines mentioning completed and 2022
pattern = re.compile(r'([A-Z][A-Za-z0-9\s&]+Park[^
]*?completed[^\n]*?2022)', re.IGNORECASE)
for m in pattern.finditer(text_all):
    snippet = m.group(1)
    nm = re.match(r'([A-Z][A-Za-z0-9\s&]+Park(?: [A-Z][A-Za-z0-9]+)*)', snippet)
    if nm:
        park_completed_2022.add(nm.group(1).strip())

name_set_lower = {n.lower() for n in park_completed_2022}

total = 0
matched_projects = []
for row in funding:
    pname = row.get('Project_Name','')
    if pname.lower() in name_set_lower:
        try:
            amt = int(row.get('Amount',0))
        except Exception:
            amt = 0
        total += amt
        matched_projects.append({'Project_Name': pname, 'Amount': amt})

res = {'total_funding_park_completed_2022': total, 'matched_projects': matched_projects, 'identified_projects_from_docs': sorted(park_completed_2022)}

s = json.dumps(res)
print('__RESULT__:')
print(s)"""

env_args = {'var_call_cYtPBoPJEqBtaBuqOXa54KJM': 'file_storage/call_cYtPBoPJEqBtaBuqOXa54KJM.json', 'var_call_173Zhogfsr6Mwl0PHnOH0sVp': 'file_storage/call_173Zhogfsr6Mwl0PHnOH0sVp.json'}

exec(code, env_args)
