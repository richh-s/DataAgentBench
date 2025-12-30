code = """import json
import re

with open(locals()['var_function-call-9226438263479244870'], 'r') as f:
    documents = json.load(f)

disaster_projects_2022_names = []

for doc in documents:
    text_lines = doc['text'].split('\n')
    
    current_project_name = None
    is_disaster_project = False
    found_2022_start = False
    
    for i, line in enumerate(text_lines):
        line_stripped = line.strip()

        # Try to identify a project name. Project names are usually capitalized and not starting with a bullet point or common header.
        # This pattern needs to be quite robust.
        # Let's look for lines that might be project names, often followed by (cid:190) Updates:
        if re.match(r'^[A-Z][A-Za-z0-9 &\\-/,'.()]+(?: Project| Improvements| Plan| Repairs| Study| System)?$', line_stripped) and \
           (i + 1 < len(text_lines) and '(cid:190) Updates:' in text_lines[i+1]):
            current_project_name = line_stripped
            is_disaster_project = False # Reset for new project
            found_2022_start = False # Reset for new project
            
            # Check if the project name itself contains disaster keywords
            if re.search(r'disaster|FEMA|recovery|fire|emergency|CalOES|CalJPIA', current_project_name, re.IGNORECASE):
                is_disaster_project = True
            continue
            
        # If we have a current_project_name, look for disaster keywords in the details section (until next project or end)
        if current_project_name and not is_disaster_project:
            if re.search(r'disaster|FEMA|recovery|fire|emergency|CalOES|CalJPIA', line_stripped, re.IGNORECASE):
                is_disaster_project = True
                
        # If it's a disaster project, look for 2022 in the project schedule
        if current_project_name and is_disaster_project and not found_2022_start:
            if 'Project Schedule:' in line_stripped:
                # Look in the current and next few lines for 2022
                for j in range(i, min(i + 5, len(text_lines))):
                    if '2022' in text_lines[j]:
                        found_2022_start = True
                        break
        
        # If both conditions are met, add the project name
        if current_project_name and is_disaster_project and found_2022_start:
            disaster_projects_2022_names.append(current_project_name)
            current_project_name = None # Reset to look for next project
            is_disaster_project = False
            found_2022_start = False

# Filter out duplicates and generic headers again
final_disaster_projects_2022 = []
for project in list(set(disaster_projects_2022_names)):
    lower_project = project.lower()
    if not (lower_project.startswith('capital improvement projects') or
            lower_project.startswith('disaster recovery projects') or
            lower_project.startswith('public works commission') or
            lower_project.startswith('agenda report') or
            lower_project.startswith('public works') or
            lower_project.startswith('item') or
            lower_project.startswith('to:') or
            lower_project.startswith('prepared by:') or
            lower_project.startswith('approved by:') or
            lower_project.startswith('date prepared:') or
            lower_project.startswith('meeting date:') or
            lower_project.startswith('subject:') or
            lower_project.startswith('recommended action:') or
            lower_project.startswith('discussion:') or
            lower_project.startswith('page') or
            lower_project.startswith('malibu bluffs park') # Specific to this dataset if it's a false positive
           ):
        final_disaster_projects_2022.append(project)

print("__RESULT__:")
print(json.dumps(final_disaster_projects_2022))"""

env_args = {'var_function-call-14874373830466001573': ['civic_docs'], 'var_function-call-6587384332537770908': [], 'var_function-call-9226438263479244870': 'file_storage/function-call-9226438263479244870.json', 'var_function-call-3865910938844144022': []}

exec(code, env_args)
