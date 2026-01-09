code = """import json, pandas as pd

path = var_call_hKVtOc29TORP25yMgYhZaq9l
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = int(df['desc_len'].max())
row = df.loc[df['desc_len'].idxmax()]

print('__RESULT__:')
print(json.dumps({'title': row['title'], 'article_id': row.get('article_id', None), 'desc_len': int(row['desc_len'])}))"""

env_args = {'var_call_hKVtOc29TORP25yMgYhZaq9l': 'file_storage/call_hKVtOc29TORP25yMgYhZaq9l.json', 'var_call_tu3ZqWL9tPomPagiVwjvoSy7': {'max_description_length': 985, 'num_articles_with_max_length': 1, 'num_sports_articles_with_max_length': 0, 'titles': []}}

exec(code, env_args)
