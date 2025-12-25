code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_mluk84sQJ5zKzhcQ8ZiWuIGX)
track_ids = tracks['track_id'].astype(int).tolist()

with open(var_call_rfjzZENkQHpIKkTcdpRqVndu, 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

filtered = sales[sales['track_id'].isin(track_ids)]
result = (
    filtered.groupby('store', as_index=False)['revenue_usd']
    .sum()
    .sort_values('revenue_usd', ascending=False)
    .head(1)
)

answer = {
    'store': result.iloc[0]['store'] if not result.empty else None,
    'revenue_usd': result.iloc[0]['revenue_usd'] if not result.empty else 0.0
}

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mluk84sQJ5zKzhcQ8ZiWuIGX': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_rfjzZENkQHpIKkTcdpRqVndu': 'file_storage/call_rfjzZENkQHpIKkTcdpRqVndu.json'}

exec(code, env_args)
