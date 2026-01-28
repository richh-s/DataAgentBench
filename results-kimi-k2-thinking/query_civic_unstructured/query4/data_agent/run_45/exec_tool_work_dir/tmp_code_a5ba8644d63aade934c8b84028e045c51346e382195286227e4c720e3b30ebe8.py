code = """import json

docs = json.load(open('/tmp/tmp_9m9q8o4.json'))
count = 0
for doc in docs:
    txt = doc.get('text','')
    if '2022-Spring' in txt or '2022-March' in txt or '2022-April' in txt or '2022-May' in txt:
        count += 1
        
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
