code = """import json, pandas as pd, re

# Load mongo results
path = var_call_G0Sanghz1o6NZX4lFa0Edq73
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

food_titles = []
for d in docs:
    fn = d.get('filename','')
    text = d.get('text','') or ''
    # domain tag detection
    if re.search(r'(?im)^\s*domain\s*:\s*.*\bfood\b', text):
        food_titles.append(fn[:-4] if fn.lower().endswith('.txt') else fn)
    elif re.search(r'(?im)^\s*domains\s*:\s*.*\bfood\b', text):
        food_titles.append(fn[:-4] if fn.lower().endswith('.txt') else fn)
    elif re.search(r'(?i)\"domain\"\s*:\s*\"food\"', text):
        food_titles.append(fn[:-4] if fn.lower().endswith('.txt') else fn)
    elif re.search(r'(?i)\"domains\"\s*:\s*\[.*?\bfood\b.*?\]', text, flags=re.S):
        food_titles.append(fn[:-4] if fn.lower().endswith('.txt') else fn)

# unique
food_titles = sorted(set(food_titles))

print('__RESULT__:')
print(json.dumps({'food_titles': food_titles, 'n_food_titles': len(food_titles)}))"""

env_args = {'var_call_G0Sanghz1o6NZX4lFa0Edq73': 'file_storage/call_G0Sanghz1o6NZX4lFa0Edq73.json'}

exec(code, env_args)
