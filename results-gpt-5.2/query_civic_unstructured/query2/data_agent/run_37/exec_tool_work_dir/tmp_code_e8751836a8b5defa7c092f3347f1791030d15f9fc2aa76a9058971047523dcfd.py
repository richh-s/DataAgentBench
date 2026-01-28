code = """import json, re

def load_maybe_path(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_maybe_path(var_call_PSEDl1KcedE8d42keS4hSf4K)
fund = load_maybe_path(var_call_mHowZH49DE3gHNi1DCBbZdvp)

fund_map = {r['Project_Name']: int(r['total_amount']) for r in fund}

park_completed_2022 = set()

for d in docs:
    text = d.get('text','') or ''
    if 'park' not in text.lower():
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        for pname in fund_map.keys():
            if re.search(r'park', pname, flags=re.I) and pname in line:
                window = "\n".join(lines[max(0,i-4):min(len(lines), i+6)])
                wlow = window.lower()
                if ('completed' in wlow) and ('2022' in wlow):
                    park_completed_2022.add(pname)

if not park_completed_2022:
    patterns = [re.escape(pname) for pname in fund_map.keys() if re.search(r'park', pname, flags=re.I)]
    if patterns:
        bigpat = re.compile(r'('+'|'.join(patterns)+r')(.{0,200}completed.{0,200}2022|.{0,200}2022.{0,200}completed)', re.I|re.S)
        for d in docs:
            m = bigpat.search(d.get('text','') or '')
            if m:
                park_completed_2022.add(m.group(1))

projects = sorted(park_completed_2022)

total = sum(fund_map.get(p,0) for p in projects)

out = {
    'total_funding': total,
    'projects': projects,
    'project_funding': [{'Project_Name': p, 'total_amount': fund_map.get(p,0)} for p in projects]
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PSEDl1KcedE8d42keS4hSf4K': 'file_storage/call_PSEDl1KcedE8d42keS4hSf4K.json', 'var_call_mHowZH49DE3gHNi1DCBbZdvp': 'file_storage/call_mHowZH49DE3gHNi1DCBbZdvp.json'}

exec(code, env_args)
