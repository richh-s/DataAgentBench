code = """import json, pandas as pd, re

# Load citations (may be file path)
cit_var = var_call_Vqy4Fmxf4oirwPb1Gcp0fCbK
if isinstance(cit_var, str):
    with open(cit_var, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_var

# Load paper docs text to classify domain=food
pd_var = var_call_bdDFjy0diCigKQHTZYmNikO2
if isinstance(pd_var, str):
    with open(pd_var, 'r', encoding='utf-8') as f:
        paper_docs = json.load(f)
else:
    paper_docs = pd_var

# Build set of titles in food domain using heuristic keyword search
food_titles = set()
food_re = re.compile(r'\b(food|diet|eating|meal|nutrition|calorie|calories|myfitnesspal|food journal|food journaling)\b', re.IGNORECASE)
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    # classify food domain if title or text contains food keywords and not just references to food as an example? keep simple
    if food_re.search(title) or food_re.search(text):
        food_titles.add(title)

# Sum citations for those titles

total = 0
for r in citations:
    title = r.get('title')
    if title in food_titles:
        try:
            total += int(r.get('citation_count',0))
        except Exception:
            pass

print('__RESULT__:')
print(json.dumps({'total_citation_count_food_domain': total, 'food_paper_count': len(food_titles)}))"""

env_args = {'var_call_Vqy4Fmxf4oirwPb1Gcp0fCbK': 'file_storage/call_Vqy4Fmxf4oirwPb1Gcp0fCbK.json', 'var_call_fHG9HzygcJwNedr1XK4wg67i': 'file_storage/call_fHG9HzygcJwNedr1XK4wg67i.json', 'var_call_bdDFjy0diCigKQHTZYmNikO2': 'file_storage/call_bdDFjy0diCigKQHTZYmNikO2.json'}

exec(code, env_args)
