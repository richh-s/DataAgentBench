code = """import re, json, pandas as pd

with open(var_call_Nyru9P82euwwQqpKXOXT7TZx, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]

projects = []
for text in texts:
    blocks = re.split(r"\n\s*\n", text)
    for b in blocks:
        lines = [l.strip() for l in b.split('\n') if l.strip()]
        if not lines:
            continue
        name = lines[0]
        if len(name.split()) < 2:
            continue
        if not re.search(r"(Project|Improvements|Repairs|Park|Road|Bridge|Drain|Canyon|Facility|Signals|Shade|Biofilter|Playground|Walkway|Study|Maintenance)", name):
            continue
        st = None
        for l in lines[1:]:
            m = re.search(r"(Begin Construction|Start|Project Schedule|Estimated Schedule|Schedule)[:\-]?\s*(.*)", l, re.IGNORECASE)
            if m:
                rest = m.group(2)
                season_match = re.search(r"(Spring|Summer|Fall|Winter)\s*20(\d{2})", rest)
                if season_match:
                    st = season_match.group(0).replace(' ', '-')
                    break
        if st:
            projects.append({'Project_Name': name, 'st': st})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

spring22 = proj_df[proj_df['st'].str.contains('Spring-2022', case=False, na=False)]

if isinstance(var_call_1uw5fdiGpJQc7fRViyV4d5gX, str) and var_call_1uw5fdiGpJQc7fRViyV4d5gX.endswith('.json'):
    with open(var_call_1uw5fdiGpJQc7fRViyV4d5gX, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = var_call_1uw5fdiGpJQc7fRViyV4d5gX

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

merged = pd.merge(spring22, fund_df, on='Project_Name', how='inner')

result = {
    'num_projects_spring_2022': int(merged['Project_Name'].nunique()),
    'total_funding_spring_2022': int(merged['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Nyru9P82euwwQqpKXOXT7TZx': 'file_storage/call_Nyru9P82euwwQqpKXOXT7TZx.json', 'var_call_1uw5fdiGpJQc7fRViyV4d5gX': 'file_storage/call_1uw5fdiGpJQc7fRViyV4d5gX.json', 'var_call_g1YwbKyKtiga6UIT15SmgVmj': ['civic_docs'], 'var_call_TdAfsLG6twQ1KnnzQeV3plEb': ['Funding']}

exec(code, env_args)
