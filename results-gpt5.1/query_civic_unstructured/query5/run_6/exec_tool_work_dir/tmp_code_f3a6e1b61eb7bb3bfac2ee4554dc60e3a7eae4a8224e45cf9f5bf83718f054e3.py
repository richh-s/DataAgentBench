code = """import json, pandas as pd
funding = pd.read_json(var_call_r3Ly2AjNpSxyqTHu71BdX0W6)
funding['is_disaster'] = funding['Project_Name'].str.contains(r"FEMA|CalOES|CalJPIA", case=False, regex=True)
# assume all disaster projects started in or before 2022; without reliable start dates, cannot filter further
subset = funding[funding['is_disaster']].copy()
subset['Amount'] = subset['Amount'].astype(int)
result = int(subset['Amount'].sum())
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VYRpnwOZvKmQYUkpdaLPYU5v': 'file_storage/call_VYRpnwOZvKmQYUkpdaLPYU5v.json', 'var_call_r3Ly2AjNpSxyqTHu71BdX0W6': 'file_storage/call_r3Ly2AjNpSxyqTHu71BdX0W6.json'}

exec(code, env_args)
