code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

civic = load_json_maybe(var_call_DIHXHl764GTqjmunV9ZlinMu)
fund = load_json_maybe(var_call_dI2tSwd00uIHGyclnoLvnw7a)

fund_map = {r['Project_Name']: float(r['total_amount']) for r in fund}

project_completed_2022 = set()

for doc in civic:
    text = doc.get('text','')
    if text is None:
        continue
    text = text.replace(chr(0), '')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if ln in fund_map:
            window = '\n'.join(lines[i:i+40])
            if re.search(r'(Construction was completed|Complete Construction|completed)[^\n]*2022', window, flags=re.IGNORECASE):
                name_l = ln.lower()
                if ('park' in name_l) or ('playground' in name_l):
                    project_completed_2022.add(ln)

sum_amt = sum(fund_map.get(p,0) for p in project_completed_2022)

out = {'total_funding': int(sum_amt) if float(sum_amt).is_integer() else sum_amt,
       'projects': sorted(project_completed_2022)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DIHXHl764GTqjmunV9ZlinMu': 'file_storage/call_DIHXHl764GTqjmunV9ZlinMu.json', 'var_call_dI2tSwd00uIHGyclnoLvnw7a': 'file_storage/call_dI2tSwd00uIHGyclnoLvnw7a.json'}

exec(code, env_args)
