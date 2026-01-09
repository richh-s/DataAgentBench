code = """import json, pandas as pd

# load full mongo result
path = var_call_e0O8RArbxHTHb0Q6KHl8NA66
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].map(len)
max_len = df['desc_len'].max()
# pick one title deterministically: first by desc_len desc then article_id asc
# article_id may be str

df['article_id_int'] = pd.to_numeric(df['article_id'], errors='coerce')
df_sorted = df.sort_values(['desc_len','article_id_int'], ascending=[False, True])
row = df_sorted.iloc[0]
result = {'title': row['title'], 'description_length': int(row['desc_len']), 'article_id': None if pd.isna(row['article_id_int']) else int(row['article_id_int'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_e0O8RArbxHTHb0Q6KHl8NA66': 'file_storage/call_e0O8RArbxHTHb0Q6KHl8NA66.json'}

exec(code, env_args)
