code = """import json, pandas as pd

# load filenames
fn_src = var_call_IqDnD0s8e2WhiN2KUv2ik7As
if isinstance(fn_src, str):
    with open(fn_src, 'r', encoding='utf-8') as f:
        filenames = json.load(f)
else:
    filenames = fn_src

cit_src = var_call_C1cprDYxmSF74gZ0iJ3afDx0
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cit_src

def title_from_filename(fn):
    if fn is None:
        return None
    if fn.lower().endswith('.txt'):
        return fn[:-4]
    return fn

food_titles = set()
for r in filenames:
    fn = r.get('filename')
    if not fn:
        continue
    if 'food' in fn.lower():
        food_titles.add(title_from_filename(fn))

# sum citations for those titles
# total_citations may come back as string
food_total = 0
for r in cits:
    t = r.get('title')
    if t in food_titles:
        try:
            food_total += int(r.get('total_citations') or 0)
        except Exception:
            # try float
            try:
                food_total += int(float(r.get('total_citations')))
            except Exception:
                pass

out = {"total_citation_count_food_domain": food_total, "matched_papers": len(food_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_IqDnD0s8e2WhiN2KUv2ik7As': 'file_storage/call_IqDnD0s8e2WhiN2KUv2ik7As.json', 'var_call_C1cprDYxmSF74gZ0iJ3afDx0': 'file_storage/call_C1cprDYxmSF74gZ0iJ3afDx0.json'}

exec(code, env_args)
