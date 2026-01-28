code = """import json, pandas as pd

def load_maybe_path(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_files = load_maybe_path(var_call_YKvWeB1IkD8v5uEE6keSgc0j)
cit_rows = load_maybe_path(var_call_VALFLNgz5ysZ7XxkE3Wx2dq2)

# Infer 'food' domain papers by filename/title containing 'food' (case-insensitive)
food_titles = set()
for r in paper_files:
    fn = r.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if 'food' in title.lower():
        food_titles.add(title)

# Sum citations for those titles
cit_total = 0
for r in cit_rows:
    title = r.get('title')
    if title in food_titles:
        try:
            cit_total += int(r.get('citation_count', 0))
        except Exception:
            pass

out = {"total_citation_count_food_domain": cit_total, "matched_food_papers": len(food_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YKvWeB1IkD8v5uEE6keSgc0j': 'file_storage/call_YKvWeB1IkD8v5uEE6keSgc0j.json', 'var_call_VALFLNgz5ysZ7XxkE3Wx2dq2': 'file_storage/call_VALFLNgz5ysZ7XxkE3Wx2dq2.json'}

exec(code, env_args)
