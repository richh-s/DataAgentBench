code = """import json, pandas as pd, re

def load(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

sales = load(var_call_OOxQcK4XWMGiVs4PSuvbWMlC)
tracks = load(var_call_sBpjjLvf7q3ew11uBL1iAkDy)

df_sales = pd.DataFrame(sales)
df_tracks = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    df_sales[c] = pd.to_numeric(df_sales[c], errors='coerce').astype('Int64')
    df_tracks[c] = pd.to_numeric(df_tracks[c], errors='coerce').astype('Int64')

df_sales['total_revenue_usd'] = pd.to_numeric(df_sales['total_revenue_usd'], errors='coerce')

# build canonical key for entity resolution
stopwords = set(['the','a','an','and','feat','ft','featuring','remix','edit','live','version','radio','mix','demo','acoustic','mono','stereo'])

def norm_text(s):
    if s is None or (isinstance(s,float) and pd.isna(s)):
        return ''
    s = str(s).lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"\[.*?\]", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    toks = [t for t in s.split() if t not in stopwords]
    return ' '.join(toks).strip()

def extract_year(y):
    if y is None or (isinstance(y,float) and pd.isna(y)):
        return None
    s = str(y)
    m = re.search(r"(19\d{2}|20\d{2})", s)
    if m:
        return int(m.group(1))
    return None

df_tracks['n_title'] = df_tracks['title'].map(norm_text)
df_tracks['n_artist'] = df_tracks['artist'].map(norm_text)
df_tracks['n_album'] = df_tracks['album'].map(norm_text)
df_tracks['y'] = df_tracks['year'].map(extract_year)

# key: title + artist; fallback to title+album if artist missing

def make_key(row):
    t = row['n_title']
    a = row['n_artist']
    al = row['n_album']
    if a:
        return f"t:{t}|a:{a}"
    elif al:
        return f"t:{t}|al:{al}"
    else:
        return f"t:{t}"

df_tracks['entity_key'] = df_tracks.apply(make_key, axis=1)

# join sales with track metadata
merged = df_sales.merge(df_tracks[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

# aggregate revenue by entity_key (resolved song)
agg = merged.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
agg = agg.sort_values('total_revenue_usd', ascending=False)

top_key = agg.iloc[0]['entity_key']
top_rev = float(agg.iloc[0]['total_revenue_usd'])

# pick representative track row with most revenue within entity
rep = merged[merged['entity_key'] == top_key].copy()
rep = rep.sort_values('total_revenue_usd', ascending=False)
rep_row = rep.iloc[0]

result = {
    'title': None if pd.isna(rep_row['title']) else str(rep_row['title']),
    'artist': None if pd.isna(rep_row['artist']) else str(rep_row['artist']),
    'album': None if pd.isna(rep_row['album']) else str(rep_row['album']),
    'year': None if pd.isna(rep_row['year']) else str(rep_row['year']),
    'total_revenue_usd': round(top_rev, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OOxQcK4XWMGiVs4PSuvbWMlC': 'file_storage/call_OOxQcK4XWMGiVs4PSuvbWMlC.json', 'var_call_sBpjjLvf7q3ew11uBL1iAkDy': 'file_storage/call_sBpjjLvf7q3ew11uBL1iAkDy.json'}

exec(code, env_args)
