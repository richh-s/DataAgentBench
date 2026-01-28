code = """import json

# Load data
funding_data = json.load(open(locals()['var_functions.query_db:2']))
civic_docs = json.load(open(locals()['var_functions.query_db:5']))

# Find capital design projects from civic documents
capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    capture_mode = False
    for line in lines:
        clean_line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in clean_line:
            capture_mode = True
        elif capture_mode:
            # Stop at next major section
            if 'Capital Improvement Projects (Construction)' in clean_line or 'Disaster Recovery' in clean_line:
                break
            # Capture project names
            if clean_line and len(clean_line) > 10 and 'Project' in clean_line:
                if 'fema' not in clean_line.lower() and 'disaster' not in clean_line.lower():
                    capital_design_projects.add(clean_line)

# Count of design projects found
print(f'Design projects found: {len(capital_design_projects)}')

# Count funded projects > 50000
funded_matches = set()

for record in funding_data:
    amount = int(record['Amount'])
    project_name = record['Project_Name']
    
    if amount > 50000:
        # Match project (remove suffix like (FEMA Project))
        base_name = project_name.split('(')[0].strip()
        if base_name in capital_design_projects:
            funded_matches.add(base_name)

result = funded_matches
print('__RESULT__:')
print(json.dumps({'count': len(result)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
