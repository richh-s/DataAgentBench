code = """import json, pandas as pd

with open(var_call_otNRRnZZlmOUmE6wg58jVIAc, 'r') as f:
    tracks = json.load(f)
with open(var_call_tYHRJR5RKqvvex6TKD234a92, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure consistent dtypes
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

tracks_df['canon_key'] = tracks_df['title'] + '|' + tracks_df['artist'] + '|' + tracks_df['album']

track_id_to_key = tracks_df.set_index('track_id')['canon_key']

sales_df = sales_df.merge(track_id_to_key.rename('canon_key'), left_on='track_id', right_index=True, how='left')

agg = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].apply(lambda s: pd.to_numeric(s, errors='coerce').sum()).reset_index()

agg = agg[agg['revenue_usd'].notna()]

top_row = agg.sort_values('revenue_usd', ascending=False).iloc[0]

best_key = top_row['canon_key']
best_revenue = float(top_row['revenue_usd'])

rep = tracks_df[tracks_df['canon_key'] == best_key].iloc[0]

answer = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'total_revenue_usd': round(best_revenue, 2)
}

result = json.dumps(answer)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_otNRRnZZlmOUmE6wg58jVIAc': 'file_storage/call_otNRRnZZlmOUmE6wg58jVIAc.json', 'var_call_tYHRJR5RKqvvex6TKD234a92': 'file_storage/call_tYHRJR5RKqvvex6TKD234a92.json'}

exec(code, env_args)
