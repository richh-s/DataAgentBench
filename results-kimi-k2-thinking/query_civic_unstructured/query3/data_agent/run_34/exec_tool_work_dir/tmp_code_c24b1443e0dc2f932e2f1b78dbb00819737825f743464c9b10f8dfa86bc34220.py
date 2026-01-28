code = """import json

# Load data
civic_file = open(var_functions.query_db:6)
civic_docs = json.load(civic_file)
civic_file.close()

funding_file = open(var_functions.query_db:7)
funding_data = json.load(funding_file)
funding_file.close()

# Find FEMA/emergency projects
civic_projects = []
doc_text = civic_docs[0]['text']
lines = doc_text.split('
')

for line in lines:
    line = line.strip()
    if line and len(line) < 80 and line[0].isupper() and '(cid:' not in line and 'Page' not in line:
        # Check context
        context_start = max(0, lines.index(line) - 2)
        context_end = min(len(lines), lines.index(line) + 8)
        context = ' '.join(lines[context_start:context_end]).lower()
        
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

# Filter funding
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
    'civic_projects': civic_projects[:15],
    'funding_records': funding_records
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
