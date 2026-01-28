code = """import json

# Access the civic documents data using locals() as mentioned in instructions
civic_docs_result = locals()['var_functions.query_db:5']

# Load the data
if isinstance(civic_docs_result, str) and civic_docs_result.endswith('.json'):
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_result

print("Number of civic docs loaded:", len(civic_docs))

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
        if current_section is None:
            continue
            
        # Skip lines with bullet points or special markers
        if line.startswith('(') or line.startswith('•') or 'cid:' in line:
            continue
        if line.isupper() or line.lower().startswith('page') or 'PROJECTS' in line.upper():
            continue
        
        # Skip schedule/updates lines
        lower_line = line.lower()
        skip_markers = ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'project description:', 'estimated schedule:', 'complete construction:', 'project updates:']
        if any(marker in lower_line for marker in skip_markers):
            continue
            
        # Skip single words that are status labels
        if line.lower() in ['design', 'construction', 'not started']:
            continue
            
        # Skip if too short
        if len(line) < 5:
            continue
        
        # Clean up line
        project_name = line
        for prefix in ['·', '•', '-', '▪']:
            if project_name.startswith(prefix):
                project_name = project_name[1:].strip()
        
        # Skip header/footer content
        skip_phrases = ['public works', 'commission', 'agenda', 'report', 'meeting', 'prepared by', 'approved by', 'subject', 'date prepared']
        if any(phrase in project_name.lower() for phrase in skip_phrases):
            continue
            
        # Skip dates
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

print("Total unique projects extracted:", len(unique_projects))

# Filter for capital projects with design status
capital_design_projects = [p for p in unique_projects if p['type'] == 'capital' and p['status'] == 'design']

print("Capital projects with design status:", len(capital_design_projects))
for proj in capital_design_projects[:15]:
    print("  -", proj['Project_Name'])

# Save result as JSON string
result = json.dumps(capital_design_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
