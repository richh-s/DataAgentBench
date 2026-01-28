code = """import json
import re

# Load funding data
funding_path = var_functions.query_db:2
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_path = var_functions.query_db:6
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding map for projects with amount > 50000
funding_map = {}
for record in funding_data:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean_name] = amount

# Extract capital design projects from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Check for section headers
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            in_design_section = False
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            in_design_section = False
            continue
        
        # Process lines in design section
        if in_design_section and line and len(line) > 10:
            # Skip disaster projects
            if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                continue
            
            # Skip meta lines
            if any(word in line.upper() for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA']):
                continue
            
            # Skip section headers and bullet points
            if any(phrase in line for phrase in ['Updates:', 'Schedule:', 'Capital Improvement']):
                continue
            
            if line.startswith('(') or line.startswith('\u2022'):
                continue
            
            # Add project
            capital_design_projects.append(line)

# Count matches with funding
count = 0
matched = []

for project in capital_design_projects:
    project_clean = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
    
    if project in funding_map or project_clean in funding_map:
        count += 1
        amount = funding_map.get(project) or funding_map.get(project_clean, 0)
        matched.append({'name': project, 'amount': int(amount)})

result = {'count': count, 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
