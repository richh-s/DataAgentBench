code = """import json, pandas as pd
path = var_call_EoNR6oUkyQFl34st4Q3Au2Xl
with open(path,'r',encoding='utf-8') as f:
    data=json.load(f)
df=pd.DataFrame(data)
df['description']=df['description'].fillna('').astype(str)
df['title']=df['title'].fillna('').astype(str)
df['desc_len']=df['description'].str.len()
top=df.sort_values('desc_len',ascending=False).iloc[0]
res={'title':top['title'],'article_id':top['article_id'],'description_length':int(top['desc_len'])}
print('__RESULT__:')
print(json.dumps(res, ensure_ascii=False))"""

env_args = {'var_call_r6ZP8mAzBJhKdnajDBztSYqD': 'file_storage/call_r6ZP8mAzBJhKdnajDBztSYqD.json', 'var_call_b3Mz7fJdmdQtYYswxNX6newz': {'title': None, 'article_id': None, 'description_length': None}, 'var_call_Km8Ue8EJmnKXrazu09exZcbI': {'count': 0}, 'var_call_EoNR6oUkyQFl34st4Q3Au2Xl': 'file_storage/call_EoNR6oUkyQFl34st4Q3Au2Xl.json', 'var_call_nOgGnB7062CLDQlRAgheHwnP': {'title': None, 'article_id': None, 'description_length': None}}

exec(code, env_args)
