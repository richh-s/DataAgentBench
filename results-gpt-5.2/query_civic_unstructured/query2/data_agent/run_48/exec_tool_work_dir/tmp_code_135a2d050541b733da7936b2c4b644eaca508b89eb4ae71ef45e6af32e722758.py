code = """import json, pandas as pd, re

# load funding
fp = var_call_qf7xqPlR2mmtYI8kPnnMKWQw
if isinstance(fp,str) and fp.endswith('.json'):
    with open(fp) as f: fund = json.load(f)
else:
    fund = fp
fund_df=pd.DataFrame(fund)
fund_df['Amount']=pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

# load docs
dp = var_call_I094J3nR4wyEDDpDEy4xwPOd
if isinstance(dp,str) and dp.endswith('.json'):
    with open(dp) as f: docs=json.load(f)
else:
    docs=dp

# Build park-related candidates from funding by name
park_name_df = fund_df[fund_df['Project_Name'].str.contains(r'(?i)\bpark\b', na=False)].copy()
park_projects=set(park_name_df['Project_Name'])

completed_2022=set()

patterns=[r'construction was completed[^\n\.]*2022', r'completed[^\n\.]*2022', r'completed\s*(?:in|,)\s*\w+\s*2022', r'completed\s*\w+\s*2022']
pat=re.compile('|'.join(patterns), re.IGNORECASE)

for d in docs:
    text=d.get('text','') or ''
    low=text.lower()
    if 'completed' not in low or '2022' not in low:
        continue
    for name in park_projects:
        idx=low.find(name.lower())
        if idx==-1:
            continue
        # look 1200 chars after name for completed 2022, or 400 chars before
        after= text[idx:idx+1200]
        before= text[max(0,idx-400):idx+200]
        if pat.search(after) or pat.search(before):
            completed_2022.add(name)

sel=fund_df[fund_df['Project_Name'].isin(completed_2022)]
res={'total_funding': int(sel['Amount'].sum()), 'num_projects': int(sel['Project_Name'].nunique()), 'projects': sorted(sel['Project_Name'].unique().tolist())}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_XGjrDhY9XCRnZyS9KXsopn0B': ['Funding'], 'var_call_qf7xqPlR2mmtYI8kPnnMKWQw': 'file_storage/call_qf7xqPlR2mmtYI8kPnnMKWQw.json', 'var_call_I094J3nR4wyEDDpDEy4xwPOd': 'file_storage/call_I094J3nR4wyEDDpDEy4xwPOd.json', 'var_call_ChEPrykgxqO29y3vAYdMaGvY': {'total_funding': 0, 'num_projects': 0, 'projects': []}}

exec(code, env_args)
