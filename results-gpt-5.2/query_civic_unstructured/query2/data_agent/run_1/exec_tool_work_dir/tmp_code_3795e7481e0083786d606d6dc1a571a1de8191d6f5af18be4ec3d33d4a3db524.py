code = """import json

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_KYRK4xUSAtxEAJdgI1BrqhqV)
fund = load_json_maybe(var_call_5wBIUvFbVq6D7BGzPAvwAJbx)

fund_map = {}
for r in fund:
    pn = (r.get('Project_Name') or '').strip()
    if not pn:
        continue
    try:
        amt_i = int(r.get('total_amount'))
    except Exception:
        try:
            amt_i = int(float(r.get('total_amount')))
        except Exception:
            continue
    fund_map[pn] = fund_map.get(pn, 0) + amt_i

text_all = "\n".join([d.get('text','') for d in docs if d.get('text')])

import re
pattern = r'(?im)^(?P<name>.+?)\s*\n(?:.*\n){0,15}.*Construction was completed[^\n]*2022'
pat = re.compile(pattern)

names = []
for m in pat.finditer(text_all):
    name = m.group('name').strip()
    if len(name) < 3:
        continue
    low = name.lower()
    if low.startswith('updates') or low.startswith('project schedule') or low.startswith('capital improvement projects') or low.startswith('disaster recovery projects') or low.startswith('discussion'):
        continue
    if re.search(r'\b(park|playground|bluffs)\b', name, flags=re.I):
        names.append(name)

uniq=[]; seen=set()
for n in names:
    if n not in seen:
        seen.add(n)
        uniq.append(n)

total = sum(int(fund_map.get(n,0)) for n in uniq)

print('__RESULT__:')
print(json.dumps({'total': total, 'projects': uniq}))"""

env_args = {'var_call_4PG5K1JFOxGDnVSmjHEy9scy': ['Funding'], 'var_call_LZiL1tp6SEIuXVpXZIGyQBMT': ['civic_docs'], 'var_call_KYRK4xUSAtxEAJdgI1BrqhqV': 'file_storage/call_KYRK4xUSAtxEAJdgI1BrqhqV.json', 'var_call_5wBIUvFbVq6D7BGzPAvwAJbx': 'file_storage/call_5wBIUvFbVq6D7BGzPAvwAJbx.json'}

exec(code, env_args)
