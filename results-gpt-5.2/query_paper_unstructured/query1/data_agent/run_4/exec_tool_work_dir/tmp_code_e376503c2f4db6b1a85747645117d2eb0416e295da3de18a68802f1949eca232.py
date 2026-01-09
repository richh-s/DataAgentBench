code = """import json, pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_files = load_records(var_call_lJL9ktrDgMkiNIm3eR3wFRX5)
citations = load_records(var_call_kqLbaIJddm0ocjGtCZL53ZrZ)

# Identify 'food' domain papers via filename/title containing food/journal/eat/diet/nutrition (best-effort given only filenames available)
food_keywords = ['food', 'eat', 'diet', 'nutrition', 'meal', 'calorie', 'myfitnesspal', 'journaling', 'journal']

food_titles = set()
for rec in paper_files:
    fn = rec.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    t_low = title.lower()
    if any(k in t_low for k in food_keywords):
        food_titles.add(title)

cit_df = pd.DataFrame(citations)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

food_cit_total = int(cit_df[cit_df['title'].isin(food_titles)]['citation_count'].sum()) if not cit_df.empty else 0

out = {
    'total_citation_count_food_domain': food_cit_total,
    'matched_food_paper_count': int(len(food_titles)),
    'method_note': 'Domain inferred from paper filename keywords because explicit domain field is not present in the paper_docs collection.'
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lJL9ktrDgMkiNIm3eR3wFRX5': 'file_storage/call_lJL9ktrDgMkiNIm3eR3wFRX5.json', 'var_call_kqLbaIJddm0ocjGtCZL53ZrZ': 'file_storage/call_kqLbaIJddm0ocjGtCZL53ZrZ.json'}

exec(code, env_args)
