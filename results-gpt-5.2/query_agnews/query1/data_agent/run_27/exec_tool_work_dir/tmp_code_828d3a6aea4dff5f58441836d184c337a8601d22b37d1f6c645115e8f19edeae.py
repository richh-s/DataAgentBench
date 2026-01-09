code = """import json, pandas as pd
path = var_call_r6ZP8mAzBJhKdnajDBztSYqD
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['description'] = df.get('description', pd.Series(dtype=str)).fillna('').astype(str)
df['title'] = df.get('title', pd.Series(dtype=str)).fillna('').astype(str)
df['desc_len'] = df['description'].str.len()
text = (df['title'] + ' ' + df['description']).str.lower()
# broaden keywords
kw = r"\b(game|games|match|season|league|team|teams|player|players|win|won|loss|coach|tournament|championship|cup|final|semifinal|quarterfinal|score|scored|goal|goals|points|draft|injury|fans|stadium|athlete|athletes|medal|race|races|grand slam|open|series)\b"
is_sports = text.str.contains(kw, regex=True)
sports_df = df[is_sports].copy()
mx = sports_df['desc_len'].max() if not sports_df.empty else None
# provide top 5 titles for inspection
if sports_df.empty:
    out = {"count":0}
else:
    tops = sports_df.sort_values('desc_len', ascending=False).head(5)[['article_id','title','desc_len']].to_dict('records')
    out = {"count": int(len(sports_df)), "top5": tops}
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_r6ZP8mAzBJhKdnajDBztSYqD': 'file_storage/call_r6ZP8mAzBJhKdnajDBztSYqD.json', 'var_call_b3Mz7fJdmdQtYYswxNX6newz': {'title': None, 'article_id': None, 'description_length': None}}

exec(code, env_args)
