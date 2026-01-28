code = """import json, re
import pandas as pd

# Load mongo results (may be a path)
raw = var_call_k2pkTZolnzHBVxT43KDhyu_H0 if 'var_call_k2pkTZolnzHBVxT43KDhyu_H0' in globals() else var_call_k2pkTZolnzHBVxT43KDhyuH0
if isinstance(raw, str) and raw.endswith('.json'):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

food_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r'\bdomain\s*:\s*food\b', text, flags=re.I):
        food_titles.append(title)

# unique
food_titles = sorted(set(food_titles))
print('__RESULT__:')
print(json.dumps({'food_titles': food_titles, 'count': len(food_titles)}))"""

env_args = {'var_call_L5F3slNGQ7LAgAufGKswxWaC': [], 'var_call_k2pkTZolnzHBVxT43KDhyuH0': 'file_storage/call_k2pkTZolnzHBVxT43KDhyuH0.json'}

exec(code, env_args)
