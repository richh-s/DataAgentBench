code = """import json

# Load funding data
with open(locals()['var_functions.query_db:40'], 'r') as f:
    funding = json.load(f)

# Load civic documents  
with open(locals()['var_functions.query_db:5'], 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Find capital design projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    if 'Capital Improvement Projects (Design)' in text:
        # Get chunk after design header
        start = text.index('Capital Improvement Projects (Design)')
        chunk = text[start:start + 2500]
        
        # Find project names
        for line in chunk.split('\n'):
            stripped = line.strip()
            if len(stripped) > 10 and 'Project' in stripped:
                if 'fema' not in stripped.lower():
                    design_projects.add(stripped)

# Count funded projects > 50000
funded = set()
for rec in funding:
    amt = int(rec['Amount'])
    if amt > 50000:
        proj_name = rec['Project_Name']
        # Remove suffix if any
        if '(' in proj_name:
            base = proj_name.split('(')[0].strip()
        else:
            base = proj_name
        
        if base in design_projects:
            funded.add(base)

result = {'count': len(funded)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
