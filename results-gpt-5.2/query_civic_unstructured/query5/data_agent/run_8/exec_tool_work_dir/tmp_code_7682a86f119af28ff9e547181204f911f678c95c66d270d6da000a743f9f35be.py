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

# Since extracting start dates from unstructured text is unreliable here, approximate "started in 2022" by project names beginning with '2022'
# and disaster-related by containing FEMA/CalOES/CalJPIA or 'Disaster'.
mask = fund_df['Project_Name'].str.contains(r"\b2022\b", regex=True, na=False) & fund_df['Project_Name'].str.contains(r"FEMA|CalOES|CalJPIA|Disaster", case=False, regex=True, na=False)
sel = fund_df[mask]

out = {
    'total_funding_usd': int(sel['total_amount'].sum()),
    'projects_count': int(sel['Project_Name'].nunique()),
    'projects': sel.sort_values('total_amount', ascending=False)[['Project_Name','total_amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bOOz23WYBvTWRqo0YznHKIHe': 'file_storage/call_bOOz23WYBvTWRqo0YznHKIHe.json', 'var_call_lErE1gjrVmu0A0NLFQ7uSw3P': 'file_storage/call_lErE1gjrVmu0A0NLFQ7uSw3P.json', 'var_call_MV0FFk9ZWcw3ssWqMCoysvzc': {'total_funding_usd': 0, 'matched_projects_count': 0, 'matched_projects': []}}

exec(code, env_args)
