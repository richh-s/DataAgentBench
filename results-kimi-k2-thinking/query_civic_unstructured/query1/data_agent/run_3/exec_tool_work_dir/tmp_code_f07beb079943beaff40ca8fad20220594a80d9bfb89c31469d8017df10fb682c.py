code = """import json
import re

# Load data
funding_file = locals()['var_functions.query_db:40']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Find capital design projects from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    start = text.find('Capital Improvement Projects (Design)')
    if start >= 0:
        # Find end of section (next major heading)
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end < 0:
            end = len(text)
        
        section = text[start:end]
        
        # Extract project names from section
        # Look for lines with Project in them
        lines = section.split('\n')
        for line in lines:
            clean = line.strip()
            if (len(clean) > 10 and 'Project' in clean and 
                'fema' not in clean.lower() and 'disaster' not in clean.lower()):
                design_projects.add(clean)

# Match with funding data > $50,000
matched = set()

for rec in funding_data:
    if int(rec['Amount']) > 50000:
        name = rec['Project_Name']
        # Normalize name by removing parenthetical suffix
        base = name.split('(')[0].strip()
        if base in design_projects:
            matched.add(base)

count = len(matched)

# Create result dict
result_dict = {'count': count}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
