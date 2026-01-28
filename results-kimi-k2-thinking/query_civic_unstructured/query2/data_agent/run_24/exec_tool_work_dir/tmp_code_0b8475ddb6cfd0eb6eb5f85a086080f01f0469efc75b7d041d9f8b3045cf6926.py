code = """import json
import re

# Load data from files
civic_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
funding_records = json.load(open('/tmp/tmptjtu3_1d.json'))

print('Loaded data successfully')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Look for completed park projects in 2022
found_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Check if this document mentions park projects completed in 2022
    if 'completed' in text and '2022' in text and 'park' in text:
        # Extract relevant lines
        lines = doc.get('text', '').split('\n')
        for line in lines:
            line_lower = line.lower()
            if 'completed' in line_lower and '2022' in line_lower and 'park' in line_lower:
                found_projects.append(line.strip())

print('Found projects:', len(found_projects))

# Show first few
for i, proj in enumerate(found_projects[:3]):
    print(i, proj[:100])

__RESULT__:
result = {'found': len(found_projects)}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
