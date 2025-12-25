code = """import json, pandas as pd

tracks_path = var_call_XLTN4Hh4aGg02bjQo0pim5UG
sales_path = var_call_qVUKlIZvYbww95kruFtoAzGL

with open(tracks_path, 'r') as f:
    tracks = json.load(f)
with open(sales_path, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalization helper
def norm_text(s):
    if pd.isna(s) or s in [None, 'None', '']:
        return None
    return ' '.join(str(s).lower().strip().replace('\n', ' ').split())

for col in ['title', 'artist', 'album', 'year']:
    tracks_df[col + '_norm'] = tracks_df[col].apply(norm_text)

tracks_df['canon_key'] = tracks_df[['title_norm', 'artist_norm', 'album_norm']].astype(str).agg(' | '.join, axis=1)

track_id_to_key = tracks_df.set_index('track_id')['canon_key'].to_dict()

sales_df['canon_key'] = sales_df['track_id'].map(track_id_to_key)

rev_by_track = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].astype(float).sum().reset_index()

max_row = rev_by_track.loc[rev_by_track['revenue_usd'].idxmax()]
max_key = max_row['canon_key']
max_revenue = float(max_row['revenue_usd'])

rep_track = tracks_df[tracks_df['canon_key'] == max_key].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'year': rep_track['year'],
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_XLTN4Hh4aGg02bjQo0pim5UG': 'file_storage/call_XLTN4Hh4aGg02bjQo0pim5UG.json', 'var_call_qVUKlIZvYbww95kruFtoAzGL': 'file_storage/call_qVUKlIZvYbww95kruFtoAzGL.json'}

exec(code, env_args)
