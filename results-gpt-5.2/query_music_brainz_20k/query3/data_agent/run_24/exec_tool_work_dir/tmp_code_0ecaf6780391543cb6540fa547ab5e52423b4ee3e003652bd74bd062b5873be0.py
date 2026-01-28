code = """import json, pandas as pd, re

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

sales_tot = pd.DataFrame(load_records(var_call_P498EM6oyimy5fCpsyj3C13z))
tracks = pd.DataFrame(load_records(var_call_Yb0fs3JT16GaQET6FTMBYhWy))

# types
sales_tot['track_id'] = sales_tot['track_id'].astype(int)
sales_tot['total_revenue_usd'] = sales_tot['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# Basic cleaning/normalization for entity resolution
stop_words = set(['the','a','an','and','&','feat','featuring','ft','vs','with'])

def norm_text(x):
    if x is None:
        return ''
    s = str(x).strip().lower()
    if s == 'none' or s == '[unknown]':
        return ''
    s = re.sub(r"\([^)]*\)", " ", s)  # remove parenthetical
    s = re.sub(r"\[[^]]*\]", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    toks = [t for t in s.split() if t not in stop_words]
    return ' '.join(toks)

def norm_year(y):
    if y is None:
        return None
    s = str(y).strip()
    if s.lower() == 'none' or s == '':
        return None
    s = s.replace("'", '')
    m = re.search(r"\d{4}", s)
    if m:
        return int(m.group(0))
    m = re.fullmatch(r"\d{1,2}", s)
    if m:
        yy = int(s)
        # heuristic: treat 00-25 as 2000s else 1900s
        return 2000+yy if yy <= 25 else 1900+yy
    m = re.fullmatch(r"\d{1,3}", s)
    if m:
        return int(s)
    return None

tracks['t_norm'] = tracks['title'].apply(norm_text)
tracks['a_norm'] = tracks['artist'].apply(norm_text)
tracks['al_norm'] = tracks['album'].apply(norm_text)
tracks['y_norm'] = tracks['year'].apply(norm_year)

# Join sales to track metadata
df = sales_tot.merge(tracks[['track_id','title','artist','album','year','t_norm','a_norm','al_norm','y_norm']], on='track_id', how='left')

# Create entity key: title+artist preferred; fallback to title+album; fallback to title only

def make_key(r):
    t = r['t_norm']
    a = r['a_norm']
    al = r['al_norm']
    if t and a:
        return f"TA::{t}::{a}"
    if t and al:
        return f"TL::{t}::{al}"
    return f"T::{t}"

df['entity_key'] = df.apply(make_key, axis=1)

# Aggregate revenue by resolved entity
agg = df.groupby('entity_key', as_index=False)['total_revenue_usd'].sum()
agg = agg.sort_values('total_revenue_usd', ascending=False)

best_key = agg.iloc[0]['entity_key']
best_rev = float(agg.iloc[0]['total_revenue_usd'])

# Pick a representative track record for the best key: highest revenue track_id within that entity
rep = df[df['entity_key']==best_key].sort_values('total_revenue_usd', ascending=False).iloc[0]

answer = {
    'title': None if pd.isna(rep['title']) else str(rep['title']),
    'artist': None if pd.isna(rep['artist']) else str(rep['artist']),
    'album': None if pd.isna(rep['album']) else str(rep['album']),
    'year': None if pd.isna(rep['year']) else str(rep['year']),
    'total_revenue_usd': round(best_rev, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_P498EM6oyimy5fCpsyj3C13z': 'file_storage/call_P498EM6oyimy5fCpsyj3C13z.json', 'var_call_Yb0fs3JT16GaQET6FTMBYhWy': 'file_storage/call_Yb0fs3JT16GaQET6FTMBYhWy.json'}

exec(code, env_args)
