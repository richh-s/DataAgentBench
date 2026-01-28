code = """import json
import pandas as pd
import re

# Load data from previous tool calls
tracks_path = var_call_Q5o9ZmtcWis0gNhW0bhh6xc3
sales_path = var_call_tnoQtXnBaToewiAWMk3EBTyk

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks_list = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales_list = json.load(f)

tracks = pd.DataFrame(tracks_list)
sales = pd.DataFrame(sales_list)

# Ensure correct types
tracks['track_id'] = tracks['track_id'].astype(str)
sales['track_id'] = sales['track_id'].astype(str)

# Convert revenue to float
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

# Normalization functions

def clean_text(s):
    if s is None:
        return ''
    s = str(s).strip()
    if s.lower() in ('none', "nan", ''):
        return ''
    # remove parenthetical content
    s = re.sub(r"\(.*?\)", "", s)
    # remove punctuation except alphanumeric and spaces
    s = re.sub(r"[^0-9a-zA-Z\s]", "", s)
    # collapse whitespace and lowercase
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s

def clean_year(y):
    if y is None:
        return ''
    y = str(y).strip()
    if y.lower() in ('none', "nan", ""):
        return ''
    # extract 4-digit or 2-digit numbers
    m = re.search(r"(\d{4})", y)
    if m:
        return m.group(1)
    m2 = re.search(r"(\d{2})", y)
    if m2:
        return m2.group(1)
    return re.sub(r"[^0-9]", "", y)

# Create normalized signature for entity resolution
tracks['norm_title'] = tracks['title'].apply(clean_text)
tracks['norm_artist'] = tracks['artist'].apply(clean_text)
tracks['norm_album'] = tracks['album'].apply(clean_text)
tracks['norm_year'] = tracks['year'].apply(clean_year)

tracks['signature'] = tracks['norm_title'] + ' | ' + tracks['norm_artist'] + ' | ' + tracks['norm_album'] + ' | ' + tracks['norm_year']

# For signatures that are empty (all fields missing), fall back to title only
tracks.loc[tracks['signature'].str.strip() == ' |  |  | ', 'signature'] = tracks.loc[tracks['signature'].str.strip() == ' |  |  | ', 'norm_title']

# Map track_id to signature
trackid_to_sig = tracks.set_index('track_id')['signature'].to_dict()

# Aggregate sales by track_id
sales_agg = sales.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Map to signature; if a track_id missing in tracks, set signature to 'UNKNOWN_<id>'
def map_sig(tid):
    return trackid_to_sig.get(tid, f'__UNKNOWN__{tid}')

sales_agg['signature'] = sales_agg['track_id'].apply(map_sig)

# Aggregate revenue by signature
rev_by_sig = sales_agg.groupby('signature', as_index=False)['revenue_usd'].sum()

# Find max revenue signature
rev_by_sig_sorted = rev_by_sig.sort_values('revenue_usd', ascending=False)
if rev_by_sig_sorted.shape[0] == 0:
    result = {
        'title': None,
        'artist': None,
        'total_revenue_usd': 0.0,
        'track_ids': [],
        'num_duplicates': 0
    }
else:
    top = rev_by_sig_sorted.iloc[0]
    top_sig = top['signature']
    top_revenue = float(top['revenue_usd'])
    # find all track_ids with this signature
    tids = tracks[tracks['signature'] == top_sig]['track_id'].tolist()
    # choose representative title and artist: most common non-empty
    def choose_rep(col):
        vals = tracks[tracks['signature'] == top_sig][col].fillna('').astype(str)
        vals = [v for v in vals if v.strip().lower() not in ('', 'none')]
        return vals[0] if len(vals) > 0 else ''
    rep_title = choose_rep('title')
    rep_artist = choose_rep('artist')
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(top_revenue, 2),
        'track_ids': tids,
        'num_duplicates': len(tids),
        'signature': top_sig
    }

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Q5o9ZmtcWis0gNhW0bhh6xc3': 'file_storage/call_Q5o9ZmtcWis0gNhW0bhh6xc3.json', 'var_call_tnoQtXnBaToewiAWMk3EBTyk': 'file_storage/call_tnoQtXnBaToewiAWMk3EBTyk.json'}

exec(code, env_args)
