code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_rBZwuDjTsXSCOOMA47fnyCya)
fund = load_records(var_call_ECOXYDdx7UyF66cFrhDhAtkw)

park_completed_2022 = set()
park_keywords = ['park','playground','skate','bluffs','legacy','trancas','point dume walkway','shade structure']
comp_2022_pat = re.compile(r'completed[^\n\.]*\b(2022)\b', re.IGNORECASE)

for d in docs:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        low = ln.lower()
        if low.startswith(('public works','agenda','to','prepared by','approved by','date prepared','meeting date','subject','recommended action','discussion','capital improvement projects','disaster recovery projects','page ')):
            continue
        if len(ln) > 120 or ':' in ln:
            continue
        if not re.search(r'[A-Za-z]', ln):
            continue
        window = "\n".join(lines[i:i+40])
        if comp_2022_pat.search(window) and any(k in low for k in park_keywords):
            park_completed_2022.add(ln)

for d in docs:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    for idx, ln in enumerate(lines):
        if comp_2022_pat.search(ln):
            for j in range(1, 15):
                if idx-j < 0:
                    break
                cand = lines[idx-j]
                if not cand or ':' in cand:
                    continue
                clow = cand.lower()
                if clow.startswith(('updates','(cid','project schedule','estimated schedule','capital improvement projects','disaster recovery projects','project description','project updates')):
                    continue
                if len(cand) > 120:
                    continue
                if any(k in clow for k in park_keywords):
                    park_completed_2022.add(cand)
                    break

fund_df = pd.DataFrame(fund)
fund_df['Project_Name_norm'] = fund_df['Project_Name'].astype(str).str.strip().str.lower()
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0)

park_list = sorted(park_completed_2022)
park_norm = [p.strip().lower() for p in park_list]
matched = fund_df[fund_df['Project_Name_norm'].isin(park_norm)].copy()

total = int(matched['total_amount'].sum())

out = {
    'park_completed_2022_projects': park_list,
    'matched_funding_projects': matched[['Project_Name','total_amount']].to_dict(orient='records'),
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_smXPOBk8I2nHR1Q7DTEhBVE7': ['Funding'], 'var_call_rBZwuDjTsXSCOOMA47fnyCya': 'file_storage/call_rBZwuDjTsXSCOOMA47fnyCya.json', 'var_call_ECOXYDdx7UyF66cFrhDhAtkw': 'file_storage/call_ECOXYDdx7UyF66cFrhDhAtkw.json'}

exec(code, env_args)
