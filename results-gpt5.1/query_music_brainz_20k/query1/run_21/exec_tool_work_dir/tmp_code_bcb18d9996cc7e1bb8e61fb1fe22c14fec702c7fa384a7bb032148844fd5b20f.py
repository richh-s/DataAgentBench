code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_4eV3WZFgopFNH0bmoTuz2Yro)
# Identify track_ids for Beyonce - Get Me Bodied (allowing minor title variants)
tracks['title_lower'] = tracks['title'].str.lower()
tracks['artist_lower'] = tracks['artist'].str.lower()
candidate_ids = tracks.loc[
    tracks['title_lower'].str.contains('get me bodied') &
    tracks['artist_lower'].str.contains('beyonce')
, 'track_id'].astype(int).tolist()

# Load all Canada / Apple Music sales
import os
path = var_call_CsOsxjvfmY2s8nG3mWICAeGo
if os.path.isfile(path):
    with open(path, 'r') as f:
        sales_data = json.load(f)
else:
    sales_data = var_call_CsOsxjvfmY2s8nG3mWICAeGo

sales = pd.DataFrame(sales_data)
sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

if candidate_ids:
    total_revenue = sales[sales['track_id'].isin(candidate_ids)]['revenue_usd'].sum()
else:
    total_revenue = 0.0

result = json.dumps({'track_ids': candidate_ids, 'total_revenue_usd': round(float(total_revenue), 2)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_4eV3WZFgopFNH0bmoTuz2Yro': [{'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_CsOsxjvfmY2s8nG3mWICAeGo': 'file_storage/call_CsOsxjvfmY2s8nG3mWICAeGo.json'}

exec(code, env_args)
