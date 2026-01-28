code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_ADtyOLg9zXIjDrLRpKrSJjCo)
fund = load_records(var_call_HQd5kHqbdrVQsdxSENBOzlDe)

combined = "\n\n".join([d.get('text','') for d in docs])

park_keywords = re.compile(r"\bpark\b|playground|bluffs park|skate park|legacy park|trancas canyon park|malibu park", re.I)

candidates = []
for r in fund:
    name = r.get('Project_Name')
    if not name or name.lower().startswith('project_') or name in ('Discussion','Recommended Action'):
        continue
    if not park_keywords.search(name):
        continue
    pattern = re.compile(re.escape(name), re.I)
    for m in pattern.finditer(combined):
        start = max(0, m.start()-800)
        end = min(len(combined), m.end()+800)
        window = combined[start:end]
        if re.search(r"completed", window, re.I) and re.search(r"2022", window):
            candidates.append(name)
            break

candidates = sorted(set(candidates))

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])
sel = fund_df[fund_df['Project_Name'].isin(candidates)]

total = int(sel['total_amount'].sum()) if len(sel) else 0

out = {
    'total_funding': total,
    'projects': candidates,
    'project_funding': sel[['Project_Name','total_amount']].sort_values('Project_Name').to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ADtyOLg9zXIjDrLRpKrSJjCo': 'file_storage/call_ADtyOLg9zXIjDrLRpKrSJjCo.json', 'var_call_HQd5kHqbdrVQsdxSENBOzlDe': 'file_storage/call_HQd5kHqbdrVQsdxSENBOzlDe.json'}

exec(code, env_args)
