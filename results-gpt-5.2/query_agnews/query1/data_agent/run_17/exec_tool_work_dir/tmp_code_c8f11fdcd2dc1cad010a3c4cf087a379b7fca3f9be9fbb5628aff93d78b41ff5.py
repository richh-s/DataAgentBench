code = """import json, pandas as pd

path = var_call_Cf7EZTxVxitom5mXD7EG8wA7
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure strings and handle missing
for col in ['title','description']:
    df[col] = df[col].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = df['desc_len'].max()
row = df.loc[df['desc_len'].idxmax()]
result = {'title': row['title'], 'article_id': row.get('article_id'), 'description_length': int(max_len)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Cf7EZTxVxitom5mXD7EG8wA7': 'file_storage/call_Cf7EZTxVxitom5mXD7EG8wA7.json'}

exec(code, env_args)
