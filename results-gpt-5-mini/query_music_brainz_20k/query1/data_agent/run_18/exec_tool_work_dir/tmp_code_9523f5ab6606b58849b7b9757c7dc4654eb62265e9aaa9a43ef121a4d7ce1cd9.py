code = """import pandas as pd
import json

df_tracks = pd.DataFrame(var_call_kkh8sHnwNadFYUc3IzFY7Ei2)
df_sales = pd.DataFrame(var_call_KADCxMuagkUUZEEJghlPvSAZ)

# Ensure correct dtypes
if not df_sales.empty:
    df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)

# Sum total revenue
total_revenue = float(df_sales['revenue_usd'].sum()) if not df_sales.empty else 0.0

# Build breakdown with track metadata
breakdown = []
for _, row in df_sales.iterrows():
    tid = str(row['track_id'])
    revenue = float(row['revenue_usd'])
    track_rows = df_tracks[df_tracks['track_id'] == tid]
    if not track_rows.empty:
        track_info = track_rows.iloc[0].to_dict()
    else:
        track_info = {'track_id': tid}
    breakdown.append({
        'track_id': tid,
        'revenue_usd': revenue,
        'title': track_info.get('title'),
        'artist': track_info.get('artist'),
        'album': track_info.get('album'),
        'year': track_info.get('year')
    })

result = {
    'query': "Apple Music revenue for Beyoncé's song 'Get Me Bodied' in Canada",
    'total_revenue_usd': round(total_revenue, 2),
    'breakdown': breakdown
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kkh8sHnwNadFYUc3IzFY7Ei2': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown'}], 'var_call_KADCxMuagkUUZEEJghlPvSAZ': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '377.62'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '223.82'}]}

exec(code, env_args)
