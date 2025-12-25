code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_6tqakAUUdoUzuwGrBVWm87Af)

sales_path = var_call_Koi6Z3INov1X8NSLzBpVXz69
with open(sales_path, 'r') as f:
    sales = pd.DataFrame(json.load(f))

track_ids = set(tracks['track_id'].astype(int).tolist())

sales['track_id'] = sales['track_id'].astype(int)
relevant_sales = sales[sales['track_id'].isin(track_ids)]

total_revenue = float(relevant_sales['revenue_usd'].astype(float).sum()) if not relevant_sales.empty else 0.0

result = json.dumps({"total_revenue_usd": round(total_revenue, 2)})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_6tqakAUUdoUzuwGrBVWm87Af': [{'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_Koi6Z3INov1X8NSLzBpVXz69': 'file_storage/call_Koi6Z3INov1X8NSLzBpVXz69.json'}

exec(code, env_args)
