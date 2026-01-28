code = """import json
import os

# Load the civic documents
file_path = locals()['var_functions.query_db:2']
civic_docs = json.load(open(file_path))
print('Loaded documents:', len(civic_docs))

# Find Spring 2022 projects
projects = []
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

for doc in civic_docs:
    text = doc.get('text', '')
    if any(p in text for p in spring_patterns):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'Project' in line:
                upper = sum(1 for c in line if c.isupper())
                if upper > 3:
                    projects.append(line)

# Deduplicate and limit
unique_projects = list(set(projects))[:100]
print('Found projects:', len(unique_projects))

result = {'spring_2022_count': len(unique_projects), 'projects': unique_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
