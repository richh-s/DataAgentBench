code = """import json

# Load data
civic_docs = locals()['var_functions.query_db:2']
if isinstance(civic_docs, str):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

funding_data = locals()['var_functions.query_db:6']
if isinstance(funding_data, str):
    with open(funding_data) as f:
        funding_data = json.load(f)

# Build a set of projects with funding > 50k
funded_projects = {}
for fund in funding_data:
    amount = int(fund['Amount'])
    if amount > 50000:
        funded_projects[fund['Project_Name']] = amount

# Simple pattern matching for design projects
design_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Split and get the section after the header
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            # Take a reasonable portion after the header
            section = parts[1][:5000]  # Limit to avoid parsing too much
            lines = section.split('\n')
            for line in lines:
                clean = line.strip()
                # Project names are typically capitalized, contain spaces, and are not control lines
                if (clean and len(clean) > 15 and ':' not in clean and 
                    'Updates' not in clean and 'Schedule' not in clean and
                    not clean.startswith('Page') and not clean.startswith('(') and
                    not clean.startswith('To:') and not clean.startswith('Date')):
                    design_names.append(clean)

# Count capital (non-disaster) design projects with funding > 50k
count = 0
for name in design_names[:30]:  # Limit to first 30 to avoid noise
    if '(FEMA' not in name and '(CalOES' not in name and '(CalJPIA' not in name:
        if name in funded_projects:
            count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
