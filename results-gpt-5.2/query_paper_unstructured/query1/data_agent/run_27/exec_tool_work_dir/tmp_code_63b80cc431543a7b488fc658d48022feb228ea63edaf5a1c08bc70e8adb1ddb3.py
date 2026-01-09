code = """import json, re
import pandas as pd

# load citations per title
path = var_call_U9tVTo2jLU5qdN1r09KpHftA
with open(path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

# load mongo docs sample containing 'food' (but use filename list from these 200)
path2 = var_call_NuEhPrMYndX5k5hAZsoOyHoI
with open(path2, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Heuristic: domain 'food' if text contains 'food journal' or 'diet' or 'nutrition' and NOT just citations.
# However dataset likely includes explicit domain labels elsewhere; unavailable. We'll use title keyword matching for food domain.
food_title_kw = re.compile(r"\b(food|diet|nutrition|eating|meal|calorie|diabetes)\b", re.I)

food_titles = set()
for d in docs:
    title = d['filename'].rsplit('.txt',1)[0]
    if food_title_kw.search(title):
        food_titles.add(title)

# compute total citations across all years for these titles
cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'])
food_total = int(cit_df[cit_df['title'].isin(food_titles)]['total_citations'].sum())

out = {"food_titles_count": len(food_titles), "total_citations": food_total, "food_titles": sorted(list(food_titles))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_U9tVTo2jLU5qdN1r09KpHftA': 'file_storage/call_U9tVTo2jLU5qdN1r09KpHftA.json', 'var_call_ZGWr1343JJecLzhR4wHHKG9i': [], 'var_call_NuEhPrMYndX5k5hAZsoOyHoI': 'file_storage/call_NuEhPrMYndX5k5hAZsoOyHoI.json'}

exec(code, env_args)
