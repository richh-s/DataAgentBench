code = """import json
import re

# Read data from files
civic_path = var_functions.query_db:6
funding_path = var_functions.query_db:7

civic_content = open(civic_path).read()
civic_docs = json.loads(civic_content)

funding_content = open(funding_path).read()
funding_data = json.loads(funding_content)

# Extract FEMA/emergency projects from civic docs
projects = []
doc = civic_docs[0]
text = doc.get('text', '')

# Find projects mentioning FEMA or emergency
sections = re.split(r'\n\s*\n', text)
for section in sections:
    if 'FEMA' in section or 'emergency' in section.lower():
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('(cid:') and len(line) < 80:
                status = 'unknown'
                section_text = section.lower()
                if 'under construction' in section_text:
                    status = 'construction'
                elif 'completed' in section_text:
                    status = 'completed'
                elif 'design' in section_text:
                    status = 'design'
                
                project_type = 'disaster' if 'FEMA' in section else 'capital'
                
                projects.append({'Project_Name': line, 'status': status, 'type': project_type})
                break

# Filter funding data
funding = []
for record in funding_data:
    name = record.get('Project_Name', '')
    if 'FEMA' in name or 'emergency' in name.lower():
        funding.append({
            'Project_Name': name,
            'Funding_Source': record.get('Funding_Source'),
            'Amount': record.get('Amount')
        })

result = {'projects': projects, 'funding': funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
