code = """import json
import pandas as pd
import re

with open(var_call_hmTBT2DHTxceJVlLDlvqmGy5, 'r') as f:
    businesses = json.load(f)
with open(var_call_C26XA720lemvNYIWrVw6IXtD, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Extract state
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    matches = re.findall(r"\b([A-Z]{2})\b", desc)
    return matches[-1] if matches else None

df_b['state'] = df_b['description'].apply(extract_state)

df_b_sample = df_b[['business_id','description','state']].head(20).to_dict(orient='records')

df_r_sample = df_r.head(20)[['business_ref','rating']].to_dict(orient='records')

# id_suffix
if 'business_ref' in df_r.columns:
    df_r['id_suffix'] = df_r['business_ref'].astype(str).apply(lambda s: s.split('_')[-1] if '_' in s else None)
else:
    df_r['id_suffix'] = None

df_b['id_suffix'] = df_b['business_id'].astype(str).apply(lambda s: s.split('_')[-1] if '_' in s else None)

merged_sample = df_r.head(20).merge(df_b[['id_suffix','state']], on='id_suffix', how='left')[['business_ref','rating','id_suffix','state']].to_dict(orient='records')

# Count non-null states
state_counts = df_b['state'].notna().sum()

result = {
    'df_b_sample': df_b_sample,
    'df_r_sample': df_r_sample,
    'merged_sample': merged_sample,
    'businesses_with_state_count': int(state_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_35fgkqrbnU6wwvPZlWOULiZy': ['business', 'checkin'], 'var_call_4aMIiTGqEUjIrhUXk4fjUb2X': ['review', 'tip', 'user'], 'var_call_hmTBT2DHTxceJVlLDlvqmGy5': 'file_storage/call_hmTBT2DHTxceJVlLDlvqmGy5.json', 'var_call_C26XA720lemvNYIWrVw6IXtD': 'file_storage/call_C26XA720lemvNYIWrVw6IXtD.json', 'var_call_peDaDbKsBikc6B6arqepJNai': {'state': None, 'review_count': 0, 'average_rating': None}}

exec(code, env_args)
