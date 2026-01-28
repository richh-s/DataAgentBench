code = """import json
import pandas as pd
import re
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v
pkg_records = load_var(var_call_cEoAVZZQiXs8LbPFKVNsh0Tn)
ppv_records = load_var(var_call_Bt55lTKTn4u6dPdldrniwswp)
projinfo_records = load_var(var_call_sdHuICrVVlskQ5jKTpq9Dbna)
df_pkg = pd.DataFrame(pkg_records)
df_ppv = pd.DataFrame(ppv_records)
df_proj = pd.DataFrame(projinfo_records)
merged = pd.merge(df_pkg, df_ppv, on=['System','Name','Version'], how='inner')
project_names = set(merged['ProjectName'].dropna().unique().tolist())
def extract_owner_repo(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)', s)
    return m.group(1) if m else None

# apply
df_proj['owner_repo'] = df_proj['Project_Information'].apply(extract_owner_repo)

def has_mit(lic):
    if not isinstance(lic, str):
        return False
    return 'MIT' in lic

filtered = df_proj[df_proj['owner_repo'].isin(project_names) & df_proj['Licenses'].apply(has_mit)].copy()
patterns = [r'([\d,]+)\s*forks', r'forked\s*([\d,]+)\s*times', r'forks count of\s*([\d,]+)', r'forks count[:\s]*([\d,]+)']
def extract_forks(text):
    if not isinstance(text, str):
        return 0
    for p in patterns:
        m = re.search(p, text, flags=re.IGNORECASE)
        if m:
            num = m.group(1)
            num = num.replace(',', '')
            try:
                return int(num)
            except:
                continue
    return 0

filtered['forks'] = filtered['Project_Information'].apply(extract_forks)
agg = filtered.groupby('owner_repo', as_index=False).agg({'forks':'max'})
top5 = agg.sort_values('forks', ascending=False).head(5)
result = []
for _, row in top5.iterrows():
    result.append({'project': row['owner_repo'], 'forks': int(row['forks'])})
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cEoAVZZQiXs8LbPFKVNsh0Tn': 'file_storage/call_cEoAVZZQiXs8LbPFKVNsh0Tn.json', 'var_call_Bt55lTKTn4u6dPdldrniwswp': 'file_storage/call_Bt55lTKTn4u6dPdldrniwswp.json', 'var_call_sdHuICrVVlskQ5jKTpq9Dbna': 'file_storage/call_sdHuICrVVlskQ5jKTpq9Dbna.json'}

exec(code, env_args)
