code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_rIcWqqq6H4hfUmIsGsxtOpYA)

# Identify the track_ids for Beyonce - Get Me Bodied (allowing for minor title variation already captured)
track_ids = tracks['track_id'].astype(int).tolist()

# Load full Apple Music Canada sales file
import os
with open(var_call_MWTBHV7A15HSXoyyotfIXTXP, 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['track_id'] = sales['track_id'].astype(int)

filtered = sales[sales['track_id'].isin(track_ids)].copy()

total_revenue = float(filtered['revenue_usd'].astype(float).sum()) if not filtered.empty else 0.0

result = json.dumps({"track_ids": track_ids, "total_revenue_usd": round(total_revenue, 2)})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_rIcWqqq6H4hfUmIsGsxtOpYA': [{'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_MWTBHV7A15HSXoyyotfIXTXP': 'file_storage/call_MWTBHV7A15HSXoyyotfIXTXP.json'}

exec(code, env_args)
