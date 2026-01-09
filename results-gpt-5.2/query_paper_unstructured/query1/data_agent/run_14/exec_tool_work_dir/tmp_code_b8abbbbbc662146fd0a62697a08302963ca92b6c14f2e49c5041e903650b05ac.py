code = """import json

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cit = load_records(var_call_gcW4Au8ZEukvPGrEl7qmZRWe)
docs = load_records(var_call_EZMHpBljyH1P21PpCWs72I2F)

food_titles = set()
for d in docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if 'food' in title.lower():
        food_titles.add(title)

s = 0
for r in cit:
    if r.get('title') in food_titles:
        try:
            s += int(r.get('citation_count') or 0)
        except Exception:
            pass

out = json.dumps({'total_citation_count_food_domain': s, 'num_food_papers_matched': len(food_titles)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_gcW4Au8ZEukvPGrEl7qmZRWe': 'file_storage/call_gcW4Au8ZEukvPGrEl7qmZRWe.json', 'var_call_ibszYpDVq4GuzR0Dc2duHohu': 'file_storage/call_ibszYpDVq4GuzR0Dc2duHohu.json', 'var_call_EZMHpBljyH1P21PpCWs72I2F': 'file_storage/call_EZMHpBljyH1P21PpCWs72I2F.json'}

exec(code, env_args)
