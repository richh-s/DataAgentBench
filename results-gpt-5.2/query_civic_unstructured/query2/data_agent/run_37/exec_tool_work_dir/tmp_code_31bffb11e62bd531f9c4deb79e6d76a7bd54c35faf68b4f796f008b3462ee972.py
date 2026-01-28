code = """import json

def load_maybe_path(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_maybe_path(var_call_PSEDl1KcedE8d42keS4hSf4K)
fund = load_maybe_path(var_call_mHowZH49DE3gHNi1DCBbZdvp)

fund_map = {r['Project_Name']: int(r['total_amount']) for r in fund}

park_projects = [p for p in fund_map.keys() if 'park' in p.lower()]
park_completed_2022 = set()

for d in docs:
    txt = (d.get('text') or '')
    low = txt.lower()
    if 'completed' not in low or '2022' not in low or 'park' not in low:
        continue
    for p in park_projects:
        if p in txt:
            park_completed_2022.add(p)

projects = sorted(park_completed_2022)

total = sum(fund_map.get(p, 0) for p in projects)

out = {'total_funding': total, 'projects': projects, 'project_funding': [{'Project_Name': p, 'total_amount': fund_map.get(p,0)} for p in projects]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PSEDl1KcedE8d42keS4hSf4K': 'file_storage/call_PSEDl1KcedE8d42keS4hSf4K.json', 'var_call_mHowZH49DE3gHNi1DCBbZdvp': 'file_storage/call_mHowZH49DE3gHNi1DCBbZdvp.json'}

exec(code, env_args)
