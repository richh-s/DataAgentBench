code = """import json

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

fund = load_json_maybe(var_call_dI2tSwd00uIHGyclnoLvnw7a)

# Park-related projects completed in 2022 found in docs (construction completed Nov 2022)
projects = [
    'Bluffs Park Shade Structure',
]

fund_map = {r['Project_Name']: int(float(r['total_amount'])) for r in fund}

total = sum(fund_map.get(p,0) for p in projects)

out = {'total_funding': total, 'projects': projects}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DIHXHl764GTqjmunV9ZlinMu': 'file_storage/call_DIHXHl764GTqjmunV9ZlinMu.json', 'var_call_dI2tSwd00uIHGyclnoLvnw7a': 'file_storage/call_dI2tSwd00uIHGyclnoLvnw7a.json'}

exec(code, env_args)
