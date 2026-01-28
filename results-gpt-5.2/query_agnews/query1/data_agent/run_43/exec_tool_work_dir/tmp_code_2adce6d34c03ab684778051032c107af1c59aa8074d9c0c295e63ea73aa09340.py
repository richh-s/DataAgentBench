code = """import json, pandas as pd
path = var_call_0HNmqm4wqN6v5lk90DqStdOT
with open(path,'r',encoding='utf-8') as f:
    recs = json.load(f)
df = pd.DataFrame(recs)
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
kw = r"\b(sport|sports|game|games|match|tournament|league|season|player|team|teams|coach|win|wins|won|loss|lost|score|scored|goal|goals|final|defeat|beat|beats|victory|basketball|football|baseball|soccer|hockey|tennis|golf|olymp|nfl|nba|mlb|nhl|fifa|uefa|premier|cup|champion)\b"
mask = text.str.contains(kw, regex=True)
df_s = df[mask].copy()
df_s['desc_len'] = df_s['description'].fillna('').map(len)
row = df_s.sort_values(['desc_len','article_id'], ascending=[False, True]).head(1)
ans = row[['title','article_id','desc_len']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_0HNmqm4wqN6v5lk90DqStdOT': 'file_storage/call_0HNmqm4wqN6v5lk90DqStdOT.json', 'var_call_pexuNncc1BpI9RkDyr1D0D7T': []}

exec(code, env_args)
