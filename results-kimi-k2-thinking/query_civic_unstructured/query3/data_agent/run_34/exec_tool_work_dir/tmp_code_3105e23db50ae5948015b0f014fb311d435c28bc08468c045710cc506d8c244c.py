code = """import json

# Load data files
civic_data = open(var_functions.query_db:6, 'r').read()
civic_docs = json.loads(civic_data)

funding_data = open(var_functions.query_db:7, 'r').read()
funding_records = json.loads(funding_data)

# Process data
civic_projects = []
fema_funding = []

# Look at the civic document text
text = civic_docs[0]['text']
lines = text.split('\n')

for line in lines:
    line = line.strip()
    # Skip empty lines and markers
    if line == '' or '(cid:' in line or 'Page' in line:
        continue
    # Check if line looks like a project name (not too long, starts with capital)
    if len(line) < 80 and line[0].isupper():
        # Find context around this line
        line_num = lines.index(line)
        start = max(0, line_num - 3)
        end = min(len(lines), line_num + 10)
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
            
            civic_projects.append({'Project_Name': line, 'status': status, 'type': project_type})

# Get funding records with FEMA/emergency
for record in funding_records:
    pname = record.get('Project_Name', '')
    if 'FEMA' in pname or 'emergency' in pname.lower():
        fema_funding.append({
            'Project_Name': pname,
            'Funding_Source': record.get('Funding_Source'),
            'Amount': record.get('Amount')
        })

result = {
    'civic_projects': civic_projects[:15],
    'funding_records': fema_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
