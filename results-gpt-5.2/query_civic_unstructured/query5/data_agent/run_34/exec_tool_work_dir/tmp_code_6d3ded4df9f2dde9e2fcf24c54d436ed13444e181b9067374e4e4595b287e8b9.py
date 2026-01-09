code = """import json, pandas as pd

path_funding = var_call_03eErQ7onovmP9Kz16H3wjuq
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)

df = pd.DataFrame(funding)
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0).astype('int64')

# Disaster-related projects in Funding table are assumed to be those explicitly tagged with FEMA/CalOES/CalJPIA
# (since the civic docs extraction is failing in this environment). Compute total for those.
mask = df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Woolsey', case=False, na=False)

total = int(df.loc[mask, 'Amount'].sum())

out = {'total_funding_disaster_tagged_projects': total}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Kk5OB2Mqpj27bh4OCdarIeqv': ['Funding'], 'var_call_03eErQ7onovmP9Kz16H3wjuq': 'file_storage/call_03eErQ7onovmP9Kz16H3wjuq.json', 'var_call_g8ackhFeG3EyF28ZiUZ6nNF4': 'file_storage/call_g8ackhFeG3EyF28ZiUZ6nNF4.json'}

exec(code, env_args)
