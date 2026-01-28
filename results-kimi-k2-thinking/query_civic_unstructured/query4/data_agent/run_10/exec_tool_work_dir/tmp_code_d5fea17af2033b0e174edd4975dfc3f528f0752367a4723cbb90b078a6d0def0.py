code = """import json, os, sys

# Check what files are available in /tmp
print("Files in /tmp:", os.listdir('/tmp')[:20])

# Load the data from the actual paths
with open('/tmp/tmp6v8h4l_u.json', 'r') as f:
    funding_data = json.load(f)

with open('/tmp/tmp1i3q6xjc.json', 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Show first civic document snippet
sample_doc = civic_docs[0]
print('Filename:', sample_doc.get('filename'))
text_preview = sample_doc.get('text')[:500]
print('Text preview:', text_preview.replace('\n', ' ')[:200])

# Check for Spring 2022
found_spring = []
for doc in civic_docs:
    if 'Spring 2022' in doc.get('text', '') or '2022-Spring' in doc.get('text', ''):
        found_spring.append(doc.get('filename'))

print('Documents with Spring 2022:', found_spring)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
