code = """import json, re

def load_maybe_path(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_maybe_path(var_call_PSEDl1KcedE8d42keS4hSf4K)
fund = load_maybe_path(var_call_mHowZH49DE3gHNi1DCBbZdvp)

fund_map = {r['Project_Name']: int(r['total_amount']) for r in fund}

# Use regex approach only to avoid multiline quoting issues
patterns = [re.escape(p) for p in fund_map.keys() if re.search(r'park', p, flags=re.I)]
park_completed_2022 = set()

if patterns:
    alt = '|'.join(patterns)
    # look for project name then nearby 'completed' and '2022'
    bigpat = re.compile(r'(' + alt + r')(?:(?!\n\n).){0,400}?completed(?:(?!\n\n).){0,400}?2022|(' + alt + r')(?:(?!\n\n).){0,400}?2022(?:(?!\n\n).){0,400}?completed', re.I|re.S)
    for d in docs:
        txt = d.get('text','') or ''
        for m in bigpat.finditer(txt):
            # m.group(1) or m.group(2)
            name = m.group(1) if m.group(1) else m.group(2)
            if name:
                park_completed_2022.add(name)

projects = sorted(park_completed_2022)

total = sum(fund_map.get(p,0) for p in projects)

out = {'total_funding': total, 'projects': projects, 'project_funding': [{'Project_Name':p,'total_amount':fund_map.get(p,0)} for p in projects]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PSEDl1KcedE8d42keS4hSf4K': 'file_storage/call_PSEDl1KcedE8d42keS4hSf4K.json', 'var_call_mHowZH49DE3gHNi1DCBbZdvp': 'file_storage/call_mHowZH49DE3gHNi1DCBbZdvp.json'}

exec(code, env_args)
