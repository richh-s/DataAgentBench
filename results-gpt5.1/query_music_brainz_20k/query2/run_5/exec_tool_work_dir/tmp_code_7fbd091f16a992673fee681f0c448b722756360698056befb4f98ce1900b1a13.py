code = """import json, pandas as pd
from pathlib import Path

tracks = pd.DataFrame(var_call_3JJogHZmShNEb6hoWNVUl88m)
track_ids = set(tracks['track_id'].astype(int).tolist())

# load full sales data
sales_path = Path(var_call_xHJGyI7QzwbRJEoUXIRoZkEv)
with open(sales_path, 'r') as f:
    sales_data = json.load(f)

sales = pd.DataFrame(sales_data)
sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

filtered = sales[sales['track_id'].isin(track_ids)]
by_store = filtered.groupby('store', as_index=False)['revenue_usd'].sum()
if by_store.empty:
    result = None
else:
    top = by_store.sort_values('revenue_usd', ascending=False).iloc[0]
    result = {'store': top['store'], 'revenue_usd': top['revenue_usd']}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3JJogHZmShNEb6hoWNVUl88m': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_xHJGyI7QzwbRJEoUXIRoZkEv': 'file_storage/call_xHJGyI7QzwbRJEoUXIRoZkEv.json'}

exec(code, env_args)
