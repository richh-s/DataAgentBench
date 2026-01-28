code = """import json
import pandas as pd

# Load the large query result from the tracks_database query stored in a file path variable
path = var_call_CNN3yRYVvkJfCft81uiH2XO5
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)
# normalize
df['title_low'] = df['title'].fillna('').str.lower()
df['artist_low'] = df['artist'].fillna('').str.lower()
# remove spaces for nospace check
df['title_nospace'] = df['title_low'].str.replace(' ', '')
# find candidates matching 'street' and 'hype' or title_nospace contains 'streethype' or artist contains 'maginnis'
mask = (
    ((df['title_low'].str.contains('street', na=False)) & (df['title_low'].str.contains('hype', na=False)))
    | (df['title_nospace'].str.contains('streethype', na=False))
    | (df['artist_low'].str.contains('maginnis', na=False) & df['title_low'].str.contains('street', na=False))
)
candidates = df[mask].copy()
# Collect track_ids as integers where possible
track_ids = []
for tid in candidates['track_id'].tolist():
    try:
        track_ids.append(int(tid))
    except:
        try:
            track_ids.append(int(float(tid)))
        except:
            pass

records = candidates[['track_id','title','artist','album','year']].to_dict(orient='records')
output = {'track_ids': track_ids, 'records': records}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_CNN3yRYVvkJfCft81uiH2XO5': 'file_storage/call_CNN3yRYVvkJfCft81uiH2XO5.json'}

exec(code, env_args)
