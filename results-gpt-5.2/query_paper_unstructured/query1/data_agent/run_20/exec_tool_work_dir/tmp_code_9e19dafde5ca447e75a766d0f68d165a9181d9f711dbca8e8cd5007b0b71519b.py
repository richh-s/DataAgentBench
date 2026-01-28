code = """import json, pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

paper_files = load_records(var_call_z0zsoifcc1r8Q8fWMWYrSueg)
cit_totals = load_records(var_call_e9yGhXUKD7JPvc2L8XV1DOrd)

# Identify food-domain papers by filename containing 'food' (case-insensitive)
food_titles = []
for r in paper_files:
    fn = r.get('filename','')
    if 'food' in fn.lower():
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.append(title)

food_set = set(food_titles)

total = 0
missing = 0
for r in cit_totals:
    title = r.get('title')
    if title in food_set:
        try:
            total += int(r.get('total_citations'))
        except Exception:
            pass

print('__RESULT__:')
print(json.dumps({'total_citations_food_domain': total, 'food_paper_count': len(food_set)}))"""

env_args = {'var_call_z0zsoifcc1r8Q8fWMWYrSueg': 'file_storage/call_z0zsoifcc1r8Q8fWMWYrSueg.json', 'var_call_e9yGhXUKD7JPvc2L8XV1DOrd': 'file_storage/call_e9yGhXUKD7JPvc2L8XV1DOrd.json'}

exec(code, env_args)
