code = """import json, pandas as pd

# Load aggregated sales (sorted by revenue desc) from file
path_sales = var_call_HvQU2jlD8yAZazzXzBWaLSWh
with open(path_sales, 'r') as f:
    sales_agg = json.load(f)

sales_df = pd.DataFrame(sales_agg)
# Ensure numeric
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# Take top-N candidate track_ids (e.g., 200) for efficiency
top_n = 200
candidate_ids = sales_df.head(top_n)['track_id'].tolist()

# Load all tracks
path_tracks = var_call_kELzxvcPrSNhYbyub08pTLXM
with open(path_tracks, 'r') as f:
    tracks = json.load(f)
tracks_df = pd.DataFrame(tracks)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Focus on candidates
cand_tracks = tracks_df[tracks_df['track_id'].isin(candidate_ids)].copy()

# Basic normalization helpers
import re

def norm_text(s):
    if s is None:
        return ''
    s = str(s).lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = s.strip()
    return s

cand_tracks['title_norm'] = cand_tracks['title'].apply(norm_text)
cand_tracks['artist_norm'] = cand_tracks['artist'].apply(norm_text)
cand_tracks['album_norm'] = cand_tracks['album'].apply(norm_text)

# Heuristic: same real-world song if normalized title and artist match and non-empty
cand_tracks['song_key'] = cand_tracks.apply(lambda r: (r['title_norm'], r['artist_norm']) if r['title_norm'] and r['artist_norm'] else None, axis=1)

# Map track_id -> song_key
id_to_key = dict(zip(cand_tracks['track_id'], cand_tracks['song_key']))

# Aggregate revenue by song_key among candidates
song_revenue = {}
for _, row in sales_df[sales_df['track_id'].isin(candidate_ids)].iterrows():
    tid = row['track_id']
    rev = row['total_revenue']
    key = id_to_key.get(tid)
    if key is None:
        # fallback: treat as its own key using track_id
        key = ('__id__', str(tid))
    song_revenue[key] = song_revenue.get(key, 0.0) + rev

# Find best key
best_key, best_rev = None, -1
for k, v in song_revenue.items():
    if v > best_rev:
        best_key, best_rev = k, v

# Collect representative track info for best_key
if best_key[0] == '__id__':
    best_track_ids = [int(best_key[1])]
else:
    best_track_ids = [tid for tid, sk in id_to_key.items() if sk == best_key]

best_tracks = cand_tracks[cand_tracks['track_id'].isin(best_track_ids)].copy()
rep = best_tracks.iloc[0].to_dict()

result = {
    'title': rep.get('title'),
    'artist': rep.get('artist'),
    'album': rep.get('album'),
    'approx_total_revenue_usd': round(float(best_rev), 2),
    'track_ids_contributing': best_track_ids,
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_HvQU2jlD8yAZazzXzBWaLSWh': 'file_storage/call_HvQU2jlD8yAZazzXzBWaLSWh.json', 'var_call_kELzxvcPrSNhYbyub08pTLXM': 'file_storage/call_kELzxvcPrSNhYbyub08pTLXM.json', 'var_call_GKgC0hMhpFxgbYI1r6yuJlXy': ['tracks'], 'var_call_CCclo8fEpCizTR3XaljzJN8E': ['sales']}

exec(code, env_args)
