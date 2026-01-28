code = """import json
import os

# Get the file path from the stored result
citation_key = 'var_functions.query_db:24'
file_path = locals().get(citation_key, '')

print('File path extracted:', file_path)
print('File path type:', type(file_path))

# List files in /tmp to see what's available
print('Files in /tmp:')
for f in os.listdir('/tmp'):
    if f.startswith('tmp'):
        print(f)

result = {
    'file_path': file_path,
    'path_exists': os.path.exists(file_path) if file_path else False
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': "<class 'str'>", 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'count': 39, 'has_data': True}, 'var_functions.execute_python:28': {'type': "<class 'str'>", 'is_list': False, 'is_string': True}, 'var_functions.execute_python:30': {'source': 'file_path_or_other', 'data_type': "<class 'str'>", 'count': 0}}

exec(code, env_args)
