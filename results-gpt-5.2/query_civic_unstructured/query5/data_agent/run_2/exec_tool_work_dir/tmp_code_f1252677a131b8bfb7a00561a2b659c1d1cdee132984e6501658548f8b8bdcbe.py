code = """import json, pandas as pd

ft = var_call_PSEZSqWmIRPvYkhDRIsKOJ2Z
if isinstance(ft, str):
    with open(ft, 'r') as f:
        funding_totals = json.load(f)
else:
    funding_totals = ft

fund_df = pd.DataFrame(funding_totals)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# Disaster-related heuristic using project name suffixes (FEMA/CalOES/CalJPIA/Disaster)
mask = fund_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Disaster', case=False, na=False)
disaster_fund = fund_df[mask].copy()

# Started in 2022: heuristic using project name beginning with 2022 OR contain '2022 '
mask_2022 = disaster_fund['Project_Name'].str.contains(r'(^2022\b|\b2022\b)', case=False, na=False, regex=True)
sel = disaster_fund[mask_2022]

result = {'total_funding': int(sel['total_amount'].sum()), 'project_count': int(sel.shape[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_RvZ50pS5WKtMq9Ygsv93soeX': ['Funding'], 'var_call_lstHaO2T1fNcM1AkXqdQUIcQ': ['civic_docs'], 'var_call_rrITK0lUpo5usLSikqQouxYp': 'file_storage/call_rrITK0lUpo5usLSikqQouxYp.json', 'var_call_PSEZSqWmIRPvYkhDRIsKOJ2Z': 'file_storage/call_PSEZSqWmIRPvYkhDRIsKOJ2Z.json', 'var_call_4rPFe5ACOTdHakiX8K0XORIz': {'ok': True}}

exec(code, env_args)
