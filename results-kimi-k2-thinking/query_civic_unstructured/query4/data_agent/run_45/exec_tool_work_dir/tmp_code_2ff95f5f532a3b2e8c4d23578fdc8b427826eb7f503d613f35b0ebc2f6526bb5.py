code = """import json
import re

# Load the civic docs data
with open('/tmp/tmp_9m9q8o4.json', 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(civic_docs), 'documents')

# Look at the first document to understand structure
first_doc = civic_docs[0]
print('\nFirst document filename:', first_doc['filename'])
print('\nFirst document sample text (first 500 chars):')
print(first_doc['text'][:500])

# Look for project patterns and dates in all documents
spring_2022_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for Spring 2022 date patterns
    has_spring_2022 = any(pattern in text for pattern in ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05'])
    if has_spring_2022:
        # Try to extract project names - look for lines that look like project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Repair', 'Improvement']):
                # Count uppercase letters - if more than 30% are uppercase, likely a project name
                uppercase_count = sum(1 for c in line if c.isupper())
                total_len = len(line.replace(' ', '').replace('-', '').replace('/', ''))
                if total_len > 0 and uppercase_count / total_len > 0.3:
                    spring_2022_projects.append({
                        'project_name': line,
                        'doc_filename': doc['filename']
                    })

print('\nFound', len(spring_2022_projects), 'potential Spring 2022 projects')
for proj in spring_2022_projects[:15]:
    print('  -', proj['project_name'][:80], '(from', proj['doc_filename'], ')')

__RESULT__:
print('__RESULT__:')
import json as js
result = {
    'count': len(spring_2022_projects),
    'projects': spring_2022_projects[:20]
}
print(js.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
