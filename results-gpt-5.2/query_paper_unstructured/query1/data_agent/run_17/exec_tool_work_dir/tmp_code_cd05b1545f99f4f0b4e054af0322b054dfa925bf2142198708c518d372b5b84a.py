code = """import json, re
import pandas as pd

# load citations
path = var_call_PWlzJWbFK6Uq6ImdMzHSOCWD
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

df_cit = pd.DataFrame(citations)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# load candidate docs with 'food'
path2 = var_call_Ur4y8kVTPHCCgldYqXDgvko7
with open(path2, 'r', encoding='utf-8') as f:
    docs = json.load(f)

food_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r'(?i)domain\s*:\s*[^\n]*\bfood\b', text) or re.search(r'(?i)\bfood\s+domain\b', text):
        food_titles.append(title)

food_titles = sorted(set(food_titles))

total = int(df_cit[df_cit['title'].isin(food_titles)]['citation_count'].sum()) if food_titles else 0

out = {'total_citation_count_food_domain': total, 'num_food_domain_papers_matched': len(food_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PWlzJWbFK6Uq6ImdMzHSOCWD': 'file_storage/call_PWlzJWbFK6Uq6ImdMzHSOCWD.json', 'var_call_2fEa5cABVigGalzcOhezYFWK': [], 'var_call_Ur4y8kVTPHCCgldYqXDgvko7': 'file_storage/call_Ur4y8kVTPHCCgldYqXDgvko7.json'}

exec(code, env_args)
