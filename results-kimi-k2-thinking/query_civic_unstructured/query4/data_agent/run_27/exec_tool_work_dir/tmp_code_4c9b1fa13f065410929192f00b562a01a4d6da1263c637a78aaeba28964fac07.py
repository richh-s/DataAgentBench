code = """import json
import re

# Load the data - using string key access
mongo_path = globals()['var_functions.query_db:5']
funding_path = globals()['var_functions.query_db:20']

# Load MongoDB documents
if isinstance(mongo_path, str) and mongo_path.endswith('.json'):
    with open(mongo_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = mongo_path

# Load funding records
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_path

print('Loaded %d civic docs and %d funding records' % (len(civic_docs), len(funding_records)))

# Now process the documents to find Spring 2022 projects
spring_2022_projects = []

for doc_idx, doc in enumerate(civic_docs):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for patterns indicating Spring 2022
    if '2022' in text:
        # Search for project patterns in the text
        lines = text.split('\n')
        for line_idx, line in enumerate(lines):
            if '2022' in line and ('spring' in line.lower() or 'Spring' in line):
                # Try to find project names around this line
                start_idx = max(0, line_idx - 5)
                end_idx = min(len(lines), line_idx + 5)
                context = ' '.join(lines[start_idx:end_idx])
                
                spring_2022_projects.append({
                    'doc_idx': doc_idx,
                    'filename': filename,
                    'line_context': context,
                    'spring_line': line
                })

print('Found %d potential Spring 2022 references' % len(spring_2022_projects))

# Show a sample
if spring_2022_projects:
    print('Sample context:', spring_2022_projects[0]['line_context'][:500])

# Load funding data as well
project_names_from_funding = [rec['Project_Name'] for rec in funding_records]
print('Total funding records:', len(project_names_from_funding))
print('Sample project names:', project_names_from_funding[:5])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
