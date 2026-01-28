code = """import json

# Load data
funding = json.load(open(locals()['var_functions.query_db:2']))
civic_docs = json.load(open(locals()['var_functions.query_db:5']))

# Find capital design projects from civic documents
projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Extract the design section between headers
    start = text.find('Capital Improvement Projects (Design)')
    if start > -1:
        # Find end of section
        remaining = text[start:]
        end = remaining.find('\n\nCapital Improvement Projects (Construction)')
        if end > -1:
            section = remaining[:end]
            lines = section.split('\n')
            for line in lines:
                clean = line.strip()
                if clean and len(clean) > 8 and 'Project' in clean:
                    if 'fema' not in clean.lower():
                        projects.add(clean)

# Count funded projects
funded = 0
for record in funding:
    if int(record['Amount']) > 50000:
        name = record['Project_Name']
        # Match without suffix
        base = name.split('(')[0].strip()
        if base in projects:
            funded += 1

result = {'count': funded}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
