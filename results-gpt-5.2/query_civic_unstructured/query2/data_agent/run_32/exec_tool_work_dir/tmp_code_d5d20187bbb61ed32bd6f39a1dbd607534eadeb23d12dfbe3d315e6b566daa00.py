code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_rBZwuDjTsXSCOOMA47fnyCya)
fund = load_records(var_call_ECOXYDdx7UyF66cFrhDhAtkw)

# Directly identify park-related projects with completion in 2022 by regex around known lines in documents.
text_all = "\n".join([d.get('text','') for d in docs])

# Find project name lines preceding 'Construction was completed <month> 2022'
pat = re.compile(r"\n(?P<name>[^\n]{3,120})\n\s*\(cid:[^\n]*\n\s*Updates:.*?completed[^\n]*2022", re.IGNORECASE|re.DOTALL)

cands = set()
for m in pat.finditer(text_all):
    name = m.group('name').strip()
    low = name.lower()
    if any(k in low for k in ['park','playground','skate','bluffs','legacy','trancas','point dume','shade structure']):
        cands.add(name)

fund_df = pd.DataFrame(fund)
fund_df['Project_Name_norm'] = fund_df['Project_Name'].astype(str).str.strip().str.lower()
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0)

cand_list = sorted(cands)
matched = fund_df[fund_df['Project_Name_norm'].isin([x.lower() for x in cand_list])]

total = int(matched['total_amount'].sum())

out = {'projects': cand_list, 'total_funding': total}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_smXPOBk8I2nHR1Q7DTEhBVE7': ['Funding'], 'var_call_rBZwuDjTsXSCOOMA47fnyCya': 'file_storage/call_rBZwuDjTsXSCOOMA47fnyCya.json', 'var_call_ECOXYDdx7UyF66cFrhDhAtkw': 'file_storage/call_ECOXYDdx7UyF66cFrhDhAtkw.json'}

exec(code, env_args)
