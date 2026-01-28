code = """import json
import os

# Access the result from previous query
result_key = 'var_functions.query_db:2'
file_path = globals().get(result_key)
if not file_path:
    file_path = locals().get(result_key)

print('File path accessed')

# Read the JSON file
civic_docs = None
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Docs loaded count:', len(civic_docs))

# Find projects with Spring 2022 start dates
spring_projs = []
patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

for doc in civic_docs:
    txt = doc.get('text', '')
    has_spring = False
    for pat in patterns:
        if pat in txt:
            has_spring = True
            break
    
    if has_spring:
        lines = txt.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'Project' in line:
                uppers = sum(1 for c in line if c.isupper())
                if uppers > 3:
                    spring_projs.append(line)

# Remove duplicates
unique_projs = list(set(spring_projs))
print('Spring 2022 projects found:', len(unique_projs))

# Output result
output = {'count': len(unique_projs), 'projects': unique_projs[:50]}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
