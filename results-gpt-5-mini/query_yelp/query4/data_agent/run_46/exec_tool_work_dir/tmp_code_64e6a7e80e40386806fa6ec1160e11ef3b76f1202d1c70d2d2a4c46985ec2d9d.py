code = """import json, pandas as pd
with open(var_call_2VgzWa3JXAusBYgey1CUq8bj, 'r') as f:
    biz = json.load(f)
df = pd.DataFrame(biz)
cols = list(df.columns)
# Show first 20 records with selected fields
sample = df.head(20).to_dict(orient='records')
res = {'columns': cols, 'sample_count': len(sample), 'sample': sample}
print('__RESULT__:')
import json
print(json.dumps(res))"""

env_args = {'var_call_2VgzWa3JXAusBYgey1CUq8bj': 'file_storage/call_2VgzWa3JXAusBYgey1CUq8bj.json', 'var_call_ZRQPeIbwlwDm9DOxHjzcFWq3': 'file_storage/call_ZRQPeIbwlwDm9DOxHjzcFWq3.json', 'var_call_rUE7zCuSnheFo44yAKOEe8On': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
