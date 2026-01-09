code = """import json, pandas as pd

# Load full results from files
with open(var_call_K6pNnJA0y6eEPho7e0x3iJZ4, 'r', encoding='utf-8') as f:
    sales_by_track = json.load(f)
with open(var_call_03vrOZFdUe9s1kZ69WwVJPHI, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

df_sales = pd.DataFrame(sales_by_track)
df_tracks = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    df_sales[c] = df_sales[c].astype(int)
    df_tracks[c] = df_tracks[c].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

# Identify best real-world track via entity resolution.
# Start with naive grouping key: normalized title+artist+album; fall back when artist missing.

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.strip().lower()
    # simple normalization
    for ch in ['\u2019',"'",'"']:
        s = s.replace(ch,'')
    for ch in ['-','_','/','\\',':',';','(',')','[',']',',','.','!','?']:
        s = s.replace(ch,' ')
    s = ' '.join(s.split())
    return s

# compute key
nt = df_tracks.copy()
nt['t'] = nt['title'].apply(norm)
nt['a'] = nt['artist'].apply(norm)
nt['al'] = nt['album'].apply(norm)

# if title contains ' - ' pattern where artist embedded and artist field empty, split first token as artist
# but our norm removed '-', so use original title
import re

def extract_artist_from_title(row):
    artist = row['artist']
    if artist is not None and str(artist).lower() != 'none' and str(artist).strip() != '':
        return artist
    title = row['title']
    if title is None:
        return artist
    m = re.match(r"^\s*([^\-]{2,}?)\s*-\s*(.+)$", str(title))
    if m:
        return m.group(1).strip()
    return artist

nt['artist2'] = nt.apply(extract_artist_from_title, axis=1)
nt['a2'] = nt['artist2'].apply(norm)

# key uses a2 when available else a; album included
nt['entity_key'] = nt.apply(lambda r: '|'.join([r['t'], r['a2'] if r['a2'] else r['a'], r['al']]), axis=1)

# join sales to tracks to get entity_key and canonical fields
df = df_sales.merge(nt[['track_id','title','artist','artist2','album','year','entity_key']], on='track_id', how='left')

# group by entity_key to resolve duplicates
entity_rev = df.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()

# find top entity
top = entity_rev.sort_values('total_revenue_usd', ascending=False).head(1)
entity_key = top.iloc[0]['entity_key']
max_rev = float(top.iloc[0]['total_revenue_usd'])

# pick representative track row with highest individual revenue within that entity
cand = df[df['entity_key'] == entity_key].copy()
# attach per-track revenue
track_rev = cand.groupby('track_id')['total_revenue_usd'].sum().reset_index().sort_values('total_revenue_usd', ascending=False)
top_track_id = int(track_rev.iloc[0]['track_id'])
rep = nt[nt['track_id'] == top_track_id].iloc[0]

answer = {
    'track_id_representative': top_track_id,
    'title': rep['title'],
    'artist': rep['artist2'] if rep['artist2'] and norm(rep['artist2']) else rep['artist'],
    'album': rep['album'],
    'total_revenue_usd': round(max_rev, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_K6pNnJA0y6eEPho7e0x3iJZ4': 'file_storage/call_K6pNnJA0y6eEPho7e0x3iJZ4.json', 'var_call_03vrOZFdUe9s1kZ69WwVJPHI': 'file_storage/call_03vrOZFdUe9s1kZ69WwVJPHI.json', 'var_call_wpzP1hV7WKhfYIvv2QnuSgoX': [{'n_sales': '58049', 'n_track_ids': '19375'}], 'var_call_iiOtFqlN29Z6OtnFYQImaI5f': [{'n_tracks': '19375', 'n_titles': '18967', 'n_artists': '8994'}]}

exec(code, env_args)
