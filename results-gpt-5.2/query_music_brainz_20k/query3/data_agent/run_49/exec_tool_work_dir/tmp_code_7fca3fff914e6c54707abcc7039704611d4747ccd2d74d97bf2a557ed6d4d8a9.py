code = """import json, pandas as pd

# Load full results if stored as file paths

def load_tool_result(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

sales_top = load_tool_result(var_call_r7xoVgC8FruXLOm3r7Lnvk3M)
tracks_all = load_tool_result(var_call_yiX4IeJSBIRdWmysYdfnPyXL)

sales_df = pd.DataFrame(sales_top)
tracks_df = pd.DataFrame(tracks_all)

# normalize types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# take top N track_ids, then attempt entity resolution among them by canonical key
N = 200
cand_ids = set(sales_df.sort_values('total_revenue_usd', ascending=False).head(N)['track_id'])
sub_tracks = tracks_df[tracks_df['track_id'].isin(cand_ids)].copy()

def norm_str(x):
    if x is None:
        return ''
    x = str(x)
    if x.lower() == 'none' or x.strip() == '':
        return ''
    return ' '.join(x.strip().lower().replace('\u00a0',' ').split())

import re

def clean_title(t):
    t = norm_str(t)
    # remove bracketed content and common suffixes
    t = re.sub(r"\([^\)]*\)", " ", t)
    t = re.sub(r"\[[^\]]*\]", " ", t)
    t = re.sub(r"\s+-\s+.*$", "", t)  # drop after ' - '
    t = re.sub(r"[^a-z0-9]+", " ", t)
    t = ' '.join(t.split())
    return t

sub_tracks['t_norm'] = sub_tracks['title'].map(clean_title)
sub_tracks['a_norm'] = sub_tracks['artist'].map(norm_str)
sub_tracks['al_norm'] = sub_tracks['album'].map(norm_str)

# year normalization: take 4-digit if present else last 2-digit -> 19xx/20xx heuristic

def norm_year(y):
    y = norm_str(y)
    if not y:
        return ''
    m = re.search(r"(\d{4})", y)
    if m:
        return m.group(1)
    m = re.search(r"(\d{2})", y)
    if m:
        yy = int(m.group(1))
        # heuristic: 00-25 => 2000s else 1900s
        return str(2000+yy) if yy <= 25 else str(1900+yy)
    return ''

sub_tracks['y_norm'] = sub_tracks['year'].map(norm_year)

# canonical key: title+artist (most reliable); fallback to title+album when artist missing
sub_tracks['key1'] = sub_tracks.apply(lambda r: (r['t_norm'], r['a_norm']) if r['a_norm'] else (r['t_norm'], r['al_norm']), axis=1)

# Aggregate revenue across duplicates by key1
rev_by_id = sales_df.set_index('track_id')['total_revenue_usd'].to_dict()
sub_tracks['rev'] = sub_tracks['track_id'].map(rev_by_id).fillna(0.0)

agg = sub_tracks.groupby('key1', dropna=False).agg(
    total_revenue_usd=('rev','sum'),
    best_track_id=('track_id','first'),
    title=('title', lambda s: s.dropna().iloc[0] if len(s.dropna()) else None),
    artist=('artist', lambda s: s.dropna().iloc[0] if len(s.dropna()) else None),
    album=('album', lambda s: s.dropna().iloc[0] if len(s.dropna()) else None),
).reset_index(drop=True)

agg_sorted = agg.sort_values('total_revenue_usd', ascending=False)

top = agg_sorted.iloc[0].to_dict()
# format revenue to 2 decimals
answer = {
    'title': top.get('title'),
    'artist': top.get('artist'),
    'album': top.get('album'),
    'total_revenue_usd': round(float(top.get('total_revenue_usd',0.0))+1e-9, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_r7xoVgC8FruXLOm3r7Lnvk3M': 'file_storage/call_r7xoVgC8FruXLOm3r7Lnvk3M.json', 'var_call_yiX4IeJSBIRdWmysYdfnPyXL': 'file_storage/call_yiX4IeJSBIRdWmysYdfnPyXL.json'}

exec(code, env_args)
