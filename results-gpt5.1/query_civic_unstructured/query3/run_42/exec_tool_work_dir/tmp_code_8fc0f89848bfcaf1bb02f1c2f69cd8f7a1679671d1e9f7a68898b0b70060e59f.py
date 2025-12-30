code = """import json, pandas as pd
from pathlib import Path

# Load full funding data
funding_path = var_call_NZ9MylwMaac77cRhTMahKLwN
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Convert to DataFrame
f_df = pd.DataFrame(funding)

# Filter projects whose names suggest FEMA/emergency relevance
mask = f_df['Project_Name'].str.contains('FEMA', case=False, na=False) | f_df['Project_Name'].str.contains('Emergency', case=False, na=False)
result_df = f_df.loc[mask, ['Project_Name', 'Funding_Source', 'Amount']]

result = result_df.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_NZ9MylwMaac77cRhTMahKLwN': 'file_storage/call_NZ9MylwMaac77cRhTMahKLwN.json', 'var_call_OUVGPnyEYhxpE0T71fh7RWrY': 'file_storage/call_OUVGPnyEYhxpE0T71fh7RWrY.json'}

exec(code, env_args)
