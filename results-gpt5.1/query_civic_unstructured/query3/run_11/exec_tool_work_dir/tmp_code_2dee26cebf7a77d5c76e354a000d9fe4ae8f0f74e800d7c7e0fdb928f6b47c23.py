code = """import json, pandas as pd

# Load full funding results
path_funding = var_call_kJIGV1W1zo0N512t8k0jkpGf
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Put into DataFrame
df_fund = pd.DataFrame(funding)

# Filter to projects related to 'emergency' or 'FEMA' in the name (case-insensitive)
mask = df_fund['Project_Name'].str.contains('emergency', case=False, na=False) | df_fund['Project_Name'].str.contains('FEMA', case=False, na=False)
result_df = df_fund[mask][['Project_Name', 'Funding_Source', 'Amount']]

result = result_df.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_kJIGV1W1zo0N512t8k0jkpGf': 'file_storage/call_kJIGV1W1zo0N512t8k0jkpGf.json', 'var_call_JLR6otq5x7zSigSDf309A74G': 'file_storage/call_JLR6otq5x7zSigSDf309A74G.json'}

exec(code, env_args)
