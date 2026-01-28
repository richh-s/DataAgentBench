code = """import json, pandas as pd, os

# Load full funding data
path_funding = var_call_VzGno0U11i8DjWvsNVmEGBib
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Convert to DataFrame
fdf = pd.DataFrame(funding)

# Identify projects related to 'emergency' or 'FEMA' by name keywords
mask = fdf['Project_Name'].str.contains('FEMA', case=False, na=False) | fdf['Project_Name'].str.contains('Emergency', case=False, na=False)
rel = fdf[mask][['Project_Name','Funding_Source','Amount']]

result = rel.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VzGno0U11i8DjWvsNVmEGBib': 'file_storage/call_VzGno0U11i8DjWvsNVmEGBib.json', 'var_call_Z0l0Of5PhFI2obKL7mac47RD': 'file_storage/call_Z0l0Of5PhFI2obKL7mac47RD.json'}

exec(code, env_args)
