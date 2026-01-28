code = """import json

# Check what is actually stored in the variable
citation_key = 'var_functions.query_db:24'
citation_data = locals().get(citation_key, None)

print('Type of stored data:', type(citation_data))
print('Value of stored data:', citation_data[:200] if isinstance(citation_data, str) and len(citation_data) > 200 else citation_data)

result = {
    'type': str(type(citation_data)),
    'is_list': isinstance(citation_data, list),
    'is_string': isinstance(citation_data, str)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': "<class 'str'>", 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'count': 39, 'has_data': True}}

exec(code, env_args)
