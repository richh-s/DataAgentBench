code = """import json
import re
import os

# Check if the result file exists and read it
result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_0.json'
print(f"File exists: {os.path.exists(result_file)}")

with open(result_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")

# Look for text mentioning 2022 in all documents
docs_with_2022 = []
for i, doc in enumerate(civic_docs):
    text = doc.get('text', '')
    if '2022' in text:
        docs_with_2022.append((i, doc))

print(f"Documents containing '2022': {len(docs_with_2022)}")

# Now extract projects from documents with 2022
spring_2022_projects = []

for doc_idx, doc in docs_with_2022:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split into lines and look for project headers
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for project names (typically uppercase or title case)
        if line and len(line) > 5:
            # Check if line looks like a project name
            is_project_name = False
            if line.isupper() and len(line) > 10:
                # Skip common headers
                if not any(skip in line.lower() for skip in ['page', 'agenda item', 'public works', 'commission', 'meeting', 'subject:', 'recommended action:', 'prepared by', 'approved by']):
                    is_project_name = True
            elif line.istitle() and len(line) > 10 and not line.startswith('Page'):
                if not any(skip in line.lower() for skip in ['public works', 'commission', 'meeting', 'agenda']):
                    is_project_name = True
            
            if is_project_name:
                # Check following text for Spring 2022 references
                following = ' '.join(lines[i:i+15])
                spring_indicators = ['Spring 2022', '2022 Spring', '2022-Spring', '2022 Mar', '2022 Apr', '2022 May', '2022-03', '2022-04', '2022-05']
                for indicator in spring_indicators:
                    if indicator in following or indicator.replace(' ', '') in following.replace(' ', ''):
                        spring_2022_projects.append({
                            'name': line,
                            'indicator': indicator,
                            'filename': filename
                        })
                        break

# Remove duplicates
unique_proj_names = []
seen_names = set()
for proj in spring_2022_projects:
    name = proj['name']
    if name not in seen_names:
        seen_names.add(name)
        unique_proj_names.append(name)

print(f"Found {len(spring_2022_projects)} occurrences")
print(f"Unique projects starting in Spring 2022: {len(unique_proj_names)}")
print("Project names:")
for name in unique_proj_names[:20]:  # Show first 20
    print(f"  - {name}")

result = {'count': len(unique_proj_names), 'projects': unique_proj_names}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
