code = """import json, pandas as pd

# Load full datasets from files
with open(var_call_yKmeUC7wglmMS4UJZ7MNOwuD, 'r') as f:
    tracks = json.load(f)
with open(var_call_mOqpUIkeot60s92Z4jTcGbh5, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Aggregate revenue by track_id
track_revenue = sales_df.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Merge with tracks to get metadata
merged = track_revenue.merge(tracks_df, on='track_id', how='left')

# Basic entity resolution: define canonical key using normalized title+artist+album
for col in ['title','artist','album']:
    merged[col] = merged[col].fillna('').astype(str).str.strip().str.lower()

merged['canonical'] = merged['title'] + ' | ' + merged['artist'] + ' | ' + merged['album']

# Sum revenue over canonical tracks
canonical_revenue = merged.groupby('canonical', as_index=False)['revenue_usd'].sum()

# Find max revenue canonical track
top_row = canonical_revenue.sort_values('revenue_usd', ascending=False).iloc[0]

# Retrieve one representative original record to report readable fields
rep = merged[merged['canonical'] == top_row['canonical']].iloc[0]

answer = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'total_revenue_usd': round(float(top_row['revenue_usd']), 2)
}

result = json.dumps(answer)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_yKmeUC7wglmMS4UJZ7MNOwuD': 'file_storage/call_yKmeUC7wglmMS4UJZ7MNOwuD.json', 'var_call_mOqpUIkeot60s92Z4jTcGbh5': 'file_storage/call_mOqpUIkeot60s92Z4jTcGbh5.json', 'var_call_x2s4Xrc5GOp2yjH28MvUfEeH': 'placeholder'}

exec(code, env_args)
