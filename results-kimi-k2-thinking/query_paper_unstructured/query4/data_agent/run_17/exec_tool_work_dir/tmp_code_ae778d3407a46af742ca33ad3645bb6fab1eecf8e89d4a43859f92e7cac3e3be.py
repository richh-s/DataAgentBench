code = """import json
import os

# Find and open the MongoDB result file
files = os.listdir('/tmp')
for filename in files:
    if filename.endswith('.json'):
        filepath = os.path.join('/tmp', filename)
        with open(filepath, 'r') as f:
            papers_data = json.load(f)
        break

# Count papers with 2016 and physical activity
papers_2016 = []
for paper in papers_data:
    text = paper['text']
    if '2016' in text and 'physical activity' in text.lower():
        papers_2016.append(paper)

# Prepare result
result = []
for paper in papers_2016:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    result.append({'title': title})

# Output
output = {'papers_2016': result, 'count': len(result)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'status': 'debugging'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
