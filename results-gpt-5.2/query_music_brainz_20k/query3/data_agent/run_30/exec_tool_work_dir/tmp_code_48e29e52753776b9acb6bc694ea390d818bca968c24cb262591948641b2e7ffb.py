code = """import json, pandas as pd, re
sales_path = var_call_KBQO1MHzvpMYJW1nLLhrOfNe
tracks_path = var_call_YweGQLUtycnJmCE4Vu0vduqp
with open(sales_path,'r',encoding='utf-8') as f: sales=json.load(f)
with open(tracks_path,'r',encoding='utf-8') as f: tracks=json.load(f)
dfs=pd.DataFrame(sales)
dft=pd.DataFrame(tracks)
dfs['track_id']=dfs['track_id'].astype(int)
dfs['total_revenue_usd']=dfs['total_revenue_usd'].astype(float)
dft['track_id']=dft['track_id'].astype(int)

def norm(s):
    if s is None: return ''
    s=str(s).strip().lower()
    if s in ('none','[unknown]'): return ''
    s=re.sub(r"\s+"," ",s)
    return s

def norm_title(t):
    t=norm(t)
    if not t: return ''
    if ' - ' in t:
        left,right=t.split(' - ',1)
        if len(left)>2 and not re.fullmatch(r"\d+",left):
            t=right
    t=re.sub(r"\([^)]*\)","",t)
    t=re.sub(r"\[[^\]]*\]","",t)
    t=re.sub(r"[^a-z0-9 ]","",t)
    t=re.sub(r"\s+"," ",t).strip()
    return t

def title_ok(nt):
    if not nt or len(nt)<3: return False
    # reject mostly digits or too few letters
    letters=sum(c.isalpha() for c in nt)
    digits=sum(c.isdigit() for c in nt)
    if letters==0: return False
    if digits>0 and letters/(letters+digits) < 0.4: return False
    return True

dft['ntitle']=dft['title'].map(norm_title)
dft['nartist']=dft['artist'].map(norm)
dft['entity_key']=dft.apply(lambda r: f"{r['ntitle']}||{r['nartist']}" if title_ok(r['ntitle']) and r['nartist'] else (r['ntitle'] if title_ok(r['ntitle']) else ''), axis=1)

merged=dfs.merge(dft[['track_id','entity_key','title','artist','album','year']], on='track_id', how='left')
merged=merged[merged['entity_key']!='']
entity_rev=merged.groupby('entity_key',as_index=False)['total_revenue_usd'].sum().sort_values('total_revenue_usd',ascending=False)

top=entity_rev.iloc[0]
key=top['entity_key']; total=float(top['total_revenue_usd'])
rep=merged[merged['entity_key']==key].sort_values('total_revenue_usd',ascending=False).iloc[0]
ans={'title':rep['title'],'artist':rep['artist'],'album':rep['album'],'year':rep['year'],'total_revenue_usd':round(total,2)}
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_KBQO1MHzvpMYJW1nLLhrOfNe': 'file_storage/call_KBQO1MHzvpMYJW1nLLhrOfNe.json', 'var_call_YweGQLUtycnJmCE4Vu0vduqp': 'file_storage/call_YweGQLUtycnJmCE4Vu0vduqp.json', 'var_call_D7OIiQtYuDcxXDja4iob6Q9h': {'title': '003-', 'artist': ' ', 'album': ' (2003)', 'year': 'None', 'total_revenue_usd': 8582.15}}

exec(code, env_args)
