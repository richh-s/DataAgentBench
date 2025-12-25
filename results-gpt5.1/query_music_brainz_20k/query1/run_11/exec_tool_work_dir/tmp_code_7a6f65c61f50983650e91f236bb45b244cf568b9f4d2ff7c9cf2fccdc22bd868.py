code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_95soX1af0ppz1jWD6q1ROCjs)
track_ids = tracks['track_id'].astype(int).tolist()

# load full sales data from file
with open(var_call_M4I8IgVz3djRW6JbPV3amaln, 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['track_id'] = sales['track_id'].astype(int)

relevant_sales = sales[sales['track_id'].isin(track_ids)]

total_revenue = float(relevant_sales['revenue_usd'].astype(float).sum()) if not relevant_sales.empty else 0.0

result = json.dumps({"track_ids": track_ids, "total_revenue_usd": round(total_revenue, 2)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_95soX1af0ppz1jWD6q1ROCjs': [{'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_M4I8IgVz3djRW6JbPV3amaln': 'file_storage/call_M4I8IgVz3djRW6JbPV3amaln.json'}

exec(code, env_args)
