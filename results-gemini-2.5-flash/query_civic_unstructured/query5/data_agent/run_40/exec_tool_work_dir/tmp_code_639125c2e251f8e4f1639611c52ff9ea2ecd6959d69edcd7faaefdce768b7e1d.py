code = """import json
import re

with open(locals()['var_function-call-9226438263479244870'], 'r') as f:
    documents = json.load(f)

disaster_projects_2022 = []

for doc in documents:
    text = doc['text']
    
    # Split text into sections that might represent projects
    # Projects usually follow a pattern: Project Name \n (cid:190) Updates: ... (cid:190) Project Schedule: ...
    project_sections = re.split(r'\n\s*([A-Za-z0-9][A-Za-z0-9 &\-/]*?(?: Project| Improvements| Plan| Repairs| Study)?)\n\s*\(cid:190\)\s*Updates:', text)
    
    # The first element before the first project might be general text, so we skip it.
    # The split often creates alternating project name and project details.
    for i in range(1, len(project_sections), 2):
        project_name = project_sections[i].strip()
        if i + 1 < len(project_sections):
            project_details = project_sections[i+1]
            
            # Check if it's a disaster-related project
            is_disaster_project = False
            if re.search(r'disaster|FEMA|recovery|fire|emergency', project_details, re.IGNORECASE) or \
               re.search(r'Disaster Recovery Projects', project_name, re.IGNORECASE):
                is_disaster_project = True

            if is_disaster_project:
                # Check for start date in 2022 in the Project Schedule section
                schedule_match = re.search(r'Project Schedule:.*?((?:Begin Construction|Advertise|Complete Design|st):\s*(?:2022[\s\-A-Za-z]*|Spring 2022|Fall 2022|Summer 2022|Winter 2022))' , project_details, re.DOTALL)
                
                if schedule_match:
                    date_info = schedule_match.group(1)
                    if '2022' in date_info:
                        disaster_projects_2022.append(project_name)

# Remove duplicates and filter out generic headers
final_disaster_projects_2022 = []
for project in list(set(disaster_projects_2022)):
    if not (project.lower().startswith('capital improvement projects') or
            project.lower().startswith('disaster recovery projects') or
            project.lower().startswith('public works commission') or
            project.lower().startswith('agenda report') or
            project.lower().startswith('public works') or
            project.lower().startswith('item') or
            project.lower().startswith('to:') or
            project.lower().startswith('prepared by:') or
            project.lower().startswith('approved by:') or
            project.lower().startswith('date prepared:') or
            project.lower().startswith('meeting date:') or
            project.lower().startswith('subject:') or
            project.lower().startswith('recommended action:') or
            project.lower().startswith('discussion:')):
        final_disaster_projects_2022.append(project)

print("__RESULT__:")
print(json.dumps(final_disaster_projects_2022))"""

env_args = {'var_function-call-14874373830466001573': ['civic_docs'], 'var_function-call-6587384332537770908': [], 'var_function-call-9226438263479244870': 'file_storage/function-call-9226438263479244870.json', 'var_function-call-3865910938844144022': []}

exec(code, env_args)
