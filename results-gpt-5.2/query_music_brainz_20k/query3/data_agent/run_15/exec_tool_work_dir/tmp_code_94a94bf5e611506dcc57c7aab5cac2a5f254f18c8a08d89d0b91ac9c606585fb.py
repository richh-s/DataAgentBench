code = """import json, pandas as pd, re

# Load sales top track_ids
p_sales = var_call_MyiQC9FTKmfx2PMTMRKQJG5M
with open(p_sales, 'r', encoding='utf-8') as f:
    sales_top = json.load(f)

# Load tracks
p_tracks = var_call_on1zecCONevwsTf2H8yrYrf1
with open(p_tracks, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

df_sales = pd.DataFrame(sales_top)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

# canonicalize

def norm_text(x):
    if x is None:
        return ''
    x = str(x)
    if x.lower() == 'none':
        return ''
    x = x.strip().lower()
    x = re.sub(r"\s+", " ", x)
    return x

def norm_year(y):
    if y is None:
        return ''
    y = str(y).strip()
    if y.lower() == 'none' or y == '':
        return ''
    # extract 4-digit year if present
    m = re.search(r"(19\d{2}|20\d{2})", y)
    if m:
        return m.group(1)
    # 2-digit year
    m2 = re.fullmatch(r"'?(\d{2})", y)
    if m2:
        yy = int(m2.group(1))
        # heuristic: 00-25 => 2000-2025 else 1900s
        return str(2000+yy) if yy <= 25 else str(1900+yy)
    return ''

# create track lookup
track_df = pd.DataFrame(tracks)
track_df['track_id'] = track_df['track_id'].astype(int)
for c in ['title','artist','album','language']:
    track_df[c] = track_df[c].apply(norm_text)
track_df['year_n'] = track_df['year'].apply(norm_year)

# entity key primarily title+artist; if missing artist, try parsing from title "artist - title"

def split_artist_title(title, artist):
    if artist:
        return artist, title
    # patterns: "Artist - Title"; "Artist – Title"
    m = re.match(r"^([^\-–]+)\s*[\-–]\s*(.+)$", title)
    if m:
        a = norm_text(m.group(1))
        t = norm_text(m.group(2))
        return a, t
    return artist, title

adj_artist=[]
adj_title=[]
for t,a in zip(track_df['title'], track_df['artist']):
    aa,tt = split_artist_title(t,a)
    adj_artist.append(aa)
    adj_title.append(tt)
track_df['artist_n']=adj_artist
track_df['title_n']=adj_title

# Build entity key: title_n|artist_n (fallback: title_n|album)
track_df['entity_key'] = track_df.apply(lambda r: (r['title_n']+'|'+r['artist_n']) if r['artist_n']!='' else (r['title_n']+'|'+r['album']), axis=1)

# join sales top with tracks to get entity keys
merged = df_sales.merge(track_df[['track_id','entity_key','title_n','artist_n','album','year_n']], on='track_id', how='left')

# aggregate revenue by entity
ent = merged.groupby('entity_key', as_index=False)['total_revenue_usd'].sum().sort_values('total_revenue_usd', ascending=False)

# get top entity key and representative track info (most revenue track within entity)
top_key = ent.iloc[0]['entity_key']
top_rev = float(ent.iloc[0]['total_revenue_usd'])
sub = merged[merged['entity_key']==top_key].sort_values('total_revenue_usd', ascending=False)
rep = sub.iloc[0]
# find original (non-normalized) title/artist from track_df for rep track_id
rep_row = track_df[track_df['track_id']==int(rep['track_id'])].iloc[0]
# recover display title/artist from original records (use first matching track record)
orig = next((r for r in tracks if int(r['track_id'])==int(rep['track_id'])), None)

display_title = (orig.get('title') if orig else rep_row['title_n'])
display_artist = (orig.get('artist') if orig else rep_row['artist_n'])

result = {
    'title': display_title,
    'artist': display_artist,
    'total_revenue_usd': round(top_rev, 2),
    'entity_key': top_key
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_MyiQC9FTKmfx2PMTMRKQJG5M': 'file_storage/call_MyiQC9FTKmfx2PMTMRKQJG5M.json', 'var_call_on1zecCONevwsTf2H8yrYrf1': 'file_storage/call_on1zecCONevwsTf2H8yrYrf1.json'}

exec(code, env_args)
