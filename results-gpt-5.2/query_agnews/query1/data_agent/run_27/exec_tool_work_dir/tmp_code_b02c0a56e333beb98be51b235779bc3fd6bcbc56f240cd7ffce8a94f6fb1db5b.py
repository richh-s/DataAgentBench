code = """import json, pandas as pd
path = var_call_r6ZP8mAzBJhKdnajDBztSYqD
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# normalize types
for col in ['title','description']:
    if col not in df.columns:
        df[col] = None

df['description'] = df['description'].fillna('')
df['title'] = df['title'].fillna('')
df['desc_len'] = df['description'].astype(str).str.len()
# sports heuristic keywords
text = (df['title'].astype(str) + ' ' + df['description'].astype(str)).str.lower()
kw = r"\b(nba|nfl|mlb|nhl|soccer|football|baseball|basketball|hockey|tennis|golf|olympic|olympics|cricket|rugby|fifa|uefa|premier league|world cup|super bowl|touchdown|home run|playoffs|tournament|coach|quarterback|goalkeeper|striker|pitcher|stanley cup)\b"
is_sports = text.str.contains(kw, regex=True)
# also include common team/city patterns could be huge; keep simple
sports_df = df[is_sports].copy()
if sports_df.empty:
    res = {"title": None, "article_id": None, "description_length": None}
else:
    mx = sports_df['desc_len'].max()
    top = sports_df[sports_df['desc_len'] == mx].iloc[0]
    res = {"title": str(top['title']), "article_id": str(top.get('article_id')) if 'article_id' in top else None, "description_length": int(top['desc_len'])}

print('__RESULT__:')
print(json.dumps(res, ensure_ascii=False))"""

env_args = {'var_call_r6ZP8mAzBJhKdnajDBztSYqD': 'file_storage/call_r6ZP8mAzBJhKdnajDBztSYqD.json'}

exec(code, env_args)
