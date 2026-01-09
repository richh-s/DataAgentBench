code = """import json, pandas as pd

# Load filenames
fn_src = var_call_ubFjNAovc68wQQhhg6caJBKu
if isinstance(fn_src, str) and fn_src.endswith('.json'):
    with open(fn_src, 'r', encoding='utf-8') as f:
        fn_records = json.load(f)
else:
    fn_records = fn_src

# Load citations
cit_src = var_call_R84MGMHhD8c10ypMOBdwT3Th
if isinstance(cit_src, str) and cit_src.endswith('.json'):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit_records = json.load(f)
else:
    cit_records = cit_src

# Identify food-domain papers by filename containing 'food'
food_titles = set()
for r in fn_records:
    fn = (r.get('filename') or '')
    if 'food' in fn.lower():
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.add(title)

# Sum citation counts for those titles

total = 0
for r in cit_records:
    title = r.get('title')
    if title in food_titles:
        try:
            total += int(r.get('citation_count') or 0)
        except Exception:
            pass

out = {"food_domain_paper_count": len(food_titles), "total_citation_count": total}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ubFjNAovc68wQQhhg6caJBKu': 'file_storage/call_ubFjNAovc68wQQhhg6caJBKu.json', 'var_call_R84MGMHhD8c10ypMOBdwT3Th': 'file_storage/call_R84MGMHhD8c10ypMOBdwT3Th.json'}

exec(code, env_args)
