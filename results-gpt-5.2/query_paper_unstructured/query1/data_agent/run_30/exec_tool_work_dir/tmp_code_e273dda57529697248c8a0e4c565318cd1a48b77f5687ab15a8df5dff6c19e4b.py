code = """import json, pandas as pd

def load_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

paper_files = load_maybe(var_call_Jo3BE8G2N4Sd8vdJ1eRFeyWp)
cit_rows = load_maybe(var_call_2XT45aWgjfLEf46ncj3xhbso)

# Identify 'food' domain papers by filename/title heuristic (contains 'food' case-insensitive)
food_titles = []
for r in paper_files:
    fn = r.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if 'food' in title.lower():
        food_titles.append(title)
food_set = set(food_titles)

# Sum citations for those titles
# citation_count sometimes string

total = 0
for r in cit_rows:
    if r.get('title') in food_set:
        try:
            total += int(r.get('citation_count') or 0)
        except Exception:
            pass

out = {
    'total_citation_count_food_domain': total,
    'food_domain_paper_count_matched_by_title_contains_food': len(food_set)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Jo3BE8G2N4Sd8vdJ1eRFeyWp': 'file_storage/call_Jo3BE8G2N4Sd8vdJ1eRFeyWp.json', 'var_call_2XT45aWgjfLEf46ncj3xhbso': 'file_storage/call_2XT45aWgjfLEf46ncj3xhbso.json'}

exec(code, env_args)
