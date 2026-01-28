code = """import json
import re

# Read the funding data from the file
with open(var_functions.query_db:2, 'r') as f:
    funding_data = json.load(f)

# Read the civic documents data from the file
with open(var_functions.query_db:5, 'r') as f:
    civic_docs = json.load(f)

print("Files loaded successfully")
print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Extract projects with design status from civic documents
projects_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects (Design) section
    if 'Capital Improvement Projects (Design)' in text:
        # Extract the section
        start_idx = text.find('Capital Improvement Projects (Design)')
        end_idx = text.find('\n\n', start_idx)
        if end_idx == -1:
            end_idx = len(text)
        design_section = text[start_idx:end_idx]
        
        # Split into lines and find project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            if (line and 
                len(line) > 5 and 
                not line.startswith('\u2022') and  # not a bullet
                not line.startswith('-') and
                'Updates' not in line and
                'Project Schedule' not in line and
                'Capital Improvement' not in line and
                'Design' not in line):
                
                # Check if it looks like a project name (contains Project or is title case)
                if 'Project' in line or (line[0].isupper() and ' ' in line):
                    projects_info[line] = {
                        'type': 'capital',
                        'status': 'design'
                    }

# Find projects in text that have design status
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for pattern: Project Name followed by bullet points
    project_matches = re.findall(r'\n([A-Z][a-zA-Z\s&\-\/\d]+?\s*(?:Project)?)\s*\n\s*[\u2022\-]+\s*(Updates?|Status)', text)
    
    for match in project_matches:
        project_name = match[0].strip()
        if (len(project_name) > 10 and 
            'Capital Improvement' not in project_name and
            'Disaster Recovery' not in project_name and
            'FEMA' not in project_name):
            
            # Check if in design context
            idx = text.find(project_name)
            if idx > 0:
                context = text[max(0, idx-200):idx+200].lower()
                if 'design' in context:
                    projects_info[project_name] = {
                        'type': 'capital', 
                        'status': 'design'
                    }

# Filter for capital projects only
capital_projects = {k:v for k,v in projects_info.items() if 'disaster' not in k.lower() and 'fema' not in k.lower()}

print(f"\nDesign projects found: {len(projects_info)}")
print(f"Capital design projects: {len(capital_projects)}")

# Match with funding data > $50,000
matched_projects = []

for funding in funding_data:
    if int(funding['Amount']) > 50000:
        project_name = funding['Project_Name']
        
        # Direct match
        if project_name in capital_projects:
            matched_projects.append({
                'name': project_name,
                'amount': int(funding['Amount']),
                'funding_source': funding['Funding_Source']
            })
        else:
            # Remove suffixes
            base_name = re.sub(r'\s*\([^)]*\)$', '', project_name)
            if base_name in capital_projects:
                matched_projects.append({
                    'name': project_name,
                    'amount': int(funding['Amount']),
                    'funding_source': funding['Funding_Source']
                })

# Get unique projects
unique_names = set()
unique_projects = []

for proj in matched_projects:
    base_name = re.sub(r'\s*\([^)]*\)$', '', proj['name'])
    if base_name not in unique_names:
        unique_names.add(base_name)
        unique_projects.append(proj)

count = len(unique_projects)

result = {
    'count': count,
    'projects': unique_projects[:20]  # Limit for preview
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
