code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

sales_tot = pd.DataFrame(load_records(var_call_6RvfJj1srvGfhdRPe0wX9MI2))
tracks = pd.DataFrame(load_records(var_call_O0MC6gQl3Ik55FY6KnPLLFU6))

# types
sales_tot['track_id'] = sales_tot['track_id'].astype(int)
sales_tot['total_revenue_usd'] = sales_tot['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# join track attributes to each track_id revenue
df = sales_tot.merge(tracks, on='track_id', how='left')

def norm_title(t):
    if t is None:
        return ''
    t = str(t).lower().strip()
    if t == 'none':
        t = ''
    # remove bracketed/parenthetical content often containing live/remaster info
    t = re.sub(r"\([^)]*\)", " ", t)
    t = re.sub(r"\[[^]]*\]", " ", t)
    # keep part after ' - '? actually titles sometimes include 'artist - title'
    # If pattern 'artist - title' and artist column is null, keep right side
    t = re.sub(r"\s+-\s+", " - ", t)
    # collapse whitespace and strip punctuation edges
    t = re.sub(r"[^a-z0-9\s\-']+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def norm_artist(a, title):
    if a is None:
        a = ''
    a = str(a).strip()
    if a.lower() in ['none','[unknown]','unknown','']:
        a = ''
    # if artist missing but title begins with 'X - Y'
    if not a:
        m = re.match(r"^\s*([^\-]{2,})\s-\s(.+)$", str(title))
        if m:
            a = m.group(1).strip()
    a = a.lower()
    a = re.sub(r"[^a-z0-9\s']+", " ", a)
    a = re.sub(r"\s+", " ", a).strip()
    return a

def title_from_title_field(title, artist_norm):
    t = '' if title is None else str(title)
    m = re.match(r"^\s*([^\-]{2,})\s-\s(.+)$", t)
    if m and (not artist_norm or artist_norm == re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s']+"," ", m.group(1).lower())).strip()):
        t2 = m.group(2)
    else:
        t2 = t
    return norm_title(t2)

# normalized entity key: artist + title
artist_norm = []
title_norm = []
for a,t in zip(df['artist'].tolist(), df['title'].tolist()):
    an = norm_artist(a,t)
    artist_norm.append(an)
    title_norm.append(title_from_title_field(t, an))

df['artist_norm'] = artist_norm
df['title_norm'] = title_norm

# if still missing artist_norm, use album? but keep as unknown bucket
# group
entity = df.groupby(['artist_norm','title_norm'], dropna=False, as_index=False)['total_revenue_usd'].sum()
entity = entity.sort_values('total_revenue_usd', ascending=False)

top = entity.iloc[0].to_dict()

# choose a representative display title/artist from original df among matching group
cand = df[(df['artist_norm']==top['artist_norm']) & (df['title_norm']==top['title_norm'])].copy()
# heuristic: prefer non-empty artist and title without embedded artist prefix
cand['artist_display'] = cand['artist'].replace('None', pd.NA)
cand['title_display'] = cand['title'].replace('None', pd.NA)
# pick first with artist not null and title not null
cand2 = cand.dropna(subset=['title_display'])
if len(cand2)==0:
    rep = cand.iloc[0]
else:
    rep = cand2.iloc[0]

artist_out = rep.get('artist')
title_out = rep.get('title')
# if artist_out missing and title has ' - '
if artist_out in [None,'None','[unknown]','unknown','']:
    m = re.match(r"^\s*([^\-]{2,})\s-\s(.+)$", str(title_out))
    if m:
        artist_out = m.group(1).strip()
        title_out = m.group(2).strip()

res = {
    'title': None if title_out in [None,'None'] else str(title_out),
    'artist': None if artist_out in [None,'None'] else str(artist_out),
    'total_revenue_usd': round(float(top['total_revenue_usd']), 2)
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_6RvfJj1srvGfhdRPe0wX9MI2': 'file_storage/call_6RvfJj1srvGfhdRPe0wX9MI2.json', 'var_call_O0MC6gQl3Ik55FY6KnPLLFU6': 'file_storage/call_O0MC6gQl3Ik55FY6KnPLLFU6.json'}

exec(code, env_args)
