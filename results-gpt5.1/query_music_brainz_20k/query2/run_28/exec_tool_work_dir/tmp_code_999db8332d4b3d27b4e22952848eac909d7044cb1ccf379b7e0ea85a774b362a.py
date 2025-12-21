code = """import json, pandas as pd
from pathlib import Path

tracks = var_call_zPeJBzKSqCGVt9qfGYX9S1nM
sales_path = Path(var_call_aAbpKJ2QoAu5XNQROe8QcqBS)
with open(sales_path, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

street_ids = set(tracks_df['track_id'].tolist())
filtered = sales_df[sales_df['track_id'].isin(street_ids)]
agg = filtered.groupby('store', as_index=False)['revenue_usd'].sum()
if len(agg)==0:
    result = {"store": None, "revenue_usd": 0}
else:
    top = agg.sort_values('revenue_usd', ascending=False).iloc[0]
    result = {"store": top['store'], "revenue_usd": round(float(top['revenue_usd']),2)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zPeJBzKSqCGVt9qfGYX9S1nM': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_aAbpKJ2QoAu5XNQROe8QcqBS': 'file_storage/call_aAbpKJ2QoAu5XNQROe8QcqBS.json', 'var_call_8PLmjkoPzQbGpIvMQ2sq9gBJ': ['tracks'], 'var_call_RmJ44BqCz9h74vDw1N6J5fVf': ['sales']}

exec(code, env_args)
