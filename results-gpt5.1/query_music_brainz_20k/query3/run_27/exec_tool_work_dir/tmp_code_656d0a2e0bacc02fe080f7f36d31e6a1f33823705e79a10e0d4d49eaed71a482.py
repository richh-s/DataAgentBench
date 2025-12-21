code = """import json, pandas as pd
from pathlib import Path

# Load tracks data
with open(var_call_US79COYSEKpwTi1vW9hB9P0h, 'r') as f:
    tracks = json.load(f)

tracks_df = pd.DataFrame(tracks)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Load previous result
res = var_call_3DhpYq6dpDjzMWAv6nUPTEoG
track_ids = res['track_ids']
max_rev = res['max_revenue_usd']

# Filter tracks for these IDs
subset = tracks_df[tracks_df['track_id'].isin(track_ids)][['track_id','title','artist','album','year']]

result = {
    'max_revenue_usd': max_rev,
    'tracks': subset.to_dict(orient='records')
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_o2UwDeMI56h9OQOY7f4GAP0A': 'file_storage/call_o2UwDeMI56h9OQOY7f4GAP0A.json', 'var_call_US79COYSEKpwTi1vW9hB9P0h': 'file_storage/call_US79COYSEKpwTi1vW9hB9P0h.json', 'var_call_3DhpYq6dpDjzMWAv6nUPTEoG': {'max_revenue_usd': 2522.82, 'track_ids': [14719]}}

exec(code, env_args)
