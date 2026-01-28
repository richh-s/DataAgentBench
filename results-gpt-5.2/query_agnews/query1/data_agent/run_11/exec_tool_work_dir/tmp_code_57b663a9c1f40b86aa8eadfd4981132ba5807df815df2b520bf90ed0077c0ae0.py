code = """import json
import pandas as pd

path = var_call_eI7jInTSY8f0lVgyuQthTcWQ
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure strings
for col in ['title','description']:
    df[col] = df[col].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = df['desc_len'].max()
max_rows = df[df['desc_len'] == max_len]
# pick first by article_id numeric if possible
max_rows = max_rows.copy()
max_rows['article_id_num'] = pd.to_numeric(max_rows.get('article_id'), errors='coerce')
max_rows = max_rows.sort_values(['article_id_num','article_id'], na_position='last')
result = {
    'title': max_rows.iloc[0]['title'],
    'description_length': int(max_len),
    'article_id': str(max_rows.iloc[0].get('article_id'))
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_eI7jInTSY8f0lVgyuQthTcWQ': 'file_storage/call_eI7jInTSY8f0lVgyuQthTcWQ.json'}

exec(code, env_args)
