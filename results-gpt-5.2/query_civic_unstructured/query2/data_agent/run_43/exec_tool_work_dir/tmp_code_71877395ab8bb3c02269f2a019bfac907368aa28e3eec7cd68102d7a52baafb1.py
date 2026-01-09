code = """import json, re, pandas as pd

path_docs = var_call_fNGMQN7rsGT753P1DhDoSjRg
if isinstance(path_docs, str):
    with open(path_docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = path_docs

path_fund = var_call_i24rwJefKrIAwf8WGY46Fd1j
if isinstance(path_fund, str):
    with open(path_fund, 'r', encoding='utf-8') as f:
        fund = json.load(f)
else:
    fund = path_fund

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

all_text = "\n".join([d.get('text','') for d in docs])

idx = all_text.lower().find('capital improvement projects (completed)')
if idx >= 0:
    sub = all_text[idx:]
    # end at 'disaster projects' if exists
    j = sub.lower().find('disaster projects')
    completed_block = sub[:j] if j >= 0 else sub
else:
    completed_block = all_text

park_re = r"\bpark\b|playground|skate|bluffs|legacy park|trancas canyon park|point dume"
park_projects = fund_df[fund_df['Project_Name'].fillna('').str.contains(park_re, case=False, regex=True)].copy()

completed_mask = park_projects['Project_Name'].apply(lambda n: str(n) != 'nan' and (str(n).lower() in completed_block.lower()))
completed_park_projects = park_projects[completed_mask].copy()

result = {
    'total_funding': int(completed_park_projects['total_amount'].sum()),
    'completed_park_projects': completed_park_projects[['Project_Name','total_amount']].sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_iY9iEMBFD1F9AEybuTddJbwP': ['Funding'], 'var_call_t17aCCEPYBdI8yfkojzgW6Zc': ['civic_docs'], 'var_call_fNGMQN7rsGT753P1DhDoSjRg': 'file_storage/call_fNGMQN7rsGT753P1DhDoSjRg.json', 'var_call_i24rwJefKrIAwf8WGY46Fd1j': 'file_storage/call_i24rwJefKrIAwf8WGY46Fd1j.json'}

exec(code, env_args)
