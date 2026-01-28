code = """import json

# Load data
civic_docs = json.load(open(var_functions.query_db:60))
funding = json.load(open(var_functions.query_db:48))

# Look for park projects completed in 2022
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Park' in text:
        lines = text.split('\n')
        for line in lines:
            if 'completed' in line.lower() and '2022' in line and 'Park' in line:
                projects.append(line.strip())

print('Found lines:', projects[:5] if projects else 'None')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
