code = """import json, pandas as pd

with open(var_call_y3Sj034E94rsD9AD1oYSeXuM, 'r') as f:
    tracks = json.load(f)
with open(var_call_LMsBDz4BqNUg0Ol1i4Llioa9, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure numeric types
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

track_maginnis = tracks_df[tracks_df['title'].str.contains('Sttreet Hype', case=False, na=False)]
track_ids = track_maginnis['track_id'].unique().tolist()

song_sales = sales_df[sales_df['track_id'].isin(track_ids)]
store_revenue = song_sales.groupby('store', as_index=False)['revenue_usd'].sum()

max_row = store_revenue.loc[store_revenue['revenue_usd'].idxmax()]
result = {
    'store': max_row['store'],
    'revenue_usd': float(max_row['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_y3Sj034E94rsD9AD1oYSeXuM': 'file_storage/call_y3Sj034E94rsD9AD1oYSeXuM.json', 'var_call_LMsBDz4BqNUg0Ol1i4Llioa9': 'file_storage/call_LMsBDz4BqNUg0Ol1i4Llioa9.json', 'var_call_pYzkS8GLFzAXkw0mDRfc2gif': ['tracks'], 'var_call_dQtVyxI3kAzeILxAhYvNwZzh': ['sales']}

exec(code, env_args)
