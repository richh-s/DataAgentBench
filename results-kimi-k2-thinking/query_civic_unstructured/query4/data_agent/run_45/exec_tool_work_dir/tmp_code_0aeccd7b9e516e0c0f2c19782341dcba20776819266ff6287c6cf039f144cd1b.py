code = """import json
import re

# Load the civic docs data
with open('/tmp/tmp_9m9q8o4.json', 'r') as f:
    civic_docs = json.load(f)

print(f'Loaded {len(civic_docs)} documents')

# Look at the first document to understand structure
first_doc = civic_docs[0]
print('\nFirst document keys:', first_doc.keys())
print('\nFirst document filename:', first_doc['filename'])
print('\nFirst document sample text (first 500 chars):')
print(first_doc['text'][:500])

# Look for project patterns in the text
text = first_doc['text']
print('\n--- Looking for date patterns (2022-Spring variants) ---')
date_patterns = [r'2022-Spring', r'2022-March', r'2022-April', r'2022-May', r'2022-03', r'2022-04', r'2022-05']
for pattern in date_patterns:
    matches = re.finditer(pattern, text)
    for match in matches:
        start = max(0, match.start() - 100)
        end = min(len(text), match.end() + 100)
        context = text[start:end].replace('\n', ' ')
        print(f'Found {pattern}: ...{context}...')

# Also look for project names near date patterns
print('\n--- Looking for project name patterns ---')
# Common patterns: CAPITALIZED names, ending with "Project"
project_patterns = [r'\b[A-Z][A-Z\s]+Project\b', r'\b[A-Z][A-Z\s]+Improvements\b', r'\b[A-Z][A-Z\s]+Repair\b']
for pattern in project_patterns:
    matches = re.finditer(pattern, text)
    for match in matches:
        proj_name = match.group()
        print(f'Found project: {proj_name}')

# Check all documents for Spring 2022 mentions
print('\n--- Checking all docs for Spring 2022 references ---')
spring_2022_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for Spring 2022 date patterns
    has_spring_2022 = any(pattern in text for pattern in ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05'])
    if has_spring_2022:
        # Try to extract project names from this document
        # Simple heuristic: look for CAPITALIZED words ending with Project/Improvements/Repairs
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if any(line.endswith(suffix) for suffix in ['Project', 'Improvements', 'Repairs', 'Repair', 'Improvement']):
                if line.isupper() or (len(line) > 10 and sum(1 for c in line if c.isupper()) > len(line) * 0.3):
                    spring_2022_projects.append({
                        'project_name': line,
                        'doc_filename': doc['filename'],
                        'status': 'unknown',
                        'type': 'unknown',
                        'st': '2022-Spring'
                    })

print(f'Found {len(spring_2022_projects)} potential Spring 2022 projects')
for proj in spring_2022_projects[:10]:
    print(f"  - {proj['project_name']} (from {proj['doc_filename']})")

# Store the extracted projects for next steps
__RESULT__:
print('__RESULT__:')
import json as js
print(js.dumps(spring_2022_projects))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
