code = """import json, re
import pandas as pd

cit_path = var_call_ElALRIP08rKdUErJX7TtSVr1
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'])

docs_path = var_call_1BmIl93wnjxQoHKvyKoJcn3H
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def is_food_domain(text: str) -> bool:
    if not isinstance(text, str):
        return False
    t = text.lower()
    if re.search(r'domain\s*:\s*\[?[^\n\r\]]*\bfood\b', t):
        return True
    if re.search(r'\bfood\s+(journaling|journal|logging|log|tracker|tracking|diary)\b', t):
        return True
    if re.search(r'\bnutrition\s+(tracking|log|logging|diary|journal|journaling)\b', t):
        return True
    if re.search(r'\bhealthy\s+eating\b', t):
        return True
    if re.search(r'\bdietary\s+self-?tracking\b', t):
        return True
    if re.search(r'\bcalorie\s+tracking\b', t):
        return True
    if re.search(r'\bmeal\s+tracking\b', t):
        return True
    return False

food_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if isinstance(fn,str) and fn.lower().endswith('.txt') else fn
    if is_food_domain(d.get('text','')):
        food_titles.append(title)

food_titles = sorted(set(food_titles))

df_food = pd.DataFrame({'title': food_titles})
merged = df_food.merge(df_cit, on='title', how='left')
merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)

total = int(merged['total_citations'].sum())

out = {
    'total_citation_count_food_domain': total,
    'matched_food_paper_count': int(len(merged)),
    'titles_missing_citations_count': int((merged['total_citations']==0).sum())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ElALRIP08rKdUErJX7TtSVr1': 'file_storage/call_ElALRIP08rKdUErJX7TtSVr1.json', 'var_call_RXQx55zXNxDgAcxFt79e3Mme': [], 'var_call_1BmIl93wnjxQoHKvyKoJcn3H': 'file_storage/call_1BmIl93wnjxQoHKvyKoJcn3H.json'}

exec(code, env_args)
