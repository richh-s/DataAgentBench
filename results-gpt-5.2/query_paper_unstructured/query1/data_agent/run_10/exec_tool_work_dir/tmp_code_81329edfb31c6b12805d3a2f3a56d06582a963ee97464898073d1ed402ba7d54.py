code = """import json, re, pandas as pd

docs_path = var_call_9QKvaQJOGXhlLo3iNYrBSvU5
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Since domain isn't explicitly tagged, approximate: papers whose full text contains food/nutrition/eating terms.
# Use conservative set of keywords.
kw_re = re.compile(r'\b(food|foods|eating|diet|dietary|nutrition|nutritional|meal|calorie|calories|snack|snacks|grocery|groceries|restaurant|restaurants|cook|cooking|recipe|recipes|food\s+journal|food\s+tracking|nutrition\s+tracking)\b', re.IGNORECASE)

food_titles = set()
for d in docs:
    text = (d.get('text','') or '')
    if kw_re.search(text):
        fn = d.get('filename','')
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.add(title)

cit_path = var_call_IBbYqorI2JWVGqgFc0ClSigv
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

food_total = int(cit_df[cit_df['title'].isin(food_titles)]['total_citations'].sum())

print('__RESULT__:')
print(json.dumps({'total_citation_count_food_domain': food_total, 'num_food_papers_heuristic': len(food_titles)}))"""

env_args = {'var_call_IBbYqorI2JWVGqgFc0ClSigv': 'file_storage/call_IBbYqorI2JWVGqgFc0ClSigv.json', 'var_call_9QKvaQJOGXhlLo3iNYrBSvU5': 'file_storage/call_9QKvaQJOGXhlLo3iNYrBSvU5.json', 'var_call_GooaeeZSt0aAQyphRzwDzMpw': {'total_citation_count_food_domain': 0, 'num_food_papers_matched': 0}}

exec(code, env_args)
