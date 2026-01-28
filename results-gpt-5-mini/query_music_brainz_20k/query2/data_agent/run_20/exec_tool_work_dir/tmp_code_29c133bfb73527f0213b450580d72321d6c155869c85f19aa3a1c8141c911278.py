code = """import json
import pandas as pd

# Load the full query_db result from the tracks query stored in the provided file path
path = var_call_V4nnWuMRxYNuXATYoQaaiDHa
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)

# Ensure columns exist
for c in ['track_id','title','artist','album','year']:
    if c not in df.columns:
        df[c] = None

# Normalize helper
import re

def normalize_text(s):
    if s is None:
        return ''
    s = str(s).lower()
    s = re.sub(r"[^a-z0-9]", '', s)
    return s

# Create normalized fields
df['title_norm'] = df['title'].apply(normalize_text)
df['artist_norm'] = df['artist'].apply(lambda x: normalize_text(x if x not in ['None', None] else ''))

# Heuristics to identify variants of "Brucqe Maginnis - Street Hype"
matches = df[
    (
        df['title_norm'].str.contains('streethype', na=False)
    )
    |
    (
        df['title_norm'].str.contains('street', na=False) & df['title_norm'].str.contains('hype', na=False)
    )
    |
    (
        df['artist_norm'].str.contains('maginnis', na=False)
    )
    |
    (
        df['artist_norm'].str.contains('brucqe', na=False)
    )
    |
    (
        df['title_norm'].str.contains('sttreet', na=False) & df['title_norm'].str.contains('hype', na=False)
    )
]

# Extract unique track_ids
track_ids = sorted(list({int(x) for x in matches['track_id'].tolist()}))

# Fallback: if none found, try titles that contain 'street' and 'hype' with spaces (original)
if not track_ids:
    candidates = df[df['title'].str.lower().str.contains('street', na=False) & df['title'].str.lower().str.contains('hype', na=False)]
    track_ids = sorted(list({int(x) for x in candidates['track_id'].tolist()}))

result = {
    'track_ids': track_ids,
    'matched_rows_count': len(matches),
    'matched_preview': matches[['track_id','title','artist','album','year']].head(10).to_dict(orient='records')
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V4nnWuMRxYNuXATYoQaaiDHa': 'file_storage/call_V4nnWuMRxYNuXATYoQaaiDHa.json'}

exec(code, env_args)
