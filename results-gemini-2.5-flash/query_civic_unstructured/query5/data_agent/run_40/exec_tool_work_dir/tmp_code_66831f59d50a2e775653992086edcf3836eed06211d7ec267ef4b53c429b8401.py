code = """import json
import re

with open(locals()['var_function-call-9226438263479244870'], 'r') as f:
    documents = json.load(f)

disaster_projects_2022_names = []

for doc in documents:
    text = doc['text']
    
    # Split the document into potential project blocks. Each block typically starts with a Project Name
    # and then contains updates and schedule. We'll use a general pattern to split.
    # The regex looks for a line starting with an uppercase letter, then possibly other characters,
    # and ending with words like 'Project', 'Improvements', etc., followed by '\n(cid:190) Updates:'
    # The non-greedy `.*?` is crucial here.
    
    # This pattern will split the text into chunks, where each chunk *should* start with a project name
    # and contain its details.
    project_chunks = re.split(r'\n([A-Z][A-Za-z0-9 &\\-/,'.()]+(?: Project| Improvements| Plan| Repairs| Study| System)?)\n\\s*\\(cid:190\\)\s*Updates:', text)

    # The first element might be text before the first project, so we iterate from the second element,
    # taking project name and details in pairs.
    if len(project_chunks) > 1:
        for i in range(1, len(project_chunks), 2):
            project_name = project_chunks[i].strip()
            details_block = project_chunks[i+1].strip() if (i+1 < len(project_chunks)) else ""
            
            is_disaster_project = False
            # Check for disaster keywords in the project name or details block
            if re.search(r'disaster|FEMA|recovery|fire|emergency|CalOES|CalJPIA', project_name + " " + details_block, re.IGNORECASE):
                is_disaster_project = True

            if is_disaster_project:
                # Check for '2022' within the 'Project Schedule' part of the details block
                schedule_match = re.search(r'Project Schedule:.*?((?:Begin Construction|Advertise|Complete Design|Final Design|st):\\s*(?:2022[\\s\\-A-Za-z]*|Spring 2022|Fall 2022|Summer 2022|Winter 2022))' , details_block, re.DOTALL)
                
                if schedule_match:
                    date_info = schedule_match.group(1)
                    if '2022' in date_info:
                        disaster_projects_2022_names.append(project_name)

# Clean up and filter the project names
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
            lower_project.startswith('fiscal year') # Added another common header
           ):
        final_disaster_projects_2022.append(project)

print("__RESULT__:")
print(json.dumps(final_disaster_projects_2022))"""

env_args = {'var_function-call-14874373830466001573': ['civic_docs'], 'var_function-call-6587384332537770908': [], 'var_function-call-9226438263479244870': 'file_storage/function-call-9226438263479244870.json', 'var_function-call-3865910938844144022': []}

exec(code, env_args)
