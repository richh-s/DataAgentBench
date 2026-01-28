code = """import json

# Load data
funding_data = json.load(open(locals()['var_functions.query_db:40']))
civic_docs = json.load(open(locals()['var_functions.query_db:5'], encoding='utf-8'))

# Find capital design projects from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design projects mentioned by looking for specific sections
    if 'Design' in text:
        # Look for capital improvement design section
        design_section = False
        lines = text.split('\n')
        for line in lines:
            clean = line.strip()
            if 'Capital Improvement Projects (Design)' in clean:
                design_section = True
            elif design_section and ('Capital Improvement Projects (Construction)' in clean or 'Disaster Recovery' in clean):
                design_section = False
            elif design_section and clean:
                # Collect potential project names
                if len(clean) > 10 and 'Project' in clean and 'fema' not in clean.lower():
                    design_projects.add(clean)

# Match with funding > $50,000
matched = set()

for rec in funding_data:
    if int(rec['Amount']) > 50000:
        name = rec['Project_Name']
        # Remove any suffix in parentheses
        if '(' in name:
            base = name.split('(')[0].strip()
        else:
            base = name
        if base in design_projects:
            matched.add(base)

result = {'count': len(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
