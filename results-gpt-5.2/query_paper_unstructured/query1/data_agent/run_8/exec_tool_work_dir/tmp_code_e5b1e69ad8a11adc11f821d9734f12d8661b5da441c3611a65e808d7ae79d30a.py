code = """import json, re
import pandas as pd

docs_path = var_call_cK1DMFbC05HgX1efYgTXBowY
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df = pd.DataFrame(docs)
if df.empty:
    out = {'n_food_detected': 0, 'sample_titles': []}
else:
    df['title'] = df['filename'].str.replace(r'\\.txt$', '', regex=True)
    pat2 = re.compile(r'(domain|domains)\\s*[:\\-]\\s*[^\\n\\r]*\\bfood\\b', re.IGNORECASE)
    df['is_food'] = df['text'].apply(lambda t: bool(pat2.search(t or '')))
    out = {'n_food_detected': int(df['is_food'].sum()), 'sample_titles': df.loc[df['is_food'], 'title'].head(20).tolist()}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_OIH4ZkLpKsdNZP0Jje4SjSma': 'file_storage/call_OIH4ZkLpKsdNZP0Jje4SjSma.json', 'var_call_cK1DMFbC05HgX1efYgTXBowY': 'file_storage/call_cK1DMFbC05HgX1efYgTXBowY.json', 'var_call_ZEuF8mA9BPOUO7kbrArabAVw': {'total_citation_count_food_domain': 0}}

exec(code, env_args)
