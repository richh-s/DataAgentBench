code = """import json
import re

# Load the funding data (from var_functions.query_db:4)
with open('/tmp/tmp_hb9f3fdk.json', 'r') as f:
    funding_data = json.load(f)

# Load the civic docs data (from var_functions.query_db:5)
with open('/tmp/tmp_cdv8r04p.json', 'r') as f:
    civic_docs_data = json.load(f)

# Process funding data into dictionary for easy lookup
funding_dict = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_dict[proj_name] = amount

# Extract project information from civic documents
def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for project name lines (often have status in parentheses)
        project_match = re.match(r'^([^(]+)\(([a-zA-Z\s]+)\)$', line)
        if project_match and i + 4 < len(lines):
            project_name = project_match.group(1).strip()
            status = project_match.group(2).strip().lower()
            
            # Look for next lines with topic, type, st, et
            topic = None
            type_val = None
            st = None
            et = None
            
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].strip()
                if next_line.startswith('topic:'):
                    topic = next_line.replace('topic:', '').strip()
                elif next_line.startswith('type:'):
                    type_val = next_line.replace('type:', '').strip()
                elif next_line.startswith('st:'):
                    st = next_line.replace('st:', '').strip()
                elif next_line.startswith('et:'):
                    et = next_line.replace('et:', '').strip()
            
            if topic and type_val and st:
                projects.append({
                    'Project_Name': project_name,
                    'topic': topic,
                    'type': type_val,
                    'status': status,
                    'st': st,
                    'et': et
                })
        
        i += 1
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    projects = extract_projects_from_text(text)
    all_projects.extend(projects)

# Filter for disaster projects that started in 2022
# First pass: explicitly marked as disaster type
explicit_disaster = []
for proj in all_projects:
    if proj['type'] == 'disaster' and '2022' in proj['st']:
        explicit_disaster.append(proj)

# Second pass: look for FEMA/CalJPIA/CalOES in project name
fema_disaster = []
fema_pattern = r'\((FEMA|CalJPIA|CalOES)\s*Project\)'

# Only check projects that weren't already captured
remaining_projects = [p for p in all_projects if p not in explicit_disaster]

for proj in remaining_projects:
    if re.search(fema_pattern, proj['Project_Name'], re.IGNORECASE) and '2022' in proj['st']:
        proj_copy = proj.copy()
        proj_copy['type'] = 'disaster'
        fema_disaster.append(proj_copy)

# Combine all disaster projects from 2022
all_disaster_projects = explicit_disaster + fema_disaster

# Remove duplicates based on project name
unique_projects = {}
for proj in all_disaster_projects:
    proj_name = proj['Project_Name']
    if proj_name not in unique_projects:
        unique_projects[proj_name] = proj

final_disaster_projects = list(unique_projects.values())

# Match with funding data
total_funding = 0
funded_projects = []

for proj in final_disaster_projects:
    proj_name = proj['Project_Name']
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        total_funding += amount
        funded_projects.append({
            'Project_Name': proj_name,
            'Amount': amount,
            'st': proj['st']
        })

# Return results
result = {
    'total_fundin_2022_disaster_projects': total_funding,
    'number_of_projects': len(funded_projects),
    'projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
