code = """import json, pandas as pd

# load docs with completion 2022
civic = var_call_jYipL3T0cdQW6JjMADV4XYq4
if isinstance(civic, str):
    with open(civic, 'r') as f:
        civic = json.load(f)

fund = var_call_s84kqxjOfocZJ8F4wVH0rYf8
if isinstance(fund, str):
    with open(fund, 'r') as f:
        fund = json.load(f)

df_fund = pd.DataFrame(fund)
df_fund['total_amount'] = pd.to_numeric(df_fund['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(df_fund['Project_Name'], df_fund['total_amount']))

# From the 03-22-23 status report, park-related completed in Nov 2022 (as shown in text):
projects = ['Bluffs Park Shade Structure']

total = sum(fund_map.get(p,0) for p in projects)

out = {'projects': projects, 'total_funding': int(total)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WWB5hoLLQPARfKgi6461w7sT': ['Funding'], 'var_call_18SqMu3sFkfgtuXiCBontVSP': ['civic_docs'], 'var_call_eIC9RQkWUxJuxTKZvSmWYoxc': 'file_storage/call_eIC9RQkWUxJuxTKZvSmWYoxc.json', 'var_call_s84kqxjOfocZJ8F4wVH0rYf8': 'file_storage/call_s84kqxjOfocZJ8F4wVH0rYf8.json', 'var_call_jYipL3T0cdQW6JjMADV4XYq4': 'file_storage/call_jYipL3T0cdQW6JjMADV4XYq4.json'}

exec(code, env_args)
