code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_sjLwcgyzuWfX4ljrzLDYxW3q)

sales_path = var_call_690ZyVEna4NEvipsE0CYrtE0
with open(sales_path, 'r') as f:
    sales = pd.DataFrame(json.load(f))

track_ids = set(tracks['track_id'].astype(int).tolist())

sales['track_id'] = sales['track_id'].astype(int)

filtered_sales = sales[sales['track_id'].isin(track_ids)]

revenue = float(filtered_sales['revenue_usd'].astype(float).sum()) if not filtered_sales.empty else 0.0

result = json.dumps({"revenue_usd": round(revenue, 2)})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_sjLwcgyzuWfX4ljrzLDYxW3q': [{'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_690ZyVEna4NEvipsE0CYrtE0': 'file_storage/call_690ZyVEna4NEvipsE0CYrtE0.json'}

exec(code, env_args)
