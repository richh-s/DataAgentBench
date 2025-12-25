code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_Sgn5P4MuaCH0RMXItZX3dJR4)

# identify track_ids corresponding to Beyonce - Get Me Bodied
track_ids = tracks['track_id'].astype(int).tolist()

# load full sales data from file
with open(var_call_CxoAqPzhvqlKdX49tJ83G9Za, 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

revenue = sales[sales['track_id'].isin(track_ids)]['revenue_usd'].sum()

result = json.dumps({'revenue_usd': round(revenue, 2)})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_Sgn5P4MuaCH0RMXItZX3dJR4': [{'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_CxoAqPzhvqlKdX49tJ83G9Za': 'file_storage/call_CxoAqPzhvqlKdX49tJ83G9Za.json'}

exec(code, env_args)
