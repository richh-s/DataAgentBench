code = """import json, pandas as pd, re

# Load funding
fp = var_call_qf7xqPlR2mmtYI8kPnnMKWQw
if isinstance(fp, str) and fp.endswith('.json'):
    with open(fp,'r') as f:
        funding_records = json.load(f)
else:
    funding_records = fp
fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

# Load civic docs
dp = var_call_I094J3nR4wyEDDpDEy4xwPOd
if isinstance(dp, str) and dp.endswith('.json'):
    with open(dp,'r') as f:
        docs = json.load(f)
else:
    docs = dp

project_names = set(fund_df['Project_Name'].dropna().astype(str))

# helper to detect completed 2022 in doc text near project name
completed_projects=set()

for d in docs:
    text = d.get('text','') or ''
    # quick skip if no 2022 and no completed
    if '2022' not in text or ('completed' not in text.lower()):
        continue
    low = text.lower()
    # precompute positions of 'completed'
    comp_positions = [m.start() for m in re.finditer('completed', low)]
    if not comp_positions:
        continue
    for name in project_names:
        if not name or len(name)<4:
            continue
        # search occurrences
        for m in re.finditer(re.escape(name), text):
            start=m.start()
            # check a window after occurrence for completion info and 2022
            window = low[start:start+500]
            if 'completed' in window and '2022' in window:
                # park-related?
                if re.search(r'\bpark\b', window) or re.search(r'\bpark\b', low[max(0,start-200):start+500]):
                    completed_projects.add(name)
            else:
                # also allow completed appears before within 200 chars and 2022 after within 500
                pre = low[max(0,start-200):start]
                if 'completed' in pre and '2022' in low[start:start+500]:
                    if re.search(r'\bpark\b', low[max(0,start-200):start+500]):
                        completed_projects.add(name)

# compute total funding
sel = fund_df[fund_df['Project_Name'].isin(completed_projects)]
result = {
    'total_funding': int(sel['Amount'].sum()),
    'num_projects': int(sel['Project_Name'].nunique()),
    'projects': sorted(sel['Project_Name'].unique().tolist())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_XGjrDhY9XCRnZyS9KXsopn0B': ['Funding'], 'var_call_qf7xqPlR2mmtYI8kPnnMKWQw': 'file_storage/call_qf7xqPlR2mmtYI8kPnnMKWQw.json', 'var_call_I094J3nR4wyEDDpDEy4xwPOd': 'file_storage/call_I094J3nR4wyEDDpDEy4xwPOd.json'}

exec(code, env_args)
