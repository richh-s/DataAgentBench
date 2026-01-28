code = """import json
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding = json.load(f)

spring_projects = []
for doc in civic_docs:
    text = doc['text'].lower()
    if 'spring 2022' in text or '2022-spring' in text:
        spring_projects.append(doc)

spring_count = len(spring_projects)
total_funding = 0
funding_matches = 0

for fund in funding:
    fund_name = fund['Project_Name'].lower()
    for doc in spring_projects:
        doc_text = doc['text'].lower()
        if 'project' in fund_name and (fund_name in doc_text or any(word in fund_name for word in doc_text.split()[:5])):
            total_funding += int(fund['Amount'])
            funding_matches += 1
            break

result = {'spring_2022_projects': spring_count, 'funding_matches': funding_matches, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}}

exec(code, env_args)
