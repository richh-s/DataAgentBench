code = """import json, pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

paper_files = load_records(var_call_DGYpqSaloNbiNvPtEB5BsYIJ)
# domain heuristic: filename/title contains food-related terms
food_terms = [
    'food','eat','eating','diet','dietary','nutrition','nutritional','meal','meals','snack','snacks',
    'grocery','groceries','cooking','cook','recipe','recipes','kitchen','calorie','calories',
    'myfitnesspal','journal','journaling'
]

def is_food_title(title):
    t = (title or '').lower()
    return any(term in t for term in food_terms)

food_titles = set()
for r in paper_files:
    fn = r.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if is_food_title(title):
        food_titles.add(title)

cit = load_records(var_call_lVUZ1wPWAuC5hHEyoq8d2fUn)
df = pd.DataFrame(cit)
if df.empty:
    total = 0
else:
    df['citation_count'] = pd.to_numeric(df['citation_count'], errors='coerce').fillna(0).astype(int)
    total = int(df[df['title'].isin(food_titles)]['citation_count'].sum())

out = json.dumps({"total_citation_count_food_domain": total, "matched_food_papers": len(food_titles)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_DGYpqSaloNbiNvPtEB5BsYIJ': 'file_storage/call_DGYpqSaloNbiNvPtEB5BsYIJ.json', 'var_call_lVUZ1wPWAuC5hHEyoq8d2fUn': 'file_storage/call_lVUZ1wPWAuC5hHEyoq8d2fUn.json'}

exec(code, env_args)
