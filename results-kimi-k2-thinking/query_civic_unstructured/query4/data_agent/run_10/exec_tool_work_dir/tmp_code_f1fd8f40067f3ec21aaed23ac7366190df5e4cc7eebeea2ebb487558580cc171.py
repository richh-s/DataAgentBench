code = """import json

funding_file = locals()['var_functions.query_db:96']
civic_file = locals()['var_functions.query_db:90']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Total_Amount'])

spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text:
        spring_projects.append(text)

matched = 0
for proj_text in spring_projects:
    for proj_name in funding_lookup:
        if proj_name in proj_text:
            matched += funding_lookup[proj_name]

result = {'found_spring': len(spring_projects) > 0, 'matched_funding': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json'}

exec(code, env_args)
