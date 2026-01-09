code = """import json, re
import pandas as pd

cit_path = var_call_OIH4ZkLpKsdNZP0Jje4SjSma
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)


docs_path = var_call_cK1DMFbC05HgX1efYgTXBowY
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)

if df_docs.empty or df_cit.empty:
    total = 0
else:
    df_docs['title'] = df_docs['filename'].str.replace(r'\\.txt$', '', regex=True)
    pat = re.compile(r'domain\\s*:\\s*[^\\n\\r]*\\bfood\\b', re.IGNORECASE)
    df_docs['is_food'] = df_docs['text'].apply(lambda t: bool(pat.search(t or '')))
    food_titles = set(df_docs.loc[df_docs['is_food'], 'title'])
    total = int(df_cit[df_cit['title'].isin(food_titles)]['total_citations'].sum())

out = json.dumps({'total_citation_count_food_domain': total})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_OIH4ZkLpKsdNZP0Jje4SjSma': 'file_storage/call_OIH4ZkLpKsdNZP0Jje4SjSma.json', 'var_call_cK1DMFbC05HgX1efYgTXBowY': 'file_storage/call_cK1DMFbC05HgX1efYgTXBowY.json'}

exec(code, env_args)
