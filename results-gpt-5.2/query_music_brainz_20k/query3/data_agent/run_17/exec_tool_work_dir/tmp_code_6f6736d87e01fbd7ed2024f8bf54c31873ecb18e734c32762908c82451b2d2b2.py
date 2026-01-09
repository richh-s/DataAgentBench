code = """import json, pandas as pd, re

# load sales totals
sales_src = var_call_KdLAAQDs6smQ0feiHpkRNNkg
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales_records = json.load(f)
else:
    sales_records = sales_src

tracks_src = var_call_zOXjXI8QpfIabIeYFxi5PAVg
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        track_records = json.load(f)
else:
    track_records = tracks_src

sales_df = pd.DataFrame(sales_records)
tracks_df = pd.DataFrame(track_records)

# types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# normalize for entity resolution
stop_words = set(['the','a','an','and','feat','featuring','ft','remix','live','version','edit','radio','mix','acoustic','demo','original','bonus','deluxe'])

def norm_text(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"\[.*?\]", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    toks = [t for t in s.split() if t and t not in stop_words]
    return ' '.join(toks)

def norm_artist(s):
    s = norm_text(s)
    # common separators in title fields are handled later
    return s

def norm_title(s):
    s = '' if s is None or str(s).lower()=='none' else str(s)
    # if title embeds artist like "Artist - Track" take right part
    if ' - ' in s:
        parts = s.split(' - ')
        if len(parts)>=2:
            s = parts[-1]
    return norm_text(s)

def norm_album(s):
    return norm_text(s)

def norm_year(y):
    if y is None or str(y).lower()=='none':
        return None
    y = str(y).strip().strip("'")
    m = re.search(r"(19\d{2}|20\d{2})", y)
    if m:
        return int(m.group(1))
    # two-digit year
    m2 = re.fullmatch(r"\d{2}", y)
    if m2:
        yy = int(y)
        return 1900+yy if yy>=50 else 2000+yy
    return None

tracks_df['n_title'] = tracks_df['title'].apply(norm_title)
tracks_df['n_artist'] = tracks_df['artist'].apply(norm_artist)
tracks_df['n_album'] = tracks_df['album'].apply(norm_album)
tracks_df['n_year'] = tracks_df['year'].apply(norm_year)

# If artist missing but embedded in title as "Artist - Track", try extract

def extract_artist_from_title(t):
    if t is None or str(t).lower()=='none':
        return ''
    t = str(t)
    if ' - ' in t:
        return norm_text(t.split(' - ')[0])
    return ''

mask_missing_artist = tracks_df['n_artist'].eq('')
tracks_df.loc[mask_missing_artist, 'n_artist'] = tracks_df.loc[mask_missing_artist, 'title'].apply(extract_artist_from_title)

# build entity key: prefer (title, artist, album) else (title, artist)
tracks_df['entity_key'] = tracks_df.apply(lambda r: (r['n_title'], r['n_artist'], r['n_album']) if r['n_album']!='' else (r['n_title'], r['n_artist']), axis=1)

# merge sales totals with track metadata
m = sales_df.merge(tracks_df[['track_id','entity_key','title','artist','album','year']], on='track_id', how='left')

# aggregate revenue by entity_key
agg = m.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
agg = agg.sort_values('total_revenue_usd', ascending=False)

top_key = agg.iloc[0]['entity_key']
top_rev = float(agg.iloc[0]['total_revenue_usd'])

# pick a representative track row with that key (highest individual track revenue)
rep = m[m['entity_key']==top_key].sort_values('total_revenue_usd', ascending=False).iloc[0]
answer = {
    'title': None if pd.isna(rep['title']) else str(rep['title']),
    'artist': None if pd.isna(rep['artist']) else str(rep['artist']),
    'album': None if pd.isna(rep['album']) else str(rep['album']),
    'year': None if pd.isna(rep['year']) else str(rep['year']),
    'total_revenue_usd': round(top_rev, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_KdLAAQDs6smQ0feiHpkRNNkg': 'file_storage/call_KdLAAQDs6smQ0feiHpkRNNkg.json', 'var_call_zOXjXI8QpfIabIeYFxi5PAVg': 'file_storage/call_zOXjXI8QpfIabIeYFxi5PAVg.json'}

exec(code, env_args)
