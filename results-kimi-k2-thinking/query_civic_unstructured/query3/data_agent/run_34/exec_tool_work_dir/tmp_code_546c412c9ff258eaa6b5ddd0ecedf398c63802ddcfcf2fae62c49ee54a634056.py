code = """import json
import re

# Read data files
civic_docs = json.load(open(var_functions.query_db:6))
funding_data = json.load(open(var_functions.query_db:7))

# Process civic documents
projects = []
doc = civic_docs[0]
text = doc.get('text', '')

# Find projects mentioning FEMA or emergency
# Split by lines and look for project patterns
for section in re.split(r'\n\s*[A-Z\s\(\)]+\n', text):
    if 'FEMA' in section or 'emergency' in section.lower():
        lines = section.strip().split('\n')
        if lines:
            # First line is likely the project name
            project_name = lines[0].strip()
            if project_name and len(project_name) < 100:
                # Determine status
                status = 'unknown'
                section_lower = section.lower()
                if 'construction' in section_lower and 'completed' not in section_lower:
                    status = 'construction'
                elif 'completed' in section_lower:
                    status = 'completed'
                elif 'design' in section_lower or 'awaiting' in section_lower:
                    status = 'design'
                
                # Determine type
                project_type = 'disaster' if 'FEMA' in section else 'capital'
                
                projects.append({
                    'Project_Name': project_name,
                    'status': status,
                    'type': project_type
                })

# Filter funding data
funding_records = []
for fund in funding_data:
    name = fund.get('Project_Name', '')
    if 'FEMA' in name or 'emergency' in name.lower():
        funding_records.append({
            'Project_Name': name,
            'Funding_Source': fund.get('Funding_Source', ''),
            'Amount': fund.get('Amount', 0)
        })

print('__RESULT__:')
print(json.dumps({
    'civic_projects': projects,
    'funding_records': funding_records
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
