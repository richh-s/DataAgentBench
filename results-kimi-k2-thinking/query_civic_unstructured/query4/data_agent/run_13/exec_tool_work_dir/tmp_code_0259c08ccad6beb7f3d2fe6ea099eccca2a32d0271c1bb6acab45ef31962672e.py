code = """import json
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding = json.load(f)

spring_count = 0
for doc in civic_docs:
    text = doc['text']
    if 'Spring 2022' in text or '2022-Spring' in text:
        spring_count += 1

funding_sum = 0
for fund in funding:
    if '2022' in fund['Project_Name']:
        funding_sum += int(fund['Amount'])

result = {'spring_2022_projects': spring_count, 'total_funding': funding_sum}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}}

exec(code, env_args)
