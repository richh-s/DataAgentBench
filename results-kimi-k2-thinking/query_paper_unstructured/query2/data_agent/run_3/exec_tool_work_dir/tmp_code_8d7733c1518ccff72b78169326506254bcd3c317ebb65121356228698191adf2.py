code = """import json
import os

# Let's try to access the stored results using the storage key
citation_key = 'var_functions.query_db:24'
result_path = '/tmp/tmph0y1j0i5.json'

# Try to access the file directly
if os.path.exists(result_path):
    with open(result_path, 'r') as f:
        citations_data = json.load(f)
    print('Loaded from file path directly')
else:
    # Try to access via storage
    citations_data = locals().get(citation_key, [])
    if not citations_data:
        citations_data = []
    print('Loaded from storage variable')

print('Number of citation records:', len(citations_data))
if citations_data:
    print('First record:', citations_data[0])
    print('Sample records:', citations_data[:3])

result = {'count': len(citations_data), 'has_data': len(citations_data) > 0}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': "<class 'str'>", 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
