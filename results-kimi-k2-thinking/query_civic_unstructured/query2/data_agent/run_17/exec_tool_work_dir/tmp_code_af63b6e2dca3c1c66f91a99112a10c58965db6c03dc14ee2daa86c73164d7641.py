code = """import json
import re

# Load the civic documents
civic_docs_file = var_functions.query_db_5
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print('Total civic docs loaded:', len(civic_docs))

park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Check if document mentions park, completed, and 2022
    if re.search('park', text, re.IGNORECASE) and \
       re.search('completed', text, re.IGNORECASE) and \
       re.search('2022', text):
        lines = text.splitlines()
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            # Look for project names (likely contain 'Park' and are capitalized)
            if re.search('park', line_stripped, re.IGNORECASE) and len(line_stripped) > 10:
                # Check following lines for completed and 2022
                snippet = '\n'.join(lines[i:i+10])
                if re.search('completed', snippet, re.IGNORECASE) and re.search('2022', snippet):
                    park_projects_2022.append(line_stripped)

# Remove duplicates
unique_projects = list(dict.fromkeys(park_projects_2022))

print('Found projects:', unique_projects)
print('Total count:', len(unique_projects))

result = {'projects': unique_projects, 'count': len(unique_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
