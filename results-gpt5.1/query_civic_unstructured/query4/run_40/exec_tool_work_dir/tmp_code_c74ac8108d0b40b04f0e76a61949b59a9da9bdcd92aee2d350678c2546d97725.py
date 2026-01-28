code = """import re, json, pandas as pd

path_docs = var_call_zjN21yoY9K3cQSnErIGdCx2C
with open(path_docs, 'r') as f:
    docs = json.load(f)

path_fund = var_call_eMVi9rru5tuo7Jroti0FyuTg
with open(path_fund, 'r') as f:
    funding = json.load(f)

texts = '\n'.join(d['text'] for d in docs)
lines = texts.split('\n')

projects = []
for i, line in enumerate(lines):
    name = line.strip()
    if not name or len(name.split()) < 2:
        continue
    window = ' '.join(lines[i:i+8])
    if re.search(r'Begin\s+Construction', window, re.IGNORECASE):
        if re.search(r'2022[- ]?(March|April|May|03|04|05|Spring)', window, re.IGNORECASE):
            projects.append(name)

projects = sorted(set(projects))

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)
res = fund_df[fund_df['Project_Name'].isin(projects)]

answer = {
    'spring_2022_projects': projects,
    'count': int(res['Project_Name'].nunique()),
    'total_funding': int(res['Amount'].sum())
}

out = json.dumps(answer)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_zjN21yoY9K3cQSnErIGdCx2C': 'file_storage/call_zjN21yoY9K3cQSnErIGdCx2C.json', 'var_call_eMVi9rru5tuo7Jroti0FyuTg': 'file_storage/call_eMVi9rru5tuo7Jroti0FyuTg.json'}

exec(code, env_args)
