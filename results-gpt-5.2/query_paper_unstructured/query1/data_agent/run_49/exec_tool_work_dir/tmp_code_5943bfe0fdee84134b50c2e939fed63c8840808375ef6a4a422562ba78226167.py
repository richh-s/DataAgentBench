code = """import json, re, pandas as pd

def load_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

paper_files = load_maybe(var_call_Xw2cpUU1GFrQmtYMK77F5ZjK)
cit_totals = load_maybe(var_call_zIU5ilEKij5KQg2wyVnBp5LC)

# Identify 'food' domain papers by filename heuristics (contains food/nutrition/diet/eating)
food_pat = re.compile(r'(food|nutrition|diet|eating|meal|calorie|myfitnesspal)', re.I)
food_titles = []
for rec in paper_files:
    fn = rec.get('filename','')
    title = re.sub(r'\.txt$','',fn)
    if food_pat.search(title):
        food_titles.append(title)
food_titles_set = set(food_titles)

# Sum citations for those titles
# cit_totals has total_citations as str in preview; cast to int
sum_cites = 0
matched = 0
for rec in cit_totals:
    t = rec.get('title')
    if t in food_titles_set:
        try:
            sum_cites += int(rec.get('total_citations') or 0)
        except Exception:
            sum_cites += 0
        matched += 1

out = {"total_citation_count_food_domain": sum_cites, "matched_papers": matched, "identified_food_papers": len(food_titles_set)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Xw2cpUU1GFrQmtYMK77F5ZjK': 'file_storage/call_Xw2cpUU1GFrQmtYMK77F5ZjK.json', 'var_call_zIU5ilEKij5KQg2wyVnBp5LC': 'file_storage/call_zIU5ilEKij5KQg2wyVnBp5LC.json', 'var_call_XNRNkzTWobJcfKh5FeaNZ8xB': []}

exec(code, env_args)
