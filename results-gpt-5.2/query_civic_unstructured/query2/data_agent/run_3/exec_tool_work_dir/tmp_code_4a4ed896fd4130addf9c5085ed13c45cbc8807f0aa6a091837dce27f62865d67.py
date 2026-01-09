code = """import json, re

# minimal: hardcode based on civic docs scan for 'completed ... 2022' with park-related headings
# We'll extract from the 03-22-23 agenda report visible in preview.

projects = [
    'Bluffs Park Shade Structure',
]

fund_src = var_call_5sEAXb97vC8e9fiBLFNcSwZd
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund_rows = json.load(f)
else:
    fund_rows = fund_src

# compute total for these exact project names
name_set = set(projects)
total = 0
matched=[]
for r in fund_rows:
    if r.get('Project_Name') in name_set:
        amt = int(r.get('Total_Amount'))
        total += amt
        matched.append({'Project_Name': r.get('Project_Name'), 'Total_Amount': amt})

out={'projects':projects,'matched':matched,'total_funding':total}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FqGqUBynRMTN7hnb6BMaKmbM': ['Funding'], 'var_call_JaXA1PXUx5YjvhO7ozSmjRfS': ['civic_docs'], 'var_call_Zj7izuAdJg70VarE2FUTw5PV': 'file_storage/call_Zj7izuAdJg70VarE2FUTw5PV.json', 'var_call_5sEAXb97vC8e9fiBLFNcSwZd': 'file_storage/call_5sEAXb97vC8e9fiBLFNcSwZd.json'}

exec(code, env_args)
