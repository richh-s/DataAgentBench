code = """import json, pandas as pd, re

sales_path = var_call_KBQO1MHzvpMYJW1nLLhrOfNe
tracks_path = var_call_YweGQLUtycnJmCE4Vu0vduqp

with open(sales_path,'r',encoding='utf-8') as f:
    sales = json.load(f)
with open(tracks_path,'r',encoding='utf-8') as f:
    tracks = json.load(f)

dfs = pd.DataFrame(sales)
dft = pd.DataFrame(tracks)

dfs['track_id'] = dfs['track_id'].astype(int)
dfs['total_revenue_usd'] = dfs['total_revenue_usd'].astype(float)
dft['track_id'] = dft['track_id'].astype(int)

def norm(s):
    if s is None:
        return ''
    s = str(s).strip().lower()
    if s == 'none' or s == '[unknown]':
        return ''
    s = re.sub(r"\s+", " ", s)
    return s

def norm_title(t):
    t = norm(t)
    if not t:
        return ''
    # remove leading artist - title patterns
    if ' - ' in t:
        left,right = t.split(' - ',1)
        # if left looks like an artist name (no digits-only, not too short)
        if len(left) > 2 and not re.fullmatch(r"\d+", left):
            t = right
    # remove parenthetical live/remaster info
    t = re.sub(r"\([^)]*\)", "", t)
    t = re.sub(r"\[[^\]]*\]", "", t)
    t = re.sub(r"[^a-z0-9 ]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def norm_year(y):
    y = norm(y)
    if not y:
        return ''
    y = re.sub(r"[^0-9]", "", y)
    if len(y)==4:
        return y
    if len(y)==2:
        # heuristic: 00-25 -> 2000s else 1900s
        yy=int(y)
        return str(2000+yy) if yy<=25 else str(1900+yy)
    return ''

dft['ntitle']=dft['title'].map(norm_title)
dft['nartist']=dft['artist'].map(norm)
dft['nalbum']=dft['album'].map(norm)
dft['nyear']=dft['year'].map(norm_year)

# build entity key; allow missing artist/album/year by using just title+artist if available else title only

def make_key(row):
    t=row['ntitle']
    a=row['nartist']
    al=row['nalbum']
    y=row['nyear']
    if t and a:
        return f"{t}||{a}"
    return t

dft['entity_key']=dft.apply(make_key,axis=1)

# join sales totals to tracks, then aggregate by entity_key
merged = dfs.merge(dft[['track_id','entity_key','title','artist','album','year']], on='track_id', how='left')
merged = merged[merged['entity_key'].notna() & (merged['entity_key']!='')]
entity_rev = merged.groupby('entity_key', as_index=False)['total_revenue_usd'].sum()
entity_rev = entity_rev.sort_values('total_revenue_usd', ascending=False)

top_key = entity_rev.iloc[0]['entity_key']
top_total = float(entity_rev.iloc[0]['total_revenue_usd'])
# pick a representative track row with that key and max individual revenue
cand = merged[merged['entity_key']==top_key].copy()
rep = cand.sort_values('total_revenue_usd', ascending=False).iloc[0]

answer = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'year': rep['year'],
    'total_revenue_usd': round(top_total,2)
}

print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_KBQO1MHzvpMYJW1nLLhrOfNe': 'file_storage/call_KBQO1MHzvpMYJW1nLLhrOfNe.json', 'var_call_YweGQLUtycnJmCE4Vu0vduqp': 'file_storage/call_YweGQLUtycnJmCE4Vu0vduqp.json'}

exec(code, env_args)
