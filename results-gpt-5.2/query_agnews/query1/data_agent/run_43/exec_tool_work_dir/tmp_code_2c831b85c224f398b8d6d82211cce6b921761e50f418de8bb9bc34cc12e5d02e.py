code = """import json, pandas as pd
path = var_call_0HNmqm4wqN6v5lk90DqStdOT
with open(path,'r',encoding='utf-8') as f:
    recs = json.load(f)
df = pd.DataFrame(recs)
df['desc_len'] = df['description'].fillna('').map(len)
# take top 200 by desc length
cand = df.sort_values('desc_len', ascending=False).head(200)
print('__RESULT__:')
print(cand[['article_id','title','desc_len']].to_json(orient='records'))"""

env_args = {'var_call_0HNmqm4wqN6v5lk90DqStdOT': 'file_storage/call_0HNmqm4wqN6v5lk90DqStdOT.json', 'var_call_pexuNncc1BpI9RkDyr1D0D7T': [], 'var_call_8xPFkBCfbaNPlaKXgrOVDk7r': [], 'var_call_03p80bmyGOoafnQu34eShb2x': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}]}

exec(code, env_args)
