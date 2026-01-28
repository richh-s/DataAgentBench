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

# Keep one project per package version (choose first)
ppv_df = ppv_df.dropna(subset=['ProjectName']).drop_duplicates(subset=['System','Name','Version'])

merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# Extract owner/repo and stars from Project_Information text
rows=[]
for rec in pi:
    txt = rec.get('Project_Information') or ''
    m_repo = re.search(r'\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b', txt)
    m_stars = re.search(r'(?:has garnered|has|with|currently has|and currently has|has an open issues count of \d+,\s+along with a stars count of )\s*(?:a total of )?([0-9,]+)\s+stars', txt)
    # fallback simpler
    if not m_stars:
        m_stars = re.search(r'\b([0-9,]+)\s+stars\b', txt)
    if m_repo and m_stars:
        repo = m_repo.group(1)
        stars = int(m_stars.group(1).replace(',',''))
        rows.append({'ProjectName': repo, 'Stars': stars})

stars_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

merged2 = merged.merge(stars_df, on='ProjectName', how='left')
merged2 = merged2.dropna(subset=['Stars'])

# For packages with multiple github repos, take max stars
best = merged2.sort_values(['System','Name','Stars'], ascending=[True, True, False]).drop_duplicates(subset=['System','Name'])

top5 = best.sort_values('Stars', ascending=False).head(5)

out = top5[['Name','Version','ProjectName','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_g1fm6eUvyVnnJpURKPCqQdKj': 'file_storage/call_g1fm6eUvyVnnJpURKPCqQdKj.json', 'var_call_ARjOrtyN7tkr12WKKpms1n3O': 'file_storage/call_ARjOrtyN7tkr12WKKpms1n3O.json', 'var_call_wflmjMBsRVXEHklUWMBHxqGH': 'file_storage/call_wflmjMBsRVXEHklUWMBHxqGH.json'}

exec(code, env_args)
