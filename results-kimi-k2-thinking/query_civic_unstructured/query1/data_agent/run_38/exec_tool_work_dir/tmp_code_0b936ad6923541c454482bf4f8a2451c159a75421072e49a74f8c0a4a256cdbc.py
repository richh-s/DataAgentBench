code = """import json

# Access the civic documents data
civic_docs_result = var_functions.query_db:5

# Load the data
if isinstance(civic_docs_result, str) and civic_docs_result.endswith('.json'):
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_result

print(f"Number of civic docs: {len(civic_docs)}")

# Extract project information
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    current_section = None
    in_disaster_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check section headers
        if 'DISASTER RECOVERY' in line.upper():
            in_disaster_section = True
            if '(Design)' in line:
                current_section = 'design'
            elif '(Construction)' in line:
                current_section = 'construction'
            elif '(Not Started)' in line:
                current_section = 'not_started'
            continue
        
        if 'CAPITAL IMPROVEMENT' in line.upper():
            in_disaster_section = False
            if '(Design)' in line:
                current_section = 'design'
            elif '(Construction)' in line:
                current_section = 'construction'
            elif '(Not Started)' in line:
                current_section = 'not_started'
            continue
        
        # Extract project names
        if (current_section and 
            len(line) > 5 and
            not line.startswith('(') and 
            not line.startswith('•') and 
            not any(marker in line.lower() for marker in ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'project description:', 'estimated schedule:', 'complete construction:']) and
            not line.isupper() and
            not line.lower().startswith('page') and
            'PROJECTS' not in line.upper() and
            not any(line.lower() == word for word in ['design', 'construction', 'not started'])):
            
            project_name = line.strip()
            
            # Clean up
            for prefix in ['·', '•', '-', '▪']:
                if project_name.startswith(prefix):
                    project_name = project_name[1:].strip()
            
            # Skip headers/footers
            if any(phrase in project_name.lower() for phrase in ['public works', 'commission', 'agenda', 'report', 'meeting', 'prepared by', 'approved by', 'subject']):
                continue
            
            if any(char.isdigit() for char in project_name) and len(project_name) < 15:
                continue
            
            project_type = 'disaster' if in_disaster_section else 'capital'
            
            all_projects.append({
                'Project_Name': project_name,
                'status': current_section,
                'type': project_type
            })

# Remove duplicates
seen = set()
unique_projects = []
for proj in all_projects:
    key = (proj['Project_Name'], proj['status'], proj['type'])
    if key not in seen:
        seen.add(key)
        unique_projects.append(proj)

print(f"Total unique projects: {len(unique_projects)}")

# Filter for capital projects with design status
capital_design_projects = [p for p in unique_projects if p['type'] == 'capital' and p['status'] == 'design']

print(f"Capital projects with design status: {len(capital_design_projects)}")
for proj in capital_design_projects:
    print(f"  - {proj['Project_Name']}")

# Convert to JSON string
result = json.dumps(capital_design_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
