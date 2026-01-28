code = """import json, re
import pandas as pd

# Load full funding data
with open(var_call_BrBdGCOHOHCgllxrE84Sno0R) as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)

# Disaster projects: names containing FEMA, CalOES, or CalJPIA
mask_disaster = fund_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, regex=True)

# 2022 start year from name if present
mask_2022 = fund_df['Project_Name'].str.contains('2022', regex=False)

# Filter
df = fund_df[mask_disaster & mask_2022].copy()

# Convert Amount to int and sum
df['Amount'] = df['Amount'].astype(int)
result = int(df['Amount'].sum())

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZtoKCylLY238bLubBRmSVmep': 'file_storage/call_ZtoKCylLY238bLubBRmSVmep.json', 'var_call_BrBdGCOHOHCgllxrE84Sno0R': 'file_storage/call_BrBdGCOHOHCgllxrE84Sno0R.json'}

exec(code, env_args)
