code = """import json
import re
import os

# Load the MongoDB results
result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_0.json'
with open(result_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Total civic documents: {len(civic_docs)}")

# Look for documents from 2022 (based on filename or content)
documents_2022 = []
for doc in civic_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if '2022' in filename or '2022' in text:
        documents_2022.append(doc)

print(f"Documents with 2022 references: {len(documents_2022)}")

# Extract projects with Spring 2022 start dates
spring_2022_projects = set()

for doc in documents_2022:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for project headers (uppercase lines that aren't page numbers or generic headers)
        if line.isupper() and len(line) > 15 and not line.startswith('PAGE'):
            # Skip non-project headers
            skip_terms = ['AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:', 'PREPARED BY', 'APPROVED BY', 'DATE PREPARED', 'DISCUSSION:']
            if not any(term in line for term in skip_terms):
                # Look ahead for date information
                look_ahead = '\n'.join(lines[i:i+20])
                # Check for Spring 2022 indicators
                if re.search(r'Advertise.*Spring[^\n]{0,50}2022', look_ahead, re.IGNORECASE) or \
                   re.search(r'Begin[^\n]{0,50}Spring[^\n]{0,50}2022', look_ahead, re.IGNORECASE) or \
                   re.search(r'Start[^\n]{0,50}Spring[^\n]{0,50}2022', look_ahead, re.IGNORECASE) or \
                   re.search(r'2022[^\n]{0,50}Spring', look_ahead, re.IGNORECASE) or \
                   re.search(r'2022[-\s](?:03|04|05|Mar|Apr|May)', look_ahead, re.IGNORECASE):
                    spring_2022_projects.add(line)

print(f"Spring 2022 projects: {len(spring_2022_projects)}")
print("Projects:")
for proj in sorted(spring_2022_projects)[:20]:
    print(f"  - {proj}")

result = {'count': len(spring_2022_projects), 'projects': list(spring_2022_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
