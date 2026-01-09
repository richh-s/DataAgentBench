code = """import json, pandas as pd, re

# load sales by track_id
sales_src = var_call_dAapA6OfgVkdmMTpfLd261s5
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

tracks_src = var_call_5poOF8vgF2kj4xJ3FwCsKEc2
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

sales_df = pd.DataFrame(sales)
tracks_df = pd.DataFrame(tracks)

# types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# normalize
def norm_txt(x):
    if x is None:
        return ''
    x = str(x)
    if x.lower() == 'none':
        return ''
    x = x.lower().strip()
    x = re.sub(r"\s+", " ", x)
    x = re.sub(r"\s*[-–—]\s*", " - ", x)
    return x

def norm_year(y):
    if y is None:
        return None
    y = str(y).strip()
    if y.lower() == 'none' or y == '':
        return None
    y = y.strip("'")
    digits = re.findall(r"\d{2,4}", y)
    if not digits:
        return None
    d = digits[0]
    if len(d) == 4:
        return int(d)
    if len(d) == 2:
        yy = int(d)
        # heuristic: 00-26 => 2000s else 1900s
        return 2000 + yy if yy <= 26 else 1900 + yy
    if len(d) == 3:
        return int(d)
    return None

tracks_df['t_title'] = tracks_df['title'].map(norm_txt)
tracks_df['t_artist'] = tracks_df['artist'].map(norm_txt)
tracks_df['t_album'] = tracks_df['album'].map(norm_txt)
tracks_df['y_norm'] = tracks_df['year'].map(norm_year)

# resolve embedded artist in title like "Artist - Track"
def split_artist_title(t):
    if not t:
        return ('', '')
    parts = t.split(' - ', 1)
    if len(parts)==2 and len(parts[0])>0 and len(parts[1])>0:
        return (parts[0].strip(), parts[1].strip())
    return ('', t)

spl = tracks_df['t_title'].map(split_artist_title)
tracks_df['emb_artist'] = [a for a,_ in spl]
tracks_df['emb_title'] = [b for _,b in spl]

# canonical artist/title
tracks_df['c_artist'] = tracks_df.apply(lambda r: r['t_artist'] if r['t_artist'] else r['emb_artist'], axis=1)
tracks_df['c_title'] = tracks_df.apply(lambda r: r['emb_title'] if r['emb_artist'] else r['t_title'], axis=1)

# basic cleanup of title suffixes like live/remaster in parentheses (keep core)
def core_title(t):
    t = t or ''
    t = re.sub(r"\(.*?\)", "", t)
    t = re.sub(r"\[.*?\]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t
tracks_df['core_title'] = tracks_df['c_title'].map(core_title)

# entity key: artist + core_title + album (if present) + year (if present)
# use album if exists else blank; year optional
tracks_df['key'] = tracks_df.apply(lambda r: "|".join([
    r['c_artist'],
    r['core_title'],
    r['t_album'],
    str(r['y_norm']) if pd.notna(r['y_norm']) else ''
]), axis=1)

# join revenue onto tracks then aggregate by key
merged = sales_df.merge(tracks_df[['track_id','key','c_title','c_artist','t_album','y_norm']], on='track_id', how='left')
agg = merged.groupby('key', as_index=False)['total_revenue_usd'].sum()

top = agg.sort_values('total_revenue_usd', ascending=False).head(1)
top_key = top.iloc[0]['key']
top_rev = float(top.iloc[0]['total_revenue_usd'])

# pick a representative track metadata for that key (most complete)
rep = tracks_df[tracks_df['key']==top_key].copy()
rep['comp'] = (rep['c_artist'].ne('').astype(int) + rep['c_title'].ne('').astype(int) + rep['t_album'].ne('').astype(int) + rep['y_norm'].notna().astype(int))
rep = rep.sort_values(['comp','track_id'], ascending=[False, True]).head(1)
rep_row = rep.iloc[0]

result = {
    'title': rep_row['c_title'],
    'artist': rep_row['c_artist'] if rep_row['c_artist'] else None,
    'album': rep_row['t_album'] if rep_row['t_album'] else None,
    'year': int(rep_row['y_norm']) if pd.notna(rep_row['y_norm']) else None,
    'total_revenue_usd': round(top_rev, 2)
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_dAapA6OfgVkdmMTpfLd261s5': 'file_storage/call_dAapA6OfgVkdmMTpfLd261s5.json', 'var_call_5poOF8vgF2kj4xJ3FwCsKEc2': 'file_storage/call_5poOF8vgF2kj4xJ3FwCsKEc2.json'}

exec(code, env_args)
