code = """import json, re
import pandas as pd

path = var_call_nKcqwc5ja4sXUlqRqUJJ6uzV
with open(path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

path2 = var_call_GZmXkPR1bvCkVUon7p1X0fCh
with open(path2, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def is_food_domain(text):
    if not text:
        return False
    t = text.lower()
    if re.search(r'\bdomain\b\s*[:=]\s*\[?[^\r\n\]]*\bfood\b', t):
        return True
    if re.search(r'\bdomains\b\s*[:=]\s*\[?[^\r\n\]]*\bfood\b', t):
        return True
    head = t[:5000]
    if re.search(r'\bfood\s+(journal|journaling|tracker|tracking|log|logging)\b', head):
        return True
    if re.search(r'\bnutrition\b', head) and re.search(r'\bfood\b', head):
        return True
    return False

food_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if is_food_domain(d.get('text','')):
        food_titles.append(title)

food_titles = sorted(set(food_titles))
df_food = pd.DataFrame({'title': food_titles})
merged = df_food.merge(df_cit, on='title', how='left')
merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
ans = int(merged['total_citations'].sum())

print('__RESULT__:')
print(json.dumps({'total_citation_count_food_domain': ans, 'num_food_papers': len(food_titles), 'num_food_papers_with_citations': int((merged['total_citations']>0).sum())}))"""

env_args = {'var_call_nKcqwc5ja4sXUlqRqUJJ6uzV': 'file_storage/call_nKcqwc5ja4sXUlqRqUJJ6uzV.json', 'var_call_5d4tQE2oAez2ePpXlIQytLc6': [], 'var_call_GZmXkPR1bvCkVUon7p1X0fCh': 'file_storage/call_GZmXkPR1bvCkVUon7p1X0fCh.json'}

exec(code, env_args)
