code = """import json
import os

# Get the file path from the query result
file_path = locals()['var_functions.query_db:2']
print('File path loaded')

# Load civic documents
civic_docs = json.load(open(file_path))
print('Documents loaded:', len(civic_docs))

# Search for Spring 2022 projects
spring_2022_projects = []
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

for doc in civic_docs:
    text = doc.get('text', '')
    has_spring = any(pattern in text for pattern in spring_patterns)
    if has_spring:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'Project' in line:
                upper = sum(1 for c in line if c.isupper())
                if upper > len(line) * 0.2:  # More than 20% uppercase
                    spring_2022_projects.append(line)

# Remove duplicates
unique_projects = list(set(spring_2022_projects))
print('Unique Spring 2022 projects:', len(unique_projects))

# Prepare result
result = {'count': len(unique_projects), 'projects': unique_projects[:50]}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
