code = """import json, pandas as pd

# Load mongo filenames
mongo_src = var_call_N7Bi5QSbCwGLQFFpgsBxg4XE
if isinstance(mongo_src, str):
    with open(mongo_src, 'r', encoding='utf-8') as f:
        mongo_rows = json.load(f)
else:
    mongo_rows = mongo_src

# Load citations
cit_src = var_call_5TrZNhVbPoRhuTQHKM1PImWY
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit_rows = json.load(f)
else:
    cit_rows = cit_src

# Determine 'food' domain papers by filename containing 'food' (case-insensitive)
food_titles = set()
for r in mongo_rows:
    fn = r.get('filename','')
    if isinstance(fn, str) and 'food' in fn.lower():
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.add(title)

# Sum citations for those titles
cit_total = 0
for r in cit_rows:
    t = r.get('title')
    if t in food_titles:
        try:
            cit_total += int(r.get('citation_count', 0))
        except Exception:
            pass

out = {"total_citation_count_food_domain": cit_total, "food_paper_count": len(food_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_N7Bi5QSbCwGLQFFpgsBxg4XE': 'file_storage/call_N7Bi5QSbCwGLQFFpgsBxg4XE.json', 'var_call_5TrZNhVbPoRhuTQHKM1PImWY': 'file_storage/call_5TrZNhVbPoRhuTQHKM1PImWY.json'}

exec(code, env_args)
