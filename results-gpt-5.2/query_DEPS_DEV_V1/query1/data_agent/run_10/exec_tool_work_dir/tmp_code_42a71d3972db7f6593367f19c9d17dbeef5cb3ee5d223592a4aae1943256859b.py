code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

latest = load_records(var_call_g1fm6eUvyVnnJpURKPCqQdKj)
ppv = load_records(var_call_ARjOrtyN7tkr12WKKpms1n3O)
pi = load_records(var_call_wflmjMBsRVXEHklUWMBHxqGH)

latest_df = pd.DataFrame(latest)
ppv_df = pd.DataFrame(ppv)

ppv_df = ppv_df.dropna(subset=['ProjectName']).drop_duplicates(subset=['System','Name','Version'])
merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

rows=[]
for rec in pi:
    txt = rec.get('Project_Information') or ''
    m_repo = re.search(r'\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b', txt)
    m_stars = re.search(r'\b([0-9,]+)\s+stars\b', txt)
    if m_repo and m_stars:
        rows.append({'ProjectName': m_repo.group(1), 'Stars': int(m_stars.group(1).replace(',',''))})

stars_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])
merged2 = merged.merge(stars_df, on='ProjectName', how='left').dropna(subset=['Stars'])

best = merged2.sort_values(['System','Name','Stars'], ascending=[True, True, False]).drop_duplicates(subset=['System','Name'])
top5 = best.sort_values('Stars', ascending=False).head(5)

out = top5[['Name','Version','ProjectName','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_g1fm6eUvyVnnJpURKPCqQdKj': 'file_storage/call_g1fm6eUvyVnnJpURKPCqQdKj.json', 'var_call_ARjOrtyN7tkr12WKKpms1n3O': 'file_storage/call_ARjOrtyN7tkr12WKKpms1n3O.json', 'var_call_wflmjMBsRVXEHklUWMBHxqGH': 'file_storage/call_wflmjMBsRVXEHklUWMBHxqGH.json', 'var_call_IBrNSDvMfnv3jfKQamNJ8heQ': {'columns': ['System', 'Name', 'Version', 'ProjectName'], 'ncols': 4, 'sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}]}}

exec(code, env_args)
