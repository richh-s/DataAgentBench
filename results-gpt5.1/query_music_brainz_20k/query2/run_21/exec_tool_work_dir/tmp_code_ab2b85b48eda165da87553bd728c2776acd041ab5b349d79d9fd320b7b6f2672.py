code = """import json
import pandas as pd

tracks = pd.DataFrame(var_call_w6hUZwrHFFW45nfDUFCkm943)
track_ids = tracks['track_id'].astype(int).tolist()

with open(var_call_fCbUtn3pxB85Jkc2yyKN4b9X, 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

filtered = sales[sales['track_id'].isin(track_ids)]
agg = filtered.groupby('store', as_index=False)['revenue_usd'].sum()
max_row = agg.sort_values('revenue_usd', ascending=False).iloc[0]
result = {'store': max_row['store'], 'total_revenue_usd': max_row['revenue_usd']}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_w6hUZwrHFFW45nfDUFCkm943': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_fCbUtn3pxB85Jkc2yyKN4b9X': 'file_storage/call_fCbUtn3pxB85Jkc2yyKN4b9X.json'}

exec(code, env_args)
