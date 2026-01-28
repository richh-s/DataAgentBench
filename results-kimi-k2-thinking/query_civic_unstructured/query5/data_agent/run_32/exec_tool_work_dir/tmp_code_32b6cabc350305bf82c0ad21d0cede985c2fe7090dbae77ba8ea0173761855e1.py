code = """import json
import re

# Load the data from the stored variables
# The results are stored in variables named after the tool call IDs
funding_data = locals().get('var_functions.query_db:4', [])
civic_docs_data = locals().get('var_functions.query_db:5', [])

# If the data is not directly available, it might be file paths
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

# Process funding data into dictionary for easy lookup
funding_dict = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_dict[proj_name] = amount

# Extract project information from civic documents  
def extract_projects_from_text(text):
    projects = []
    if not text:
        return projects
        
    lines = text.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Pattern: Project Name (status)
        project_match = re.match(r'^([^(]+)\(([a-zA-Z\s]+)\)$', line)
        if project_match and i + 4 < len(lines):
            project_name = project_match.group(1).strip()
            status = project_match.group(2).strip().lower()
            
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

# Extract all projects from documents
all_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    projects = extract_projects_from_text(text)
    all_projects.extend(projects)

# Filter for disaster projects starting in 2022
disaster_projects_2022 = []

# First get explicitly marked disaster projects
for proj in all_projects:
    if proj.get('type') == 'disaster' and '2022' in proj.get('st', ''):
        disaster_projects_2022.append(proj)

# Then add projects with FEMA/CalJPIA/CalOES indicators
fema_pattern = r'\((FEMA|CalJPIA|CalOES)\s*Project\)'
for proj in all_projects:
    proj_name = proj.get('Project_Name', '')
    if re.search(fema_pattern, proj_name, re.IGNORECASE) and '2022' in proj.get('st', ''):
        # Mark as disaster type
        proj_copy = proj.copy()
        proj_copy['type'] = 'disaster'
        # Avoid duplicates
        if proj_copy not in disaster_projects_2022:
            disaster_projects_2022.append(proj_copy)

# Remove duplicates based on project name
unique_names = set()
unique_projects = []
for proj in disaster_projects_2022:
    name = proj['Project_Name']
    if name not in unique_names:
        unique_names.add(name)
        unique_projects.append(proj)

# Match with funding data and calculate total
total_funding = 0
funded_projects = []

for proj in unique_projects:
    proj_name = proj['Project_Name']
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        total_funding += amount
        funded_projects.append({
            'Project_Name': proj_name,
            'Amount': amount
        })

result = {
    'total_funding_2022_disaster_projects': total_funding,
    'number_of_projects': len(funded_projects),
    'funded_projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
