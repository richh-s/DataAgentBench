code = """import json, pandas as pd
path = var_call_r6ZP8mAzBJhKdnajDBztSYqD
with open(path,'r',encoding='utf-8') as f:
    data=json.load(f)
df=pd.DataFrame(data)
df['description']=df['description'].fillna('').astype(str)
df['title']=df['title'].fillna('').astype(str)
text=(df['title']+' '+df['description']).str.lower()
# sports keyword list expanded
sports_kw = r"\b(olympic|olympics|nba|nfl|mlb|nhl|soccer|football|baseball|basketball|hockey|tennis|golf|judo|swimming|track|marathon|cycling|race|racing|grand slam|open|tournament|championship|cup|quarterfinal|semifinal|final|coach|player|team|match|stadium|medal)\b"
is_sports=text.str.contains(sports_kw, regex=True)
sdf=df[is_sports].copy()
sdf['desc_len']=sdf['description'].str.len()
mx=sdf['desc_len'].max()
top=sdf.sort_values('desc_len',ascending=False).head(1).iloc[0]
res={'title':top['title'],'article_id':top['article_id'],'description_length':int(top['desc_len'])}
print('__RESULT__:')
print(json.dumps(res, ensure_ascii=False))"""

env_args = {'var_call_r6ZP8mAzBJhKdnajDBztSYqD': 'file_storage/call_r6ZP8mAzBJhKdnajDBztSYqD.json', 'var_call_b3Mz7fJdmdQtYYswxNX6newz': {'title': None, 'article_id': None, 'description_length': None}, 'var_call_Km8Ue8EJmnKXrazu09exZcbI': {'count': 0}, 'var_call_EoNR6oUkyQFl34st4Q3Au2Xl': 'file_storage/call_EoNR6oUkyQFl34st4Q3Au2Xl.json'}

exec(code, env_args)
