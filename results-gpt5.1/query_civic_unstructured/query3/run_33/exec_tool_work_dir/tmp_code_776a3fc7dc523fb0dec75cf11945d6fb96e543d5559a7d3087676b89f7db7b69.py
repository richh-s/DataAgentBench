code = """import json, pandas as pd

funding = pd.read_json(var_call_jMR7qpIIsPL15NscUeSo5zoi)

# Filter projects whose names suggest FEMA/emergency relevance
mask = funding['Project_Name'].str.contains('FEMA', case=False, na=False) | funding['Project_Name'].str.contains('emergency', case=False, na=False) | funding['Project_Name'].str.contains('Warning', case=False, na=False)
rel = funding[mask][['Project_Name','Funding_Source','Amount']].reset_index(drop=True)

result = rel.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_jMR7qpIIsPL15NscUeSo5zoi': 'file_storage/call_jMR7qpIIsPL15NscUeSo5zoi.json', 'var_call_wSllEUxGyXGNFxiDvG6vhPZU': 'file_storage/call_wSllEUxGyXGNFxiDvG6vhPZU.json'}

exec(code, env_args)
