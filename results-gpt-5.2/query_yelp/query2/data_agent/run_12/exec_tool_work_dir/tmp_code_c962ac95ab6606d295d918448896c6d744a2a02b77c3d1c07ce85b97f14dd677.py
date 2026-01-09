code = """import json, re, pandas as pd

def load_tool_result(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

biz = load_tool_result(var_call_nM334UVtoNFxYyzh0CYyTTDV)
rev = load_tool_result(var_call_RIoSDHu7GDyB3qSNOy3DhfNp)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

state_pat = re.compile(r",\s*([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pat.search(desc)
    return m.group(1) if m else None

biz_df['state'] = biz_df['description'].apply(extract_state)

biz_df['key'] = biz_df['business_id'].str.replace('businessid_', '', regex=False)
rev_df['key'] = rev_df['business_ref'].str.replace('businessref_', '', regex=False)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

merged = rev_df.merge(biz_df[['key','state']], on='key', how='left')
merged = merged.dropna(subset=['state','rating'])

if merged.empty:
    out = {'error':'No reviews could be matched to a parsed state from business descriptions.'}
else:
    state_counts = merged.groupby('state').size().sort_values(ascending=False)
    max_state = state_counts.index[0]
    avg_rating = merged.loc[merged['state']==max_state, 'rating'].mean()
    out = {
        'state': max_state,
        'review_count': int(state_counts.iloc[0]),
        'average_business_rating_in_state': float(avg_rating)
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nM334UVtoNFxYyzh0CYyTTDV': 'file_storage/call_nM334UVtoNFxYyzh0CYyTTDV.json', 'var_call_RIoSDHu7GDyB3qSNOy3DhfNp': 'file_storage/call_RIoSDHu7GDyB3qSNOy3DhfNp.json'}

exec(code, env_args)
