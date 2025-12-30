code = """import re, json, pandas as pd, pathlib, json as jsonmod

path = pathlib.Path(var_call_kZa27tpLrDXOn8yd0JQQFkMI)
with path.open() as f:
    civic_docs = jsonmod.load(f)

funding = pd.DataFrame(var_call_2lmvN1TvM82PM1nxwsf4lPus)

text = " ".join(doc.get('text','') for doc in civic_docs)

projects = []
for line in text.split('\n'):
    line = line.strip()
    if not line:
        continue
    if ('Project' in line) or ('Repairs' in line) or ('Improvements' in line) or ('Recovery' in line):
        if '2022' in line:
            projects.append(line)

funding['is_disaster'] = funding['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Disaster', case=False, regex=True)
funding['is_2022'] = funding['Project_Name'].str.contains('2022', case=False, regex=False)

subset = funding[funding['is_disaster'] & funding['is_2022']].copy()
subset['Amount'] = subset['Amount'].astype(int)

total = int(subset['Amount'].sum())

result = {'total_disaster_2022_funding': total, 'matching_projects': subset[['Project_Name','Amount']].to_dict(orient='records')}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_kZa27tpLrDXOn8yd0JQQFkMI': 'file_storage/call_kZa27tpLrDXOn8yd0JQQFkMI.json', 'var_call_2lmvN1TvM82PM1nxwsf4lPus': 'file_storage/call_2lmvN1TvM82PM1nxwsf4lPus.json'}

exec(code, env_args)
