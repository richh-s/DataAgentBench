code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_QCDxOFBADeyJqJa9ZFNaq022)

with open(var_call_DvhrgRGnKHat72mQDloLvdc9, 'r') as f:
    sales = pd.DataFrame(json.load(f))

track_ids = set(tracks['track_id'].astype(int).tolist())

sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

filtered = sales[sales['track_id'].isin(track_ids)]

agg = filtered.groupby('store', as_index=False)['revenue_usd'].sum()

if agg.empty:
    result = {"store": None, "revenue_usd": 0.0}
else:
    top = agg.sort_values('revenue_usd', ascending=False).iloc[0]
    result = {"store": top['store'], "revenue_usd": float(top['revenue_usd'])}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QCDxOFBADeyJqJa9ZFNaq022': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_DvhrgRGnKHat72mQDloLvdc9': 'file_storage/call_DvhrgRGnKHat72mQDloLvdc9.json', 'var_call_OwPKp6lxfz7JgoedsS0MCDYP': ['tracks'], 'var_call_laGE6A4iBlgjmQ6HfGQ1HBvX': ['sales']}

exec(code, env_args)
