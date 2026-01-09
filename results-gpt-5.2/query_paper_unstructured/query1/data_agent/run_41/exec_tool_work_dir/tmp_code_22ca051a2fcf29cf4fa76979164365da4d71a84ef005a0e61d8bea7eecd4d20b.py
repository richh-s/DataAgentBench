code = """import json, re, pandas as pd

def load_mongo_res(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_mongo_res(var_call_FcGorrHnDakgfgCJfTgwIs8B)

# Determine food-domain papers by substring match in text
food_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r'\bfood\b', text, flags=re.IGNORECASE):
        food_titles.add(title)

# citations
cits = load_mongo_res(var_call_0wc67iTtBfUDtPhBJ8n33vYn)
df = pd.DataFrame(cits)
if df.empty:
    total = 0
else:
    df['citation_count'] = pd.to_numeric(df['citation_count'], errors='coerce').fillna(0).astype(int)
    df_food = df[df['title'].isin(food_titles)]
    total = int(df_food['citation_count'].sum())

print('__RESULT__:')
print(json.dumps({'total_citation_count_food_domain': total, 'food_paper_count_matched_titles': len(food_titles)}))"""

env_args = {'var_call_FcGorrHnDakgfgCJfTgwIs8B': 'file_storage/call_FcGorrHnDakgfgCJfTgwIs8B.json', 'var_call_0wc67iTtBfUDtPhBJ8n33vYn': 'file_storage/call_0wc67iTtBfUDtPhBJ8n33vYn.json'}

exec(code, env_args)
