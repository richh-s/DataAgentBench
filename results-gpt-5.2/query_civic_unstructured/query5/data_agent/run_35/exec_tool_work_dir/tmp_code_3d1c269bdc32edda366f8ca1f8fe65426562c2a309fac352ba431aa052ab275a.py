code = """import json
import pandas as pd

path_funding = var_call_RulML30xUVm7z6HjS6Vlheqd
with open(path_funding, 'r', encoding='utf-8') as f:
    funding_totals = json.load(f)
fund_df = pd.DataFrame(funding_totals)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Disaster-related projects: Project_Name contains FEMA/CalOES/CalJPIA
mask = fund_df['Project_Name'].str.contains('(FEMA|CalOES|CalJPIA)', case=False, regex=True, na=False)
disaster_fund = fund_df[mask].copy()

# Started in 2022: heuristic based on project name containing '2022'
started_2022 = disaster_fund[disaster_fund['Project_Name'].str.contains('2022', na=False)]

result = int(started_2022['total_amount'].sum())
print('__RESULT__:')
print(json.dumps({'total_funding': result, 'projects': started_2022['Project_Name'].tolist()}))"""

env_args = {'var_call_YJ2uK7IC5YUxvFQ5GSnMFfDn': ['Funding'], 'var_call_dEt2skTiWFH9rCHgKtKznCXX': ['civic_docs'], 'var_call_RulML30xUVm7z6HjS6Vlheqd': 'file_storage/call_RulML30xUVm7z6HjS6Vlheqd.json', 'var_call_GnrTK04YJ2K9l5O71wRnwMs4': 'file_storage/call_GnrTK04YJ2K9l5O71wRnwMs4.json'}

exec(code, env_args)
