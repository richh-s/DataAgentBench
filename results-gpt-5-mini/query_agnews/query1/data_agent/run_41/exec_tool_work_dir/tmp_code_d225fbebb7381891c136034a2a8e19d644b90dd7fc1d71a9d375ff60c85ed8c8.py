code = """import json
import pandas as pd

with open(var_call_wjijicMPNedUw4ONyAHg4xMA, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['article_id','title','description']:
    if col not in df.columns:
        df[col] = ''

df['description'] = df['description'].fillna('').astype(str)
df['desc_len'] = df['description'].apply(len)

# Prepare list of dicts for first 300 records (or all if fewer)
records = df[['article_id','title','desc_len']].to_dict(orient='records')

# Limit to first 300
records = records[:300]

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_wjijicMPNedUw4ONyAHg4xMA': 'file_storage/call_wjijicMPNedUw4ONyAHg4xMA.json', 'var_call_cx5PEPS95YUVsIvlHoiREaKF': None, 'var_call_Ats8FczWZ8SwMGxhTTwZuUnX': {'count': 0, 'top_title': None, 'top_desc_len': None, 'candidates': []}}

exec(code, env_args)
