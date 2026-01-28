code = """import pandas as pd
import json

# Data from previous query_db calls (available in storage)
records = var_call_wMHlokly7VTNyqi9jEYwV3of
tracks = var_call_bHRnjLCBIMcDvY06c4hrIkBr

# Load sales records into DataFrame
if isinstance(records, str):
    # if it's a filepath, read json
    df = pd.read_json(records)
else:
    df = pd.DataFrame(records)

# Normalize types and compute totals
if not df.empty:
    df['revenue_usd'] = df['revenue_usd'].astype(float)
    df['track_id'] = df['track_id'].astype(int)
    total = df['revenue_usd'].sum()
else:
    total = 0.0

# Determine track_ids from tracks table (entity resolution candidates)
track_ids = sorted([int(t['track_id']) for t in tracks])

sold_track_ids = df['track_id'].tolist() if not df.empty else []
missing = [tid for tid in track_ids if tid not in sold_track_ids]

# Build breakdown including missing track_ids with zero revenue
breakdown = []
for r in (df.to_dict(orient='records') if not df.empty else []):
    breakdown.append({'track_id': int(r['track_id']), 'revenue_usd': float(r['revenue_usd'])})
for m in missing:
    breakdown.append({'track_id': m, 'revenue_usd': 0.0})

result = {
    'track_ids_considered': track_ids,
    'breakdown': breakdown,
    'total_revenue_usd': round(float(total), 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bHRnjLCBIMcDvY06c4hrIkBr': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_wMHlokly7VTNyqi9jEYwV3of': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354.0', 'revenue_usd': '377.62'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210.0', 'revenue_usd': '223.82'}]}

exec(code, env_args)
