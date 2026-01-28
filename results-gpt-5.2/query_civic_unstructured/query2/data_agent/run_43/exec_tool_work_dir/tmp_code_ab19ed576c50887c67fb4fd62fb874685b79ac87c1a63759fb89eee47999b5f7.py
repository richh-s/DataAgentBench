code = """import json, re, pandas as pd

# Load civic docs (2022 filenames)
path_docs = var_call_fNGMQN7rsGT753P1DhDoSjRg
if isinstance(path_docs, str):
    with open(path_docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = path_docs

# Load funding totals by project
path_fund = var_call_i24rwJefKrIAwf8WGY46Fd1j
if isinstance(path_fund, str):
    with open(path_fund, 'r', encoding='utf-8') as f:
        fund = json.load(f)
else:
    fund = path_fund
fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

all_text = "\n".join([d.get('text','') for d in docs])

m = re.search(r"Capital Improvement Projects \(Completed\)(.*?)(?:Disaster Projects \(|\Z)", all_text, flags=re.S|re.I)
completed_block = m.group(1) if m else all_text

park_projects = fund_df[fund_df['Project_Name'].fillna('').str.contains(r"\bpark\b|playground|skate|bluffs|legacy park|trancas canyon park|point dume", case=False, regex=True)].copy()

completed_mask = park_projects['Project_Name'].apply(lambda n: re.search(re.escape(str(n)), completed_block, flags=re.I) is not None)
completed_park_projects = park_projects[completed_mask].copy()

result = {
    "total_funding": int(completed_park_projects['total_amount'].sum()),
    "completed_park_projects": completed_park_projects[['Project_Name','total_amount']].sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_iY9iEMBFD1F9AEybuTddJbwP': ['Funding'], 'var_call_t17aCCEPYBdI8yfkojzgW6Zc': ['civic_docs'], 'var_call_fNGMQN7rsGT753P1DhDoSjRg': 'file_storage/call_fNGMQN7rsGT753P1DhDoSjRg.json', 'var_call_i24rwJefKrIAwf8WGY46Fd1j': 'file_storage/call_i24rwJefKrIAwf8WGY46Fd1j.json'}

exec(code, env_args)
