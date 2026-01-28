code = """import json
import pandas as pd

# Load the JSON results from the stored files
with open(var_call_vsCuleE6xfbHqTc3uQ9bJmpu, 'r') as f:
    tracks = json.load(f)
with open(var_call_t31GWiyO2Rts8xsCrIVA0L9W, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize columns and types
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
for col in ['title','artist','album','year','language','length']:
    if col in tracks_df.columns:
        tracks_df[col] = tracks_df[col].fillna('')

sales_df['track_id'] = sales_df['track_id'].astype(str)
# Convert revenue to float
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0)

# Heuristic entity resolution: derive canonical artist and title
import re

def clean_text(s):
    if s is None:
        return ''
    s = str(s)
    # remove parenthetical/bracket content
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"\[[^]]*\]", "", s)
    s = s.replace("\u2013", "-")
    s = s.replace("\u2014", "-")
    # remove extra punctuation except hyphen and apostrophe
    s = re.sub(r"[^\w\s\-']", ' ', s)
    s = re.sub(r"\s+", ' ', s)
    s = s.strip().lower()
    return s

# Parse artist from title if artist field missing or placeholder
def derive_artist_title(row):
    title = str(row.get('title','') or '')
    artist = str(row.get('artist','') or '')
    title_c = clean_text(title)
    artist_c = clean_text(artist)
    # consider artist missing if empty or contains 'none' or 'unknown' or only whitespace
    if artist_c in ['', 'none', '[unknown]', 'unknown', '   ']:
        # try split by ' - ' or ' – '
        parts = re.split(r"\s-\s|\s–\s|\s—\s", title)
        if len(parts) >= 2:
            possible_artist = clean_text(parts[0])
            possible_title = clean_text(' - '.join(parts[1:]))
            # Heuristic: if possible_artist contains a space and letters, use it
            if re.search(r"[a-zA-Z]", possible_artist) and len(possible_artist) <= 60:
                return possible_artist, possible_title
        # fallback: keep artist blank and cleaned title
        return '', title_c
    else:
        # artist present, clean title but if title includes artist prefix, remove it
        # remove leading artist from title if it repeats
        # find artist token inside title start
        t = title
        # case-insensitive check
        pat = re.compile(re.escape(artist), re.IGNORECASE)
        if artist and pat.match(title):
            # remove the matching prefix from title
            new_title = pat.sub('', title, count=1)
            new_title = new_title.lstrip(' -:')
            return clean_text(artist), clean_text(new_title)
        return clean_text(artist), title_c

tracks_df[['canonical_artist','canonical_title']] = tracks_df.apply(lambda r: pd.Series(derive_artist_title(r)), axis=1)

# For further normalization of titles, remove common suffixes like live, remix, acoustic, version, remaster
def normalize_song_title(t):
    t = str(t)
    # remove descriptors
    t = re.sub(r"\b(live|remix|acoustic|version|demo|edit|original|remastered|instrumental)\b", '', t)
    t = re.sub(r"\bfeat\b|\bft\b", '', t)
    t = re.sub(r"\s+", ' ', t)
    return t.strip()

tracks_df['canonical_title'] = tracks_df['canonical_title'].apply(normalize_song_title)
tracks_df['canonical_artist'] = tracks_df['canonical_artist'].apply(lambda x: x.strip())

# Now join sales to tracks
merged = sales_df.merge(tracks_df[['track_id','canonical_artist','canonical_title','title','artist']], on='track_id', how='left')

# For any sales rows without matching track metadata (should be rare), use unknown placeholders
merged['canonical_artist'] = merged['canonical_artist'].fillna('')
merged['canonical_title'] = merged['canonical_title'].fillna(merged['title'].fillna('').apply(clean_text))

# Aggregate revenue by canonical artist + canonical title
grouped = merged.groupby(['canonical_artist','canonical_title'], dropna=False)['revenue_usd'].sum().reset_index()
# Find max
top = grouped.sort_values('revenue_usd', ascending=False).head(1)

if top.empty:
    result = {"title":"","artist":"","total_revenue_usd":0.0,"matching_track_ids":[]}
else:
    artist = top.iloc[0]['canonical_artist']
    title = top.iloc[0]['canonical_title']
    total = float(top.iloc[0]['revenue_usd'])
    # find matching track_ids
    matches = merged[(merged['canonical_artist']==artist)&(merged['canonical_title']==title)]['track_id'].unique().tolist()
    result = {"title": title, "artist": artist, "total_revenue_usd": round(total,2), "matching_track_ids": matches}

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vsCuleE6xfbHqTc3uQ9bJmpu': 'file_storage/call_vsCuleE6xfbHqTc3uQ9bJmpu.json', 'var_call_t31GWiyO2Rts8xsCrIVA0L9W': 'file_storage/call_t31GWiyO2Rts8xsCrIVA0L9W.json'}

exec(code, env_args)
