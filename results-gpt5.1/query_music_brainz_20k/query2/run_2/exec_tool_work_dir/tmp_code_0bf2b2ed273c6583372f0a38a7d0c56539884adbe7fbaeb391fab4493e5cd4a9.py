code = """import json, pandas as pd

with open(var_call_TIRlkB33DS7YH7NLNy59DNGJ, 'r') as f:
    tracks = json.load(f)
tracks_df = pd.DataFrame(tracks)

# Inspect any row that looks like Bruce/Brucqe Maginnis Street Hype allowing for typos
candidates = tracks_df[tracks_df['title'].str.contains('ruce', case=False, na=False) |
                       tracks_df['title'].str.contains('Maginnis', case=False, na=False) |
                       tracks_df['title'].str.contains('Street', case=False, na=False) |
                       tracks_df['title'].str.contains('Hype', case=False, na=False)]

res = candidates[['track_id','title','artist','album','year']].head(50).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_TIRlkB33DS7YH7NLNy59DNGJ': 'file_storage/call_TIRlkB33DS7YH7NLNy59DNGJ.json', 'var_call_uy6lO5uMG2mcBNQ2QSZAltLI': 'file_storage/call_uy6lO5uMG2mcBNQ2QSZAltLI.json', 'var_call_JhMX87QwpoEetM2u3P7zkpan': {}}

exec(code, env_args)
