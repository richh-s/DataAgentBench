code = """import json

# Load data
civic_docs = json.load(open('/tmp/tmp7q6r1zwh.json', 'r'))
funding_data = json.load(open('/tmp/tmptf8vwxq6.json', 'r'))

# Find projects with 2022 Morning View in their name
project_name = '2022 Morning View Resurfacing & Storm Drain Improvements'
found_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'Morning View' in text:
        found_projects.append(project_name)
        break

# Get funding for this project
project_funding = [f for f in funding_data if f['Project_Name'] == project_name]
total_funding = sum(int(f['Amount']) for f in project_funding)

result = {
    'project_count': len(found_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
