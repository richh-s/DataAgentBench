code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:19']
with open(funding_path) as f:
    funding_data = json.load(f)

# Find projects with 2022 in the name that might be Spring 2022
projects_2022 = []
for item in funding_data:
    project_name = item['Project_Name']
    if '2022' in project_name:
        amount = int(item['Total_Amount'])
        projects_2022.append({
            'name': project_name,
            'funding': amount
        })

result = {
    'count': len(projects_2022),
    'total_funding': sum(p['funding'] for p in projects_2022),
    'projects': projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}], 'var_functions.query_db:48': [{'project_count': '1', 'total_funding': '38000'}], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json'}

exec(code, env_args)
