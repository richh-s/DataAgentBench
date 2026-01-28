code = """import json

# Load data using locals() to access the stored file paths
civic_path = locals()['var_functions.query_db:6']
funding_path = locals()['var_functions.query_db:7']

with open(civic_path, 'r') as f1:
    civic_docs = json.load(f1)
with open(funding_path, 'r') as f2:
    funding_records = json.load(f2)

# Extract FEMA/emergency projects from civic documents
civic_projects = []
text = civic_docs[0].get('text', '')
lines = text.splitlines()

for i, line in enumerate(lines):
    line = line.strip()
    # Skip empty or marker lines
    if line and not line.startswith('(cid:') and 'Page' not in line and len(line) < 80:
        # Get context around this line
        context_start = max(0, i-2)
        context_end = min(len(lines), i+8)
        context = ' '.join(lines[context_start:context_end]).lower()
        
        if 'fema' in context or 'emergency' in context:
            status = 'unknown'
            if 'construction' in context and 'completed' not in context:
                status = 'construction'
            elif 'completed' in context:
                status = 'completed'
            elif 'design' in context or 'awaiting' in context:
                status = 'design'
            
            proj_type = 'disaster' if 'fema' in context else 'capital'
            
            civic_projects.append({
                'Project_Name': line,
                'status': status,
                'type': proj_type
            })

# Filter funding for FEMA/emergency projects
fema_funding = []
for record in funding_records:
    proj_name = record.get('Project_Name', '')
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        fema_funding.append({
            'Project_Name': proj_name,
            'Funding_Source': record.get('Funding_Source'),
            'Amount': record.get('Amount')
        })

# Final result
result = {
    'projects_from_civic_docs': civic_projects[:15],
    'funding_records': fema_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
