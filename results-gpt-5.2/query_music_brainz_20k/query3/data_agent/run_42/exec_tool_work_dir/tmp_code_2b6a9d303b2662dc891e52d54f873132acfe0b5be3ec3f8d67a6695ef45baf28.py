code = """import json, pandas as pd

# Load tracks table (may be a path)
tracks_data = var_call_4TPWf0FEjoz9zJeVMCTttOwo
if isinstance(tracks_data, str):
    import pathlib
    p = pathlib.Path(tracks_data)
    tracks = json.loads(p.read_text())
else:
    tracks = tracks_data

tracks_df = pd.DataFrame(tracks)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

# Top track_ids by revenue
top_df = pd.DataFrame(var_call_zVMpoBQXcetoVOLSA7Okg5TO)
top_df['track_id'] = top_df['track_id'].astype(str)
top_df['total_revenue_usd'] = top_df['total_revenue_usd'].astype(float)

# Join to get metadata
joined = top_df.merge(tracks_df[['track_id','title','artist','album','year']], on='track_id', how='left')

# Entity resolution: normalize key based on title+artist+album (year ignored due to format variability)
def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    return ' '.join(''.join(ch.lower() if ch.isalnum() else ' ' for ch in s).split())

for col in ['title','artist','album']:
    joined[col] = joined[col].where(joined[col].notna(), None)

joined['key'] = joined.apply(lambda r: norm(r['title'])+'|'+norm(r['artist'])+'|'+norm(r['album']), axis=1)

# If artist missing but embedded in title like "Artist - Track", try extract for key
import re

def split_artist_title(title):
    if title is None:
        return (None, None)
    t = str(title)
    m = re.match(r"^\s*(.*?)\s+-\s+(.*)\s*$", t)
    if m:
        return (m.group(1), m.group(2))
    return (None, None)

ex_artist = []
ex_title = []
for t in joined['title'].tolist():
    a, tt = split_artist_title(t)
    ex_artist.append(a)
    ex_title.append(tt)
joined['artist_extracted'] = ex_artist
joined['title_extracted'] = ex_title

joined['artist_for_key'] = joined.apply(lambda r: r['artist'] if norm(r['artist'])!='' else r['artist_extracted'], axis=1)
joined['title_for_key'] = joined.apply(lambda r: r['title'] if r['title_extracted'] is None else r['title_extracted'], axis=1)
joined['key2'] = joined.apply(lambda r: norm(r['title_for_key'])+'|'+norm(r['artist_for_key'])+'|'+norm(r['album']), axis=1)

# Determine all track_ids that match the top track's entity key2
best_track_id = top_df.sort_values('total_revenue_usd', ascending=False).iloc[0]['track_id']
best_row = joined[joined['track_id']==best_track_id].iloc[0]
best_key = best_row['key2']

# Candidate duplicates in full tracks table based on same normalized (title, artist, album), with same extraction heuristic
all_tracks = tracks_df.copy()
all_tracks['artist_extracted'] = all_tracks['title'].apply(lambda t: split_artist_title(t)[0])
all_tracks['title_extracted'] = all_tracks['title'].apply(lambda t: split_artist_title(t)[1])
all_tracks['artist_for_key'] = all_tracks.apply(lambda r: r['artist'] if norm(r['artist'])!='' else r['artist_extracted'], axis=1)
all_tracks['title_for_key'] = all_tracks.apply(lambda r: r['title'] if r['title_extracted'] is None else r['title_extracted'], axis=1)
all_tracks['key2'] = all_tracks.apply(lambda r: norm(r['title_for_key'])+'|'+norm(r['artist_for_key'])+'|'+norm(r['album']), axis=1)

dup_ids = all_tracks.loc[all_tracks['key2']==best_key, 'track_id'].astype(str).tolist()

result = {
    'top_track_id': best_track_id,
    'entity_key': best_key,
    'dup_track_ids_count': len(dup_ids),
    'dup_track_ids_sample': dup_ids[:20],
    'best_metadata': {
        'title': best_row.get('title'),
        'artist': best_row.get('artist') if best_row.get('artist') not in [None,'None'] else best_row.get('artist_extracted'),
        'album': best_row.get('album'),
        'year': best_row.get('year')
    },
    'top_track_revenue_single_track_id_usd': float(top_df.loc[top_df['track_id']==best_track_id, 'total_revenue_usd'].iloc[0]),
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zVMpoBQXcetoVOLSA7Okg5TO': [{'track_id': '14719', 'total_revenue_usd': '2522.82'}, {'track_id': '5124', 'total_revenue_usd': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue_usd': '2500.72'}, {'track_id': '6725', 'total_revenue_usd': '2489.81'}, {'track_id': '10377', 'total_revenue_usd': '2466.71'}, {'track_id': '5050', 'total_revenue_usd': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue_usd': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue_usd': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue_usd': '2428.2200000000003'}, {'track_id': '964', 'total_revenue_usd': '2425.61'}, {'track_id': '12984', 'total_revenue_usd': '2401.71'}, {'track_id': '6208', 'total_revenue_usd': '2385.0299999999997'}, {'track_id': '666', 'total_revenue_usd': '2382.74'}, {'track_id': '12620', 'total_revenue_usd': '2377.59'}, {'track_id': '19232', 'total_revenue_usd': '2368.7499999999995'}, {'track_id': '17757', 'total_revenue_usd': '2365.59'}, {'track_id': '3462', 'total_revenue_usd': '2359.23'}, {'track_id': '9639', 'total_revenue_usd': '2351.68'}, {'track_id': '18760', 'total_revenue_usd': '2349.33'}, {'track_id': '2516', 'total_revenue_usd': '2346.18'}, {'track_id': '6326', 'total_revenue_usd': '2331.91'}, {'track_id': '5836', 'total_revenue_usd': '2321.31'}, {'track_id': '9988', 'total_revenue_usd': '2317.41'}, {'track_id': '18508', 'total_revenue_usd': '2308.44'}, {'track_id': '10760', 'total_revenue_usd': '2293.1099999999997'}, {'track_id': '9002', 'total_revenue_usd': '2288.23'}, {'track_id': '14169', 'total_revenue_usd': '2281.23'}, {'track_id': '9649', 'total_revenue_usd': '2276.7200000000003'}, {'track_id': '10856', 'total_revenue_usd': '2275.85'}, {'track_id': '7422', 'total_revenue_usd': '2275.04'}, {'track_id': '8705', 'total_revenue_usd': '2273.46'}, {'track_id': '5933', 'total_revenue_usd': '2271.62'}, {'track_id': '5809', 'total_revenue_usd': '2269.24'}, {'track_id': '16084', 'total_revenue_usd': '2259.8599999999997'}, {'track_id': '9652', 'total_revenue_usd': '2251.2200000000003'}, {'track_id': '3412', 'total_revenue_usd': '2250.04'}, {'track_id': '15664', 'total_revenue_usd': '2249.3900000000003'}, {'track_id': '12207', 'total_revenue_usd': '2248.7200000000003'}, {'track_id': '5467', 'total_revenue_usd': '2246.94'}, {'track_id': '13102', 'total_revenue_usd': '2244.51'}, {'track_id': '4145', 'total_revenue_usd': '2243.27'}, {'track_id': '13132', 'total_revenue_usd': '2238.21'}, {'track_id': '13211', 'total_revenue_usd': '2233.62'}, {'track_id': '2244', 'total_revenue_usd': '2230.04'}, {'track_id': '18846', 'total_revenue_usd': '2227.95'}, {'track_id': '2029', 'total_revenue_usd': '2226.42'}, {'track_id': '3488', 'total_revenue_usd': '2222.25'}, {'track_id': '17669', 'total_revenue_usd': '2212.4700000000003'}, {'track_id': '12969', 'total_revenue_usd': '2211.97'}, {'track_id': '12551', 'total_revenue_usd': '2210.78'}], 'var_call_4TPWf0FEjoz9zJeVMCTttOwo': 'file_storage/call_4TPWf0FEjoz9zJeVMCTttOwo.json', 'var_call_QAPXiw0hkyRLMnSGaE1pUX0C': [{'grand_total_revenue_usd': '16528140.350000285', 'n_sales': '58049'}], 'var_call_10QgbVWHzD9PwSsMoLcVWsJR': [{'n_tracks': '19375'}]}

exec(code, env_args)
