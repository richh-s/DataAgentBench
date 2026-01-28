code = """import json
import re

# Load data
funding_data = json.load(open(locals()['var_functions.query_db:40']))
civic_docs = json.load(open(locals()['var_functions.query_db:5'], encoding='utf-8'))

# Find capital design projects from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find capital improvement design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start >= 0:
        # Get a reasonable sized chunk
        section = text[design_start:design_start + 3000]
        
        # Look for project names (text before bullet points or updates)
        pattern = r'\n([A-Z][a-zA-Z0-9\s&\-\/]+?Project)(?=\s*\n\s*[\u2022\-])'
        matches = re.findall(pattern, section)
        
        for proj in matches:
            # Clean and filter
            if len(proj) > 10 and 'fema' not in proj.lower():
                design_projects.add(proj.strip())

# Match with funding > $50,000
matched = set()

for rec in funding_data:
    amount = int(rec['Amount'])
    if amount > 50000:
        proj_name = rec['Project_Name']
        # Remove suffix
        base_name = proj_name.split('(')[0].strip()
        if base_name in design_projects:
            matched.add(base_name)

result = {'count': len(matched)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
