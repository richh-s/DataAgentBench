code = """import json

# Load data
civic_docs = json.load(open('/tmp/tmp7q6r1zwh.json'))
funding_data = json.load(open('/tmp/tmptf8vwxq6.json'))

# Count projects starting in Spring 2022 and calculate total funding
spring_2022_projects = ['2022 Morning View Resurfacing & Storm Drain Improvements']
spring_2022_funding = [f for f in funding_data if f['Project_Name'] in spring_2022_projects]

total_funding = sum(int(f['Amount']) for f in spring_2022_funding)
project_count = len(spring_2022_funding)

print('__RESULT__:')
print(json.dumps({
    'project_count': project_count,
    'total_funding': total_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
