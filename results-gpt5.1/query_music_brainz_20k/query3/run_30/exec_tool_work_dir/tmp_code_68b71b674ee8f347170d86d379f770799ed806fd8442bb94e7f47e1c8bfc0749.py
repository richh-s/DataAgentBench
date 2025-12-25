code = """import json, pandas as pd

# Load full datasets from files
tracks_path = var_call_2BApm1b8npyvVwlCFcOC15Wd
sales_path = var_call_qCgo4LOdtzU5zofOFGfR0cKt

with open(tracks_path, 'r') as f:
    tracks = json.load(f)
with open(sales_path, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert types
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Basic normalization helpers
def norm_text(s):
    if pd.isna(s):
        return None
    s = str(s).strip().lower()
    if s in ('none', '[unknown]', ''):
        return None
    return ' '.join(s.split())

for col in ['title', 'artist', 'album', 'year']:
    tracks_df[col + '_norm'] = tracks_df[col].apply(norm_text)

# For year, keep only last 4 digits if looks like a year, or last 2 digits fallback
import re

def norm_year(y):
    y = norm_text(y)
    if y is None:
        return None
    digits = re.findall(r"\d+", y)
    if not digits:
        return None
    d = digits[-1]
    if len(d) >= 4:
        return d[-4:]
    if len(d) == 2:
        # Assume 1900-1999 or 2000+ is not crucial for equality, just keep two digits
        return d
    return d

tracks_df['year_norm'] = tracks_df['year'].apply(norm_year)

# Create a simple canonical key: title + artist (normalized). Album/year only if present.
keys = []
for idx, row in tracks_df.iterrows():
    t = row['title_norm']
    a = row['artist_norm']
    if not t and not a:
        key = None
    else:
        parts = []
        if t:
            parts.append(t)
        if a:
            parts.append(a)
        if row['album_norm']:
            parts.append(row['album_norm'])
        if row['year_norm']:
            parts.append(row['year_norm'])
        key = ' | '.join(parts)
    keys.append(key)

tracks_df['canonical_key'] = keys

# If canonical_key missing, fall back to title only
tracks_df.loc[tracks_df['canonical_key'].isna() & tracks_df['title_norm'].notna(), 'canonical_key'] = tracks_df['title_norm']

# Join sales with canonical keys
sales_merged = sales_df.merge(tracks_df[['track_id', 'canonical_key', 'title', 'artist', 'album']], on='track_id', how='left')

# Group by canonical track and sum revenue
agg = sales_merged.groupby('canonical_key', dropna=False)['revenue_usd'].sum().reset_index()

# Find canonical_key with max revenue
max_row = agg.loc[agg['revenue_usd'].idxmax()]
canonical = max_row['canonical_key']
max_revenue = float(max_row['revenue_usd'])

# Get a representative record for that canonical track
rep = tracks_df[tracks_df['canonical_key'] == canonical].iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'canonical_key': canonical,
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2BApm1b8npyvVwlCFcOC15Wd': 'file_storage/call_2BApm1b8npyvVwlCFcOC15Wd.json', 'var_call_qCgo4LOdtzU5zofOFGfR0cKt': 'file_storage/call_qCgo4LOdtzU5zofOFGfR0cKt.json'}

exec(code, env_args)
