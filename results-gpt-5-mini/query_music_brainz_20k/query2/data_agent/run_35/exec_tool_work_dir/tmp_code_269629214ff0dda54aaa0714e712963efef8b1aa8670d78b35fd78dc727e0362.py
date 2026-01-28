code = """import pandas as pd
import json
# var_call_CNN3yRYVvkJfCft81uiH2XO5 is available from previous query
df = pd.DataFrame(var_call_CNN3yRYVvkJfCft81uiH2XO5)
# Normalize
df['title_low'] = df['title'].fillna('').str.lower()
df['artist_low'] = df['artist'].fillna('').str.lower()
# helper normalized title without spaces
df['title_nospace'] = df['title_low'].str.replace(' ', '')
# Select candidate rows: title contains 'street' and (title contains 'hype' or title_nospace contains 'streethype') OR artist contains 'maginnis'
mask = ((df['title_low'].str.contains('street') & df['title_low'].str.contains('hype', na=False)) | (df['title_nospace'].str.contains('streethype', na=False)) | (df['artist_low'].str.contains('maginnis', na=False) & df['title_low'].str.contains('street', na=False)))
candidates = df[mask].copy()
# Extract track_ids
track_ids = candidates['track_id'].tolist()
# Also include unique mapping of track_id to title and artist for inspection
records = candidates[['track_id','title','artist','album','year']].to_dict(orient='records')
output = {'track_ids': track_ids, 'records': records}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_CNN3yRYVvkJfCft81uiH2XO5': 'file_storage/call_CNN3yRYVvkJfCft81uiH2XO5.json'}

exec(code, env_args)
