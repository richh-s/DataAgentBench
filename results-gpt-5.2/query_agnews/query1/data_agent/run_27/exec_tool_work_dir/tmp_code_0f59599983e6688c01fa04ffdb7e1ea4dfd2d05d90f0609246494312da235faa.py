code = """import json, pandas as pd
path = var_call_r6ZP8mAzBJhKdnajDBztSYqD
with open(path,'r',encoding='utf-8') as f:
    data=json.load(f)
df=pd.DataFrame(data)
df['description']=df.get('description', pd.Series(dtype=str)).fillna('').astype(str)
df['title']=df.get('title', pd.Series(dtype=str)).fillna('').astype(str)
text=(df['title']+' '+df['description']).str.lower()
sports_kw = r"\b(olympic|olympics|nba|nfl|mlb|nhl|soccer|football|baseball|basketball|hockey|tennis|golf|judo|swimming|track|marathon|cycling|race|racing|grand slam|open|tournament|championship|cup|quarterfinal|semifinal|final|coach|player|team|match|stadium|medal)\b"
is_sports=text.str.contains(sports_kw, regex=True)
sdf=df[is_sports].copy()
if sdf.empty:
    res={'title': None, 'article_id': None, 'description_length': None}
else:
    sdf['desc_len']=sdf['description'].str.len()
    top=sdf.sort_values('desc_len',ascending=False).iloc[0]
    res={'title':str(top['title']), 'article_id':str(top['article_id']), 'description_length':int(top['desc_len'])}
print('__RESULT__:')
print(json.dumps(res, ensure_ascii=False))"""

env_args = {'var_call_r6ZP8mAzBJhKdnajDBztSYqD': 'file_storage/call_r6ZP8mAzBJhKdnajDBztSYqD.json', 'var_call_b3Mz7fJdmdQtYYswxNX6newz': {'title': None, 'article_id': None, 'description_length': None}, 'var_call_Km8Ue8EJmnKXrazu09exZcbI': {'count': 0}, 'var_call_EoNR6oUkyQFl34st4Q3Au2Xl': 'file_storage/call_EoNR6oUkyQFl34st4Q3Au2Xl.json'}

exec(code, env_args)
