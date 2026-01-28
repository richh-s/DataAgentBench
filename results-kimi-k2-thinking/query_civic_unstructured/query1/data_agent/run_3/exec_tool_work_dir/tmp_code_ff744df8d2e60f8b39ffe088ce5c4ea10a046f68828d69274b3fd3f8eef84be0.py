code = """import json
import re

# Load data from files
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Find capital design project names from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find capital improvement design section
    if 'Capital Improvement Projects (Design)' in text:
        # Extract section until next major heading
        start_idx = text.index('Capital Improvement Projects (Design)')
        section = text[start_idx:start_idx + 2500]
        
        # Look for project name patterns
        for line in section.split('\n'):
            clean = line.strip()
            if len(clean) > 10 and 'Project' in clean and 'fema' not in clean.lower():
                design_projects.add(clean)

# Match with funding > 50,000
matched = set()

for rec in funding:
    amount = int(rec['Amount'])
    if amount > 50000:
        name = rec['Project_Name']
        # Remove parenthetical suffix
        base = re.sub(r'\s*\([^)]*\)$', '', name)
        if base in design_projects:
            matched.add(base)

result = {'count': len(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
