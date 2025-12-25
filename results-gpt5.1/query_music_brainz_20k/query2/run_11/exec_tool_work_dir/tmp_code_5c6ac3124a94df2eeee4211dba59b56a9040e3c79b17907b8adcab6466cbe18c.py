code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_AVjkuqg3KPOggjM3peIK3mbL)
track_ids = tracks['track_id'].astype(int).tolist()

# load full sales data
with open(var_call_DefjfdoqzFwAonpda6WdmpAi, 'r') as f:
    sales_data = json.load(f)

sales = pd.DataFrame(sales_data)
sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

filtered = sales[sales['track_id'].isin(track_ids)]
agg = filtered.groupby('store', as_index=False)['revenue_usd'].sum()
if not agg.empty:
    best = agg.sort_values('revenue_usd', ascending=False).iloc[0]
    result = {'store': best['store'], 'revenue_usd': round(float(best['revenue_usd']), 2)}
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_AVjkuqg3KPOggjM3peIK3mbL': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_DefjfdoqzFwAonpda6WdmpAi': 'file_storage/call_DefjfdoqzFwAonpda6WdmpAi.json', 'var_call_4fNienO5dStN7rtZBBLKtjFf': ['tracks'], 'var_call_IjoexOjqXCf6JNidOj3jnLML': ['sales']}

exec(code, env_args)
