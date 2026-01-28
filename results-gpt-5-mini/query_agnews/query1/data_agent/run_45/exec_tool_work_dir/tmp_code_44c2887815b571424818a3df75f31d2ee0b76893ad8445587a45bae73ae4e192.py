code = """import json
import pandas as pd

# Load the result of the sports-filtered query
with open(var_call_h0uxi2eY1wjuvKjzP7HdC7tn, 'r', encoding='utf-8') as f:
    data = json.load(f)

# data is a list of records
if not data:
    result_title = ""
else:
    df = pd.DataFrame(data)
    df['description'] = df.get('description','').fillna('').astype(str)
    df['title'] = df.get('title','').fillna('').astype(str)
    df['desc_len'] = df['description'].apply(len)
    idx = df['desc_len'].idxmax()
    result_title = df.at[idx, 'title']

import json as _json
print('__RESULT__:')
print(_json.dumps(result_title))"""

env_args = {'var_call_lgxb6TZjxdpNhqMYHh1qGD0s': 'file_storage/call_lgxb6TZjxdpNhqMYHh1qGD0s.json', 'var_call_4zqdTVXRsE4IbaFKC2DnfeWF': '', 'var_call_S5otKnULYzerPiJYdMjFhgEl': 'file_storage/call_S5otKnULYzerPiJYdMjFhgEl.json', 'var_call_Zc8aJneBVWyppeJWNKpREGqh': 'file_storage/call_Zc8aJneBVWyppeJWNKpREGqh.json', 'var_call_h0uxi2eY1wjuvKjzP7HdC7tn': 'file_storage/call_h0uxi2eY1wjuvKjzP7HdC7tn.json'}

exec(code, env_args)
