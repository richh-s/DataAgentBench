code = """import re, json
from pathlib import Path

# Load full funding data
import pandas as pd
funding_path = var_call_NhLWRkV3biLFJv1k8QAkMgJ7
funding = pd.read_json(funding_path)

# Filter funding projects whose names suggest FEMA/emergency
mask = funding['Project_Name'].str.contains('FEMA', case=False, na=False) | funding['Project_Name'].str.contains('emergency', case=False, na=False)
filtered = funding.loc[mask, ['Project_Name','Funding_Source','Amount']]

result = filtered.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NhLWRkV3biLFJv1k8QAkMgJ7': 'file_storage/call_NhLWRkV3biLFJv1k8QAkMgJ7.json', 'var_call_Y2czvFf9aP5xZRR6l6QU4qOi': 'file_storage/call_Y2czvFf9aP5xZRR6l6QU4qOi.json'}

exec(code, env_args)
