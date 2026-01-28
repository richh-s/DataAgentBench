code = """import json, pandas as pd
from pathlib import Path

# Load full funding data
funding_path = var_call_q8jaT7BiWAnNCHFee0eUWLQZ
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)

# Filter projects whose names suggest FEMA/emergency relevance
mask = funding_df['Project_Name'].str.contains('FEMA', case=False, na=False) | \
       funding_df['Project_Name'].str.contains('emergency', case=False, na=False)

relevant = funding_df.loc[mask, ['Project_Name', 'Funding_Source', 'Amount']]

result = relevant.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_q8jaT7BiWAnNCHFee0eUWLQZ': 'file_storage/call_q8jaT7BiWAnNCHFee0eUWLQZ.json', 'var_call_spbbi9aO8qwUrD5j0tssf1Ju': 'file_storage/call_spbbi9aO8qwUrD5j0tssf1Ju.json'}

exec(code, env_args)
