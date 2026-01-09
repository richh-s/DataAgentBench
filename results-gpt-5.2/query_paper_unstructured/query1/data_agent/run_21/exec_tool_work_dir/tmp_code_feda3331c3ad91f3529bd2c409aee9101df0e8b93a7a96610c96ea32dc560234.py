code = """import json, pandas as pd, re

# load filenames
fn_src = var_call_FnHGRr9GVjUgmqk0dFZvaqZG
if isinstance(fn_src, str):
    with open(fn_src, 'r', encoding='utf-8') as f:
        fn_records = json.load(f)
else:
    fn_records = fn_src

cit_src = var_call_bfAswxZvcJcyOXDxpJBHbETL
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit_records = json.load(f)
else:
    cit_records = cit_src

# infer 'food' domain by filename containing 'food'
food_titles = set()
for r in fn_records:
    fn = r.get('filename','')
    title = re.sub(r'\.txt$', '', fn)
    if 'food' in title.lower():
        food_titles.add(title)

# sum citations for those titles
_total = 0
for r in cit_records:
    title = r.get('title')
    if title in food_titles:
        try:
            _total += int(r.get('citation_count') or 0)
        except Exception:
            pass

out = {"total_citation_count_food_domain": _total, "num_food_papers_matched": len(food_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FnHGRr9GVjUgmqk0dFZvaqZG': 'file_storage/call_FnHGRr9GVjUgmqk0dFZvaqZG.json', 'var_call_bfAswxZvcJcyOXDxpJBHbETL': 'file_storage/call_bfAswxZvcJcyOXDxpJBHbETL.json'}

exec(code, env_args)
