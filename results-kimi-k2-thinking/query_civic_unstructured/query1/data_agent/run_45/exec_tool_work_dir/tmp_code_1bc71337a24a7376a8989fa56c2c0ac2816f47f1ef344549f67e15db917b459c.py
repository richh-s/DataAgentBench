code = """import json, re

# Load the funding data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load the civic documents
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_documents = json.load(f)

# Create a dictionary of funding projects with amount > 50000
funding_map = {}
for record in funding_records:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        project_name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', project_name).strip()
        funding_map[project_name] = amount
        funding_map[clean_name] = amount

# Extract capital design projects from civic documents
capital_design_projects = []

for document in civic_documents:
    text = document.get('text', '')
    lines = text.split('\n')
    
    design_section = False
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            design_section = True
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            design_section = False
            continue
        
        if design_section and line and len(line) > 15:
            # Skip disaster projects
            if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                continue
            
            # Skip meta lines
            if any(word in line.upper() for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA']):
                continue
            
            # Skip section headers and bullet points
            if any(phrase in line for phrase in ['Updates:', 'Schedule:', 'Capital Improvement']):
                continue
            
            if line.startswith('('):
                continue
            
            capital_design_projects.append(line)

# Count projects that match funding criteria
count = 0
matched_projects = []

for project in capital_design_projects:
    clean_project = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
    
    if project in funding_map or clean_project in funding_map:
        count += 1
        amount = funding_map.get(project) or funding_map.get(clean_project, 0)
        matched_projects.append({
            'project_name': project,
            'funding_amount': int(amount)
        })

# Prepare final result
result = {
    'total_count': count,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
