code = """import json
import pandas as pd
import unicodedata

# Load data from stored variables (file paths or lists)
tracks_input = var_call_HI9RMpq0yldFAgkj1jj9eCJS
sales_input = var_call_fkfJkuFP1KDHBjRoF1itvdec

# If the inputs are file paths (strings), read them
if isinstance(tracks_input, str):
    with open(tracks_input, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_input

if isinstance(sales_input, str):
    with open(sales_input, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_input

# Create DataFrames
df_tracks = pd.DataFrame(tracks)
# sales is aggregated already with total_revenue
df_sales = pd.DataFrame(sales)

# Ensure track_id types are strings for safe merge
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

# Merge sales totals with tracks
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Normalization helper
import re

def normalize_text(s):
    if s is None:
        return ''
    # convert to string
    s = str(s)
    # normalize unicode accents
    s = unicodedata.normalize('NFKD', s)
    # lower
    s = s.lower()
    # remove content in parentheses (common noise)
    s = re.sub(r"\([^)]*\)", "", s)
    # remove punctuation except spaces
    s = re.sub(r"[^0-9a-z\s]", " ", s)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Apply normalization to title and artist
for col in ['title', 'artist', 'album', 'year']:
    if col not in df.columns:
        df[col] = ''
    df['norm_' + col] = df[col].fillna('').apply(normalize_text)

# Entity resolution strategy: group primarily by normalized title + normalized artist
# We'll also compute uniqueness counts for album/year to help choose representative

group_cols = ['norm_title', 'norm_artist']

# Convert total_revenue to float
df['total_revenue'] = df['total_revenue'].astype(float)

agg = df.groupby(group_cols).agg(
    total_revenue_usd=pd.NamedAgg(column='total_revenue', aggfunc='sum'),
    track_ids=pd.NamedAgg(column='track_id', aggfunc=lambda x: sorted(list(set(x)))),
    titles=pd.NamedAgg(column='title', aggfunc=lambda x: list(x.dropna().unique())[:5]),
    artists=pd.NamedAgg(column='artist', aggfunc=lambda x: list(x.dropna().unique())[:5]),
    albums=pd.NamedAgg(column='album', aggfunc=lambda x: list(x.dropna().unique())[:5]),
    years=pd.NamedAgg(column='year', aggfunc=lambda x: list(x.dropna().unique())[:5]),
    count_records=pd.NamedAgg(column='track_id', aggfunc='nunique')
).reset_index()

# Find the group with maximum revenue
if agg.shape[0] == 0:
    result = {
        'title': None,
        'artist': None,
        'representative_album': None,
        'total_revenue_usd': 0.0,
        'track_ids': []
    }
else:
    top = agg.sort_values('total_revenue_usd', ascending=False).iloc[0]
    # choose representative title/artist/album/year
    rep_title = top['titles'][0] if top['titles'] else ''
    rep_artist = top['artists'][0] if top['artists'] else ''
    rep_album = top['albums'][0] if top['albums'] else ''
    rep_year = top['years'][0] if top['years'] else ''
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'representative_album': rep_album,
        'representative_year': rep_year,
        'total_revenue_usd': float(round(top['total_revenue_usd'], 2)),
        'track_ids': top['track_ids'],
        'grouping_key': {
            'norm_title': top['norm_title'],
            'norm_artist': top['norm_artist']
        }
    }

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6XRnL6hthZCNRkvK6PEeOUT1': ['tracks'], 'var_call_zcsZAsTwZz8pjvVRU9rI7XKS': ['sales'], 'var_call_HI9RMpq0yldFAgkj1jj9eCJS': 'file_storage/call_HI9RMpq0yldFAgkj1jj9eCJS.json', 'var_call_fkfJkuFP1KDHBjRoF1itvdec': 'file_storage/call_fkfJkuFP1KDHBjRoF1itvdec.json'}

exec(code, env_args)
