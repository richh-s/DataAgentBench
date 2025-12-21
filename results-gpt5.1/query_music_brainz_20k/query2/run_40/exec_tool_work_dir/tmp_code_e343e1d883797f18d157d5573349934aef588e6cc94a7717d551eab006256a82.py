code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_H6ugi7Hl5MPfiWpelpVvqcVs)
track_ids = set(tracks['track_id'].astype(int).tolist())

# load full sales data
import os
with open(var_call_QHoIlvdrzXaV8JGjavRVVmJ7, 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

filtered = sales[sales['track_id'].isin(track_ids)]
by_store = filtered.groupby('store', as_index=False)['revenue_usd'].sum()
by_store = by_store.sort_values('revenue_usd', ascending=False)

best_store = None
best_revenue = 0.0
if not by_store.empty:
    row = by_store.iloc[0]
    best_store = row['store']
    best_revenue = float(row['revenue_usd'])

result = {'store': best_store, 'total_revenue_usd': best_revenue}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_H6ugi7Hl5MPfiWpelpVvqcVs': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_QHoIlvdrzXaV8JGjavRVVmJ7': 'file_storage/call_QHoIlvdrzXaV8JGjavRVVmJ7.json'}

exec(code, env_args)
