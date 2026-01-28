code = """import json, re

# Get the file path for civic documents
civic_file = var_functions.query_db:60

# Load just the first file to see structure
with open(civic_file) as f:
    civic_docs = json.load(f)

# Check if we can find park projects
print('Total civic documents:', len(civic_docs))

# Look for park-related content in a sample
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Park' in text:
        lines = text.split('\n')
        for line in lines:
            if 'Park' in line and 'completed' in line.lower() and '2022' in line:
                print('Found:', line.strip())
                break"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
