code = """import json, pathlib

obj = var_call_wcH0G5gICzozKFOzOjxZV2v5
if isinstance(obj, str):
    funding = json.loads(pathlib.Path(obj).read_text())
else:
    funding = obj

# Identify park-related projects by name containing 'Park'
park = [r for r in funding if 'Project_Name' in r and isinstance(r['Project_Name'], str) and 'Park' in r['Project_Name']]

# From known docs, 'Bluffs Park Shade Structure' completed Nov 2022.
# Consider park-related projects completed in 2022 as those with explicit completed Nov 2022 in agenda status reports.
# In provided extract, only Bluffs Park Shade Structure has completion in Nov 2022.

total = 0
included=[]
for r in park:
    if r['Project_Name'] == 'Bluffs Park Shade Structure':
        amt = int(r['Total_Amount'])
        total += amt
        included.append({'Project_Name': r['Project_Name'], 'Total_Amount': amt})

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'included_projects': included}))"""

env_args = {'var_call_tEb2QUBsxnJuTQFmoMn6ttnX': ['Funding'], 'var_call_iIVaQT6kP5WyVCoQ1lJTuaP0': ['civic_docs'], 'var_call_HBmVCfCZr2ZNgGuyYKXf7Yf3': 'file_storage/call_HBmVCfCZr2ZNgGuyYKXf7Yf3.json', 'var_call_dxEi22kLvq8oSeo1t8m5SSHb': 'file_storage/call_dxEi22kLvq8oSeo1t8m5SSHb.json', 'var_call_wcH0G5gICzozKFOzOjxZV2v5': 'file_storage/call_wcH0G5gICzozKFOzOjxZV2v5.json', 'var_call_9SSZbnlHQCmbAtkhIk5xfjaa': []}

exec(code, env_args)
