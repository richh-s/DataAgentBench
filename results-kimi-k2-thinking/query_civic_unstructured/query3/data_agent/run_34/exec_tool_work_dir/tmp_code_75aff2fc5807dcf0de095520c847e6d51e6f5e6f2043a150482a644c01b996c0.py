code = """import json

# Read the civic documents
with open(var_functions.query_db:6, 'r') as civic_file:
    civic_docs = json.load(civic_file)

# Read the funding data  
with open(var_functions.query_db:7, 'r') as funding_file:
    funding_data = json.load(funding_file)

# Simple search for FEMA and emergency projects
civic_text = civic_docs[0]['text']
civic_projects = []

# Look for project names and their status - simple approach
lines = civic_text.split('\n')
for i in range(len(lines)):
    line = lines[i].strip()
    # Check if this looks like a project name (reasonably short, starts with capital, not a bullet)
    if line and not line.startswith('(cid:') and not line.startswith('Page') and len(line) < 80 and line[0].isupper():
        # Look ahead for project context
        context = ' '.join(lines[i:i+10]).lower()
        if 'fema' in context or 'emergency' in context:
            status = 'unknown'
            if 'construction' in context and 'completed' not in context:
                status = 'construction'
            elif 'completed' in context:
                status = 'completed'
            elif 'design' in context:
                status = 'design'
            
            project_type = 'disaster' if 'fema' in context else 'capital'
            civic_projects.append({'Project_Name': line, 'status': status, 'type': project_type})

# Filter funding records
funding_records = []
for record in funding_data:
    name = record.get('Project_Name', '')
    if 'FEMA' in name or 'emergency' in name.lower():
        funding_records.append({
            'Project_Name': name,
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': record.get('Amount', 0)
        })

result = {
    'civic_projects': civic_projects[:20],  # Limit to avoid too many
    'funding_records': funding_records
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
