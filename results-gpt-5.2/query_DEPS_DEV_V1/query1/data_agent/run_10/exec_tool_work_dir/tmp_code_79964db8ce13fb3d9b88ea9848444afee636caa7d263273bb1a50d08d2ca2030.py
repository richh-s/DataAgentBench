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
merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

rows=[]
for rec in pi:
    txt = rec.get('Project_Information') or ''
    m_repo = re.search(r'\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b', txt)
    m_stars = re.search(r'\b([0-9,]+)\s+stars\b', txt)
    if m_repo and m_stars:
        rows.append({'ProjectName': m_repo.group(1), 'Stars': int(m_stars.group(1).replace(',',''))})

stars_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

merged2 = merged.merge(stars_df, on='ProjectName', how='left', suffixes=('', '_pi'))

print('__RESULT__:')
print(json.dumps({'merged2_cols': list(merged2.columns), 'na_stars': int(merged2["Stars"].isna().sum()), 'nrows': int(len(merged2))}))"""

env_args = {'var_call_g1fm6eUvyVnnJpURKPCqQdKj': 'file_storage/call_g1fm6eUvyVnnJpURKPCqQdKj.json', 'var_call_ARjOrtyN7tkr12WKKpms1n3O': 'file_storage/call_ARjOrtyN7tkr12WKKpms1n3O.json', 'var_call_wflmjMBsRVXEHklUWMBHxqGH': 'file_storage/call_wflmjMBsRVXEHklUWMBHxqGH.json', 'var_call_IBrNSDvMfnv3jfKQamNJ8heQ': {'columns': ['System', 'Name', 'Version', 'ProjectName'], 'ncols': 4, 'sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}]}, 'var_call_0xhBUaBnto81g7HSpNr1oQWV': {'merged_cols': ['System', 'Name', 'Version', 'ProjectName'], 'head': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/pagination', 'Version': '3.4.1', 'ProjectName': 'discordx-ts/discordx'}]}}

exec(code, env_args)
