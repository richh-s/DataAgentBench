code = """import json, re

filepath1 = locals()['var_functions.query_db:6']
with open(filepath1, 'r') as f:
    civic_docs = json.load(f)

filepath2 = locals()['var_functions.query_db:8']
with open(filepath2, 'r') as f:
    funding_data = json.load(f)

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for completed park projects in 2022
    pattern = r'([A-Za-z\s]+Park[A-Za-z\s]*)[^\n]*?(?:Construction was completed|construction was completed)[^\n]*2022'
    matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
    
    for match in matches:
        project_name = match.group(1).strip()
        if project_name and len(project_name) < 150:
            park_projects.append(project_name)

# Also check for generic pattern that captures more park projects
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check if line mentions a park and next lines mention completion in 2022
        if 'Park' in line and len(line) < 150:
            project_name = line.strip()
            # Check following lines for completion and 2022
            context = '\n'.join(lines[i:i+5])
            if ('completed' in context.lower() or 'Complete' in context) and '2022' in context:
                if 'park' in project_name.lower() and project_name not in park_projects:
                    park_projects.append(project_name)

# Match with funding records
funding_matches = []
for project in park_projects:
    proj_lower = project.lower().strip()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        
        # Check for match
        if proj_lower == fund_name:
            funding_matches.append({'project': project, 'amount': int(fund['Amount'])})
        elif fund_name.startswith(proj_lower):
            funding_matches.append({'project': project, 'amount': int(fund['Amount'])})
        elif proj_lower.startswith(fund_name):
            funding_matches.append({'project': project, 'amount': int(fund['Amount'])})

total = sum(f['amount'] for f in funding_matches)
result = {'total_funding': total, 'projects_matched': len(funding_matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
