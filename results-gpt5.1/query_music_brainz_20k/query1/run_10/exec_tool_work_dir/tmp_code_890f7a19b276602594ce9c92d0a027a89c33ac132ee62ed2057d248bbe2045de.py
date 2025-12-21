code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_00P8O7iFnSbuXeES2sorT865)

with open(var_call_IXX6smQMdd39Iy6bTDt82m37, 'r') as f:
    sales = pd.DataFrame(json.load(f))

track_ids = tracks['track_id'].astype(int).tolist()

relevant_sales = sales[sales['track_id'].astype(int).isin(track_ids)]

total_revenue = float(relevant_sales['revenue_usd'].astype(float).sum()) if not relevant_sales.empty else 0.0

result = json.dumps({"total_revenue_usd": round(total_revenue, 2)})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_00P8O7iFnSbuXeES2sorT865': [{'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_IXX6smQMdd39Iy6bTDt82m37': 'file_storage/call_IXX6smQMdd39Iy6bTDt82m37.json'}

exec(code, env_args)
