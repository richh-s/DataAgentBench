code = """import json
import pandas as pd
import re

# Load the data from the stored JSON files
tracks_path = var_call_0ZnSWFvlycp9mmAejt4MoYfC
sales_path = var_call_AV9LfnMmXb3PA0BHuKjtIvdV

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = pd.read_json(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = pd.read_json(f)

# Clean and convert types
sales['revenue_usd'] = pd.to_numeric(sales['revenue_usd'], errors='coerce').fillna(0.0)
tracks['track_id'] = tracks['track_id'].astype(str)
sales['track_id'] = sales['track_id'].astype(str)

# Normalize function
def normalize_text(s):
    if pd.isna(s):
        return None
    s = str(s)
    s = s.strip()
    if s.lower() in ['none', 'nan', '', 'null', "[unknown]", 'unknown']:
        return None
    # remove parenthetical/bracketed content
    s = re.sub(r"\([^\)]*\)", "", s)
    s = re.sub(r"\[[^\]]*\]", "", s)
    # remove common live/remix tags after dash like " - live" if appears at end
    s = re.sub(r"-\s*(live|remix|remastered|acoustic|version).*", "", s, flags=re.I)
    s = s.strip()
    # remove punctuation except spaces and alphanumerics
    s = re.sub(r"[^0-9a-zA-Z\s]", "", s)
    s = re.sub(r"\s+", " ", s)
    s = s.lower()
    return s if s!="" else None

# Fix cases where title contains "Artist - Title" and artist missing
def split_title_artist(row):
    title = row['title']
    artist = row['artist']
    if (pd.isna(artist) or str(artist).strip().lower() in ['none', '', 'nan', 'null', '[unknown]']) and isinstance(title, str):
        # if there's a hyphen separating artist and title
        if ' - ' in title:
            parts = title.split(' - ', 1)
            # heuristics: if left part contains letters and right part more likely the title
            left, right = parts[0].strip(), parts[1].strip()
            # assign
            return pd.Series({'title': right, 'artist': left})
    return pd.Series({'title': title, 'artist': artist})

tracks[['title','artist']] = tracks.apply(split_title_artist, axis=1)

# Add normalized columns
tracks['n_title'] = tracks['title'].apply(normalize_text)
tracks['n_artist'] = tracks['artist'].apply(normalize_text)

# Create an entity key: prefer (title+artist). If artist missing, use title only.
tracks['entity_key'] = tracks.apply(lambda r: (r['n_title'] + '||' + r['n_artist']) if r['n_title'] and r['n_artist'] else (r['n_title'] if r['n_title'] else None), axis=1)

# Merge sales with tracks to get track metadata
merged = sales.merge(tracks[['track_id','title','artist','n_title','n_artist','entity_key']], on='track_id', how='left')

# For sales where entity_key is null (no matching track or no title), fallback to track_id as entity
merged['entity_key'] = merged['entity_key'].fillna('trackid||' + merged['track_id'])

# Aggregate revenue by entity_key
agg = merged.groupby('entity_key', dropna=False).agg(
    total_revenue_usd = ('revenue_usd','sum'),
    sales_count = ('sale_id','count')
).reset_index()

# Get top entity
agg_sorted = agg.sort_values('total_revenue_usd',ascending=False)
if agg_sorted.shape[0]==0:
    result = {"title": None, "artist": None, "total_revenue_usd": 0.0, "track_ids": [], "sales_count": 0}
else:
    top = agg_sorted.iloc[0]
    key = top['entity_key']
    total = float(top['total_revenue_usd'])
    scount = int(top['sales_count'])
    # get representative title/artist and track_ids contributing to this entity
    members = merged[merged['entity_key']==key]
    # choose most common non-null title and artist
    rep_title = None
    rep_artist = None
    if members['title'].dropna().shape[0]>0:
        rep_title = members['title'].dropna().mode().iloc[0]
    if members['artist'].dropna().shape[0]>0:
        rep_artist = members['artist'].dropna().mode().iloc[0]
    track_ids = sorted(list(set(members['track_id'].astype(int).tolist())))
    result = {"title": rep_title, "artist": rep_artist, "total_revenue_usd": round(total,2), "track_ids": track_ids, "sales_count": scount}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0QK7sMU2LC9eABOlo8mS3VtK': ['tracks'], 'var_call_oUhtyiE4TnoyzHVPWdO6w3E0': ['sales'], 'var_call_0ZnSWFvlycp9mmAejt4MoYfC': 'file_storage/call_0ZnSWFvlycp9mmAejt4MoYfC.json', 'var_call_AV9LfnMmXb3PA0BHuKjtIvdV': 'file_storage/call_AV9LfnMmXb3PA0BHuKjtIvdV.json'}

exec(code, env_args)
