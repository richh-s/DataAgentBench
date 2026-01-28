code = """import json, re
import pandas as pd

def load_result(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

funding = load_result(var_call_bOOz23WYBvTWRqo0YznHKIHe)
docs = load_result(var_call_lErE1gjrVmu0A0NLFQ7uSw3P)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype('int64')

# Simpler approach: if a project is disaster-related (name contains FEMA/CalOES/CalJPIA or doc has Disaster Recovery Projects section mentioning it)
# and the doc text contains both the project name and year 2022 near words Begin/Start.

begin_pat = re.compile(r"\b(Begin|Start)\b.{0,80}2022|2022.{0,80}\b(Begin|Start)\b", re.IGNORECASE|re.DOTALL)

# candidate disaster project names from funding table
cand = fund_df[fund_df['Project_Name'].str.contains(r"FEMA|CalOES|CalJPIA", case=False, regex=True, na=False)]['Project_Name'].unique().tolist()

started = set()
for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text and 'Disaster recovery projects' not in text:
        # still might mention FEMA project in capital list; keep scanning using candidates
        pass
    for name in cand:
        if name in text:
            # take a small neighborhood around first occurrence
            idx = text.find(name)
            snippet = text[max(0, idx-400): idx+800]
            if begin_pat.search(snippet):
                started.add(name)

sel = fund_df[fund_df['Project_Name'].isin(started)]
out = {
    'total_funding_usd': int(sel['total_amount'].sum()),
    'matched_projects_count': int(sel['Project_Name'].nunique()),
    'matched_projects': sel.sort_values('total_amount', ascending=False)[['Project_Name','total_amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bOOz23WYBvTWRqo0YznHKIHe': 'file_storage/call_bOOz23WYBvTWRqo0YznHKIHe.json', 'var_call_lErE1gjrVmu0A0NLFQ7uSw3P': 'file_storage/call_lErE1gjrVmu0A0NLFQ7uSw3P.json'}

exec(code, env_args)
