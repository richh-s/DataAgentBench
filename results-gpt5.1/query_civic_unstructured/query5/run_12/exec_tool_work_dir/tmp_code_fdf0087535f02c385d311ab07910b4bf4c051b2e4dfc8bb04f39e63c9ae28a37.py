code = """import json, re, pandas as pd
path = var_call_wHli7EZTdU0PuSIFJAmDOKrr
with open(path, 'r') as f:
    funding = json.load(f)
df = pd.DataFrame(funding)
mask_disaster = df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Disaster', case=False, regex=True)
mask_2022 = df['Project_Name'].str.contains('2022', case=False, regex=False)
sel = df[mask_disaster & mask_2022].copy()
sel['Amount'] = sel['Amount'].astype(int)
total_funding = int(sel['Amount'].sum())
print('__RESULT__:')
print(json.dumps(total_funding))"""

env_args = {'var_call_YtiM3HZD3AfptUlZQhMyHWxR': 'file_storage/call_YtiM3HZD3AfptUlZQhMyHWxR.json', 'var_call_wHli7EZTdU0PuSIFJAmDOKrr': 'file_storage/call_wHli7EZTdU0PuSIFJAmDOKrr.json'}

exec(code, env_args)
