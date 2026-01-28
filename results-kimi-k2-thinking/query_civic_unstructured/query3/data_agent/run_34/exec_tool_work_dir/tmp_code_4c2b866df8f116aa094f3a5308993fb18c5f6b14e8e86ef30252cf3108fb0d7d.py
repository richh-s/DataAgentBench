code = """import json

# Load the civic documents data from the stored file
civic_data = locals()['var_functions.query_db:6']
with open(civic_data, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data from the stored file
funding_data = locals()['var_functions.query_db:7']
with open(funding_data, 'r') as f:
    funding_records = json.load(f)

# Initialize results
civic_projects = []
fema_funding = []

# Search for FEMA and emergency related projects in civic documents
text = civic_docs[0].get('text', '')
lowercase_text = text.lower()

# Simple extraction - find lines that mention FEMA or emergency and look like project names
lines = text.split('\n')
for i, line in enumerate(lines):
    line = line.strip()
    if line and len(line) < 80 and not line.startswith('(cid:') and not line.startswith('Page'):
        # Check surrounding context
        start = max(0, i-2)
        end = min(len(lines), i+8)
        context = ' '.join(lines[start:end]).lower()
        
        if 'fema' in context or 'emergency' in context:
            status = 'unknown'
            if 'construction' in context and 'completed' not in context:
                status = 'construction'
            elif 'completed' in context:
                status = 'completed'
            elif 'design' in context:
                status = 'design'
            
            project_type = 'disaster' if 'fema' in context else 'capital'
            
            civic_projects.append({
                'Project_Name': line,
                'status': status,
                'type': project_type
            })

# Filter funding records for FEMA or emergency
for record in funding_records:
    project_name = record.get('Project_Name', '')
    if 'FEMA' in project_name or 'emergency' in project_name.lower():
        fema_funding.append({
            'Project_Name': project_name,
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': record.get('Amount', 0)
        })

result = {
    'civic_projects': civic_projects[:15],  # Get first 15 to avoid duplicates
    'funding_records': fema_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
