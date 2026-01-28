code = """import json, pandas as pd
path = var_call_rofT4dTBJmcUOqxOlBF5saj9
with open(path,'r',encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].astype(str)

df['desc_len'] = df['description'].str.len()
max_len = int(df['desc_len'].max())
# pick first max
row = df.loc[df['desc_len'].eq(max_len)].iloc[0]
result = {'title': row['title'], 'article_id': row.get('article_id', None), 'desc_len': max_len}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rofT4dTBJmcUOqxOlBF5saj9': 'file_storage/call_rofT4dTBJmcUOqxOlBF5saj9.json'}

exec(code, env_args)
