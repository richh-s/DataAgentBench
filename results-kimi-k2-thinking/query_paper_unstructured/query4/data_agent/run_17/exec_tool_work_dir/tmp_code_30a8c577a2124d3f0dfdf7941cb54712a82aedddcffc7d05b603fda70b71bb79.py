code = """import json

# The result from query_db is stored in var_functions.query_db:14
# Let's load it
papers_data = locals()['var_functions.query_db:14']

# If it's a string (file path), read the file
if isinstance(papers_data, str):
    with open(papers_data, 'r') as f:
        papers_data = json.load(f)

print('Total papers found: ' + str(len(papers_data)))

# Find papers from 2016 that mention physical activity
papers_2016 = []
for paper in papers_data:
    text = paper['text']
    if '2016' in text and 'physical activity' in text.lower():
        filename = paper['filename']
        title = filename.replace('.txt', '')
        papers_2016.append(title)

print('Papers from 2016: ' + str(len(papers_2016)))
for title in papers_2016:
    print('  - ' + title)

# Return the titles
result = {'titles': papers_2016, 'count': len(papers_2016)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'status': 'debugging'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
