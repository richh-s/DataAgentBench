code = """import json
import pandas as pd
import re

# Load data
tracks_path = var_call_G6FzIukjR2235Ty5bjIQGYlP
sales_path = var_call_eYAcjsmmXFAqyHeMDoIpuKVU
with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Clean helper
def clean_null(x):
    if x is None:
        return None
    if isinstance(x, str):
        s = x.strip()
        if s == '' or s.lower() in ('none', 'nan', '[unknown]'):
            return None
        return s
    return x

for col in tracks_df.columns:
    tracks_df[col] = tracks_df[col].apply(clean_null)
for col in sales_df.columns:
    sales_df[col] = sales_df[col].apply(clean_null)

# Types
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Simple normalization
non_alnum = re.compile(r'[^0-9a-zA-Z ]+')

def normalize_text(s):
    if not s:
        return ''
    s = str(s).lower()
    s = s.replace('\n',' ').replace('\t',' ')
    s = re.sub(r'\s+', ' ', s)
    s = non_alnum.sub('', s)
    s = s.strip()
    return s

# Attempt to extract artist from title if artist missing using ' - ' pattern
def get_artist_title(row):
    title = row.get('title') or ''
    artist = row.get('artist') or ''
    if not artist and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2 and re.search('[A-Za-z]', parts[0]):
            artist = parts[0].strip()
            title = parts[1].strip()
    return title, artist

tracks_df['ex_title'], tracks_df['ex_artist'] = zip(*tracks_df.apply(get_artist_title, axis=1))
tracks_df['norm_title'] = tracks_df['ex_title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['ex_artist'].apply(normalize_text)

# If artist still empty, mark as unknown
tracks_df['norm_artist'] = tracks_df['norm_artist'].replace('', 'unknown')

# Canonical key
tracks_df['canon_key'] = tracks_df['norm_title'] + '||' + tracks_df['norm_artist']

# Representative title/artist per canon
rep = tracks_df.groupby('canon_key').agg({
    'ex_title': lambda x: next((v for v in x if v and v.strip()), ''),
    'ex_artist': lambda x: next((v for v in x if v and v.strip()), '')
}).reset_index()

# Map sales to canon_key
track_to_key = tracks_df.set_index('track_id')['canon_key'].to_dict()
sales_df['canon_key'] = sales_df['track_id'].map(track_to_key)
sales_df = sales_df[sales_df['canon_key'].notnull()]

rev = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].sum().reset_index()
rev = rev.merge(rep, on='canon_key', how='left')

rev['revenue_usd'] = rev['revenue_usd'].astype(float)
if len(rev) == 0:
    result = {'title': None, 'artist': None, 'total_revenue_usd': 0.0}
else:
    max_row = rev.loc[rev['revenue_usd'].idxmax()]
    title = max_row['ex_title'] if max_row['ex_title'] else None
    artist = max_row['ex_artist'] if max_row['ex_artist'] else None
    result = {'title': title, 'artist': artist, 'total_revenue_usd': round(float(max_row['revenue_usd']), 2)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_G6FzIukjR2235Ty5bjIQGYlP': 'file_storage/call_G6FzIukjR2235Ty5bjIQGYlP.json', 'var_call_eYAcjsmmXFAqyHeMDoIpuKVU': 'file_storage/call_eYAcjsmmXFAqyHeMDoIpuKVU.json'}

exec(code, env_args)
