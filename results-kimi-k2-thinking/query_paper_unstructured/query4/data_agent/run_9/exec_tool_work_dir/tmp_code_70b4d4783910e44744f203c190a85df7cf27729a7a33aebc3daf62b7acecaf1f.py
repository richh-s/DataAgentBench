code = """import json

# Read all papers
result_path = var_functions.query_db:30
with open(result_path, 'r') as f:
    papers = json.load(f)

# Filter for 2016 physical activity papers
filtered = []
for p in papers:
    text = p.get('text', '')
    if '2016' in text and 'physical activity' in text.lower():
        filename = p.get('filename', '')
        title = filename.replace('.txt', '') if filename else 'Unknown'
        filtered.append({'title': title, 'filename': filename})

# Output results
result = json.dumps(filtered)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
