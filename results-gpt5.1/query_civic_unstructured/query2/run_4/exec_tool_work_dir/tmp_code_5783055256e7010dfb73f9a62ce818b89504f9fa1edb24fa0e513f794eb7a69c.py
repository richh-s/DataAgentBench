code = """import re, json, pandas as pd

path_docs = var_call_x6rRfRBkKNEdQQdD9GKWMOxT
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

projects_2022_completed = []
for line in full_text.split('\n'):
    if 'Construction was completed' in line or 'construction was completed' in line:
        if '2022' in line:
            projects_2022_completed.append(line.strip())

project_names = []
lines = full_text.split('\n')
for i, line in enumerate(lines):
    if ('Construction was completed' in line or 'construction was completed' in line) and '2022' in line:
        for j in range(i-3, i):
            if j >= 0:
                cand = lines[j].strip()
                if cand and not cand.lower().startswith('(cid') and 'Updates' not in cand and 'Page' not in cand and 'Agenda Item' not in cand:
                    project_names.append(cand)
                    break

project_names = list(dict.fromkeys(project_names))

park_keywords = ['park']
park_projects_2022_completed = [p for p in project_names if any(k.lower() in p.lower() for k in park_keywords)]

path_funding = var_call_cTisuIrsl5YwQu4ozQuGUWZs
with open(path_funding, 'r') as f:
    funding_records = json.load(f)

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

matched = fund_df[fund_df['Project_Name'].isin(park_projects_2022_completed)]

total_funding = int(matched['Amount'].sum())

result = {
    'park_projects_2022_completed': park_projects_2022_completed,
    'matched_funding_records': matched.to_dict(orient='records'),
    'total_funding': total_funding
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_x6rRfRBkKNEdQQdD9GKWMOxT': 'file_storage/call_x6rRfRBkKNEdQQdD9GKWMOxT.json', 'var_call_cTisuIrsl5YwQu4ozQuGUWZs': 'file_storage/call_cTisuIrsl5YwQu4ozQuGUWZs.json'}

exec(code, env_args)
