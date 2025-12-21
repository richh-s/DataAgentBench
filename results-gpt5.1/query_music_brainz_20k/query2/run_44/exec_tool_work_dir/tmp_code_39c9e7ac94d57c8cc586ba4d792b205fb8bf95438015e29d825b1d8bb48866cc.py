code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_dmry4sKhqWsNCp3rfAJHxmvb)
track_ids = tracks['track_id'].astype(int).tolist()

# load full sales data
import os
with open(var_call_TyXH2k9LP5EzBbP0l8ZrGPJZ, 'r') as f:
    sales_data = json.load(f)

sales = pd.DataFrame(sales_data)
sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

filtered = sales[sales['track_id'].isin(track_ids)]

agg = filtered.groupby('store', as_index=False)['revenue_usd'].sum()

if agg.empty:
    result = json.dumps({"store": None, "revenue_usd": 0})
else:
    top = agg.sort_values('revenue_usd', ascending=False).iloc[0]
    result = json.dumps({"store": top['store'], "revenue_usd": top['revenue_usd']})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_dmry4sKhqWsNCp3rfAJHxmvb': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_TyXH2k9LP5EzBbP0l8ZrGPJZ': 'file_storage/call_TyXH2k9LP5EzBbP0l8ZrGPJZ.json', 'var_call_SXONd42BQ9myfWxlW0MhqnHa': ['tracks'], 'var_call_AkoyEcuqEVNUenlNABNmHtrz': ['sales']}

exec(code, env_args)
