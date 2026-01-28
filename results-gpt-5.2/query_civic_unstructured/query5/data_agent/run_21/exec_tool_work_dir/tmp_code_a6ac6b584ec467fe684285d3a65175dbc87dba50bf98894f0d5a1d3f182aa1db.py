code = """import json, pandas as pd

# funding
with open(var_call_xpe1J6bZRj5eub6Cr9CJ7LkJ, 'r', encoding='utf-8') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['total_amount'] = pd.to_numeric(df_f['total_amount'], errors='coerce').fillna(0).astype('int64')

# docs
with open(var_call_bH8yuIz4aLh3wd45vlj4LmLY, 'r', encoding='utf-8') as f:
    docs = json.load(f)

funded_projects = set(df_f['Project_Name'].dropna().astype(str))

def is_disaster_name(name: str) -> bool:
    n = name.lower()
    return ('fema' in n) or ('caloes' in n) or ('caljpia' in n) or ('disaster' in n) or ('recovery' in n) or ('fire' in n) or ('woolsey' in n)

# Heuristic: for disaster-named projects, treat as started in 2022 if any doc contains both
# the project name and a 'Begin Construction: ...2022' or 'Start: ...2022' within 40 lines after occurrence.
# To avoid regex escaping issues, do simple substring checks line-by-line.

disaster_started_2022 = set()

for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue
    lines = text.splitlines()
    low_lines = [ln.lower() for ln in lines]
    low_text = text.lower()

    candidates = [p for p in funded_projects if p and is_disaster_name(p) and p.lower() in low_text]
    if not candidates:
        continue

    for p in candidates:
        pl = p.lower()
        idxs = [i for i, ln in enumerate(low_lines) if pl in ln]
        for idx in idxs:
            win = low_lines[idx: min(len(lines), idx+50)]
            for ln in win:
                if ('begin construction' in ln or ln.strip().startswith('start')) and '2022' in ln:
                    disaster_started_2022.add(p)
                    break
            if p in disaster_started_2022:
                break

sum_amt = int(df_f[df_f['Project_Name'].isin(disaster_started_2022)]['total_amount'].sum())

out = {
    'total_funding': sum_amt,
    'num_projects': int(len(disaster_started_2022)),
    'projects': sorted(disaster_started_2022)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xpe1J6bZRj5eub6Cr9CJ7LkJ': 'file_storage/call_xpe1J6bZRj5eub6Cr9CJ7LkJ.json', 'var_call_bH8yuIz4aLh3wd45vlj4LmLY': 'file_storage/call_bH8yuIz4aLh3wd45vlj4LmLY.json', 'var_call_kOBRjFba7uPAiIIvjNbnKFbZ': ['Funding'], 'var_call_giorFytyNRBYlN9KnawCT1yA': ['civic_docs']}

exec(code, env_args)
