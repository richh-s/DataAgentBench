code = """import json, re, pandas as pd
path_docs = var_call_bcXU1gAR7JWAJROBDk0vKr2G
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

rows=[]
for d in docs[:200]:
    title = d.get('filename','').rsplit('.txt',1)[0]
    rows.append({'title': title})

df = pd.DataFrame(rows)
info = {'columns': list(df.columns), 'head': df.head(3).to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(info))"""

env_args = {'var_call_TfX9M9enUCk4BvRhLnewUTBq': 'file_storage/call_TfX9M9enUCk4BvRhLnewUTBq.json', 'var_call_lQPvr4jLWcuGx4GMacVkBaZm': 'file_storage/call_lQPvr4jLWcuGx4GMacVkBaZm.json', 'var_call_bcXU1gAR7JWAJROBDk0vKr2G': 'file_storage/call_bcXU1gAR7JWAJROBDk0vKr2G.json', 'var_call_scRgKCZJVRGv0wCiP5y7Zsiq': {'columns': ['title', 'citation_count', 'citation_year'], 'head': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}]}}

exec(code, env_args)
