code = """import json, re
import pandas as pd

docs_path = var_call_cK1DMFbC05HgX1efYgTXBowY
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df = pd.DataFrame(docs)
if df.empty:
    out={'n_food_keyword':0,'sample_titles':[]}
else:
    df['title']=df['filename'].str.replace(r'\\.txt$','',regex=True)
    pat = re.compile(r'\\bfood\\b', re.IGNORECASE)
    df['has_food']=df['text'].apply(lambda t: bool(pat.search(t or '')))
    out={'n_food_keyword': int(df['has_food'].sum()), 'sample_titles': df.loc[df['has_food'],'title'].head(20).tolist()}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_OIH4ZkLpKsdNZP0Jje4SjSma': 'file_storage/call_OIH4ZkLpKsdNZP0Jje4SjSma.json', 'var_call_cK1DMFbC05HgX1efYgTXBowY': 'file_storage/call_cK1DMFbC05HgX1efYgTXBowY.json', 'var_call_ZEuF8mA9BPOUO7kbrArabAVw': {'total_citation_count_food_domain': 0}, 'var_call_DvjFD2WlKfbTLLMjOGAQewiZ': {'n_food_detected': 0, 'sample_titles': []}}

exec(code, env_args)
