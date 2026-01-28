code = """import json, pandas as pd
path = var_call_0HNmqm4wqN6v5lk90DqStdOT
with open(path,'r',encoding='utf-8') as f:
    recs = json.load(f)
df = pd.DataFrame(recs)
# infer sports by keywords in title/description
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
kw = r"\b(nfl|nba|mlb|nhl|soccer|football|baseball|basketball|hockey|tennis|golf|olympic|olympics|world cup|cup|championship|playoff|coach|quarterback|touchdown|home run|fifa|uefa|premier league|la liga|serie a|bundesliga|cricket|rugby|nascar|formula 1|f1|grand slam|pga|mls)\b"
mask = text.str.contains(kw, regex=True)
df_s = df[mask].copy()
df_s['desc_len'] = df_s['description'].fillna('').map(len)
row = df_s.sort_values(['desc_len','article_id'], ascending=[False, True]).head(1)
ans = row[['title','article_id','desc_len']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_0HNmqm4wqN6v5lk90DqStdOT': 'file_storage/call_0HNmqm4wqN6v5lk90DqStdOT.json'}

exec(code, env_args)
