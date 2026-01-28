code = """import json, pandas as pd

def load(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_files = load(var_call_cySkbDI335YfmtjV42jVnh7r)
cit = load(var_call_nE3ubpRMZ2wKpZdUBgxE96C1)

# Identify food-domain papers by filename/title heuristic (dataset doesn't provide explicit domain field)
# Use keyword matching in title/filename.
food_keywords = [
    'food', 'diet', 'eating', 'meal', 'nutrition', 'calorie', 'calories', 'myfitnesspal', 'cook', 'cooking',
    'grocery', 'snack', 'restaurant', 'recipe', 'lunch', 'dinner', 'breakfast', 'chocolate'
]

def is_food(name):
    s = name.lower()
    return any(k in s for k in food_keywords)

food_titles = set()
for r in paper_files:
    fn = r.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if is_food(title):
        food_titles.add(title)

# Sum citations for those titles
cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

food_cit_total = int(cit_df[cit_df['title'].isin(food_titles)]['citation_count'].sum())

out = {
    'total_citation_count_food_domain': food_cit_total,
    'matched_food_papers': len(food_titles)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cySkbDI335YfmtjV42jVnh7r': 'file_storage/call_cySkbDI335YfmtjV42jVnh7r.json', 'var_call_nE3ubpRMZ2wKpZdUBgxE96C1': 'file_storage/call_nE3ubpRMZ2wKpZdUBgxE96C1.json'}

exec(code, env_args)
