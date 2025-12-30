code = """import json, pandas as pd

# Load full funding data
path_funding = var_call_QZlfHEtLmRGIOvWzeFspXSeU
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Convert to DataFrame
df_funding = pd.DataFrame(funding)

# Filter projects whose names contain 'FEMA' or 'emergency' (case-insensitive)
mask = df_funding['Project_Name'].str.contains('FEMA', case=False, na=False) | df_funding['Project_Name'].str.contains('emergency', case=False, na=False)
result = df_funding.loc[mask, ['Project_Name', 'Funding_Source', 'Amount']]

out = result.to_dict(orient='records')

out_json = json.dumps(out)
print("__RESULT__:")
print(out_json)"""

env_args = {'var_call_QZlfHEtLmRGIOvWzeFspXSeU': 'file_storage/call_QZlfHEtLmRGIOvWzeFspXSeU.json', 'var_call_0ElrGwGaHLFJp7Fkv6a9ymsn': 'file_storage/call_0ElrGwGaHLFJp7Fkv6a9ymsn.json'}

exec(code, env_args)
