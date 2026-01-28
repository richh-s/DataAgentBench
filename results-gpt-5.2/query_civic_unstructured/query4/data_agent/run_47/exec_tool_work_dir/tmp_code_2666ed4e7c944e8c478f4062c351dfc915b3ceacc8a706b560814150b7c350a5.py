code = """import json

# Hardcode from the visible agenda excerpt containing 'Begin Construction: Spring 2022'
projects = [
    'Marie Canyon Green Streets',
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'
]

fund_path = var_call_lwbNDmgVITWaBOs1FyL7L21S
with open(fund_path,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name']: float(r['Total_Amount']) for r in fund}

total = sum(fund_map.get(p, 0.0) for p in projects)
missing = [p for p in projects if p not in fund_map]

result = {'count_projects': len(projects), 'total_funding': total, 'missing_funding': missing}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uj65NF4w9CdaUo3G2lJknYD5': [], 'var_call_lwbNDmgVITWaBOs1FyL7L21S': 'file_storage/call_lwbNDmgVITWaBOs1FyL7L21S.json', 'var_call_FIcFshle7x0Wv4IUBDg7ns0I': [], 'var_call_Pq8anEwyVn3RgRhcobvIh6nq': 'file_storage/call_Pq8anEwyVn3RgRhcobvIh6nq.json'}

exec(code, env_args)
