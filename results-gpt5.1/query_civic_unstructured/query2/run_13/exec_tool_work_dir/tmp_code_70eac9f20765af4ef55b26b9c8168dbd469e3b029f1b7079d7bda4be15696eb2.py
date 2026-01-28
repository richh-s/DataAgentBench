code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_EZnFkfXrvSwcsUTh5Fl9z4iQ
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = ' '.join(d['text'] for d in docs)

# Heuristic: extract project lines mentioning 'Park' and completion in 2022
projects_2022 = set()
for line in texts.split('\n'):
    if 'Park' in line or 'park' in line:
        # look ahead for completion info in nearby text
        pass
# Simpler: manually search for '2022' and 'completed' and 'Park'
for m in re.finditer(r"([A-Z][A-Za-z0-9 &()'/.-]*Park[ A-Za-z0-9&()'/.-]*)(?:\n|.){0,3}?Construction was completed,? (November|December|October|September|August|July|June|May|April|March|February|January) 2022", texts):
    name = m.group(1).strip()
    projects_2022.add(name)

# Also capture forms like 'completed 2022'
for m in re.finditer(r"([A-Z][A-Za-z0-9 &()'/.-]*Park[ A-Za-z0-9&()'/.-]*)(?:\n|.){0,3}?(?:Construction )?was completed in 2022", texts):
    projects_2022.add(m.group(1).strip())

# From preview we already saw 'Bluffs Park Shade Structure' completed November 2022
projects_2022.add('Bluffs Park Shade Structure')

funding = pd.DataFrame(var_call_Vdaf5AocBsUA9lWwVEELnOYh)
funding['Amount'] = funding['Amount'].astype(int)

mask = funding['Project_Name'].isin(projects_2022)

total = int(funding.loc[mask, 'Amount'].sum())

result = {"projects_2022_park": sorted(projects_2022), "total_funding": total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EZnFkfXrvSwcsUTh5Fl9z4iQ': 'file_storage/call_EZnFkfXrvSwcsUTh5Fl9z4iQ.json', 'var_call_Vdaf5AocBsUA9lWwVEELnOYh': 'file_storage/call_Vdaf5AocBsUA9lWwVEELnOYh.json'}

exec(code, env_args)
