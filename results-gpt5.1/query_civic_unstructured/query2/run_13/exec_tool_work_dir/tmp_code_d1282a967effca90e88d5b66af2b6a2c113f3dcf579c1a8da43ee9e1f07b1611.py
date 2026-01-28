code = """import re, json, pandas as pd

path_docs = var_call_EZnFkfXrvSwcsUTh5Fl9z4iQ
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = ' '.join(d['text'] for d in docs)

projects_2022 = set()

pattern1 = r'([A-Z][A-Za-z0-9 &()\'/.-]*Park[ A-Za-z0-9&()\'/.-]*)(?:\n|.){0,3}?Construction was completed,? (November|December|October|September|August|July|June|May|April|March|February|January) 2022'
pattern2 = r'([A-Z][A-Za-z0-9 &()\'/.-]*Park[ A-Za-z0-9&()\'/.-]*)(?:\n|.){0,3}?(?:Construction )?was completed in 2022'

for m in re.finditer(pattern1, texts):
    projects_2022.add(m.group(1).strip())
for m in re.finditer(pattern2, texts):
    projects_2022.add(m.group(1).strip())

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
