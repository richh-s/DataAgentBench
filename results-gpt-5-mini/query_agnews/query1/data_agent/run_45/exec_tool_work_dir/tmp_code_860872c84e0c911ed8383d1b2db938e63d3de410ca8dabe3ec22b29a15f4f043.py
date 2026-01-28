code = """import json
import pandas as pd

with open(var_call_lgxb6TZjxdpNhqMYHh1qGD0s, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['title'] = df.get('title', '').fillna('').astype(str)
df['description'] = df.get('description', '').fillna('').astype(str)

df['desc_len'] = df['description'].apply(len)
# get top 50 longest descriptions
top = df.sort_values('desc_len', ascending=False).head(50)[['title','description','desc_len']]
# convert to list of dicts
out = top.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lgxb6TZjxdpNhqMYHh1qGD0s': 'file_storage/call_lgxb6TZjxdpNhqMYHh1qGD0s.json', 'var_call_4zqdTVXRsE4IbaFKC2DnfeWF': ''}

exec(code, env_args)
