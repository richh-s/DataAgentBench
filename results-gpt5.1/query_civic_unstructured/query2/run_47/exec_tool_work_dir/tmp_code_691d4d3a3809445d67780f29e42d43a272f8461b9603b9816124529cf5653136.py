code = """import json, pandas as pd
from pathlib import Path

path_docs = Path(var_call_AAeTGnT9IIBClmrhYnrkNdM6)
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

path_fund = Path(var_call_cl6hZ5Bbvk95U1yWNOMsCfkX)
with open(path_fund, 'r') as f:
    funding = json.load(f)

park_projects_2022 = set(["Bluffs Park Shade Structure"])

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'])
mask = fund_df['Project_Name'].isin(park_projects_2022)
total = float(fund_df.loc[mask, 'Amount'].sum())
result = {"total_funding_park_projects_completed_2022": total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AAeTGnT9IIBClmrhYnrkNdM6': 'file_storage/call_AAeTGnT9IIBClmrhYnrkNdM6.json', 'var_call_cl6hZ5Bbvk95U1yWNOMsCfkX': 'file_storage/call_cl6hZ5Bbvk95U1yWNOMsCfkX.json'}

exec(code, env_args)
