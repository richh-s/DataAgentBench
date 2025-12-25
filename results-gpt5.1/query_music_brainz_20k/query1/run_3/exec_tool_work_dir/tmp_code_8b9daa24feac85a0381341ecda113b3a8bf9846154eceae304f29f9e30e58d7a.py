code = """import json, pandas as pd

# Load track info
tracks = var_call_S7zlJqiL6ZfUTQQY5GntIV6C
# We assume track_id 15158 is the canonical Apple Music track for Beyonce - Get Me Bodied
track_ids = {int(tracks[0]['track_id'])}

# Load full sales result from file
path = var_call_gXTEc2LPVyRAcSS5p2WYEwW7
with open(path, 'r') as f:
    sales = json.load(f)

# Filter sales to just those for the identified track_ids
filtered = [row for row in sales if int(row['track_id']) in track_ids]

total_revenue = sum(float(row['revenue_usd']) for row in filtered)

result = json.dumps({"track_ids": list(track_ids), "total_revenue_usd": round(total_revenue, 2)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_S7zlJqiL6ZfUTQQY5GntIV6C': [{'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_gXTEc2LPVyRAcSS5p2WYEwW7': 'file_storage/call_gXTEc2LPVyRAcSS5p2WYEwW7.json'}

exec(code, env_args)
