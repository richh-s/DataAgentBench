code = """import json, pandas as pd
cpath = var_call_0Mro7YzlxkD4BgEGQLoRp8hz
with open(cpath,'r',encoding='utf-8') as f:
    cit = json.load(f)
df = pd.DataFrame(cit)
print('__RESULT__:')
print(json.dumps({'columns': df.columns.tolist(), 'head': df.head(3).to_dict(orient='records')}))"""

env_args = {'var_call_0Mro7YzlxkD4BgEGQLoRp8hz': 'file_storage/call_0Mro7YzlxkD4BgEGQLoRp8hz.json', 'var_call_UeanCZ2Ph1Wzzih08kqWsV9x': 'file_storage/call_UeanCZ2Ph1Wzzih08kqWsV9x.json', 'var_call_p026YWcQVP4MkLj8ClpLArW2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
