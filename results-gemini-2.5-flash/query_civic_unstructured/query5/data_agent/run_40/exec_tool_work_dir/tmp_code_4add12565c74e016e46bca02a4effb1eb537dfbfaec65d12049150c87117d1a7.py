code = """import json
import re

with open(locals()['var_function-call-9226438263479244870'], 'r') as f:
    documents = json.load(f)

disaster_projects_2022_names = []

for doc in documents:
    text = doc['text']

    # Regex to capture project blocks. A project block starts with a project name,
    # followed by "(cid:190) Updates:", and then details, potentially ending before the next project name or end of document.
    # The project name is typically on a line by itself, and then details follow.
    # I'll look for "Project_Name\n(cid:190) Updates:" as a start of a block.
    # This pattern might be too broad or too narrow, but it's a starting point based on the preview.

    # Revised regex: find blocks starting with a potential project name followed by updates/schedule.
    # This regex attempts to find "Project Name" followed by "(cid:190) Updates:" and "(cid:190) Project Schedule:".
    # It tries to capture the project name and the details block.
    project_blocks = re.findall(r'([A-Z][A-Za-z0-9 &\\-/,'.()]+(?: Project| Improvements| Plan| Repairs| Study| System)?)\\n\\s*\\(cid:190\\)\\s*Updates:(.*?)(?=\\n\\s*[A-Z][A-Za-z0-9 &\\-/,'.()]+(?: Project| Improvements| Plan| Repairs| Study| System)?\\n\\s*\\(cid:190\\)\\s*Updates:|$)', text, re.DOTALL)

    for project_name, details in project_blocks:
        project_name = project_name.strip()
        details = details.strip()

        # Check if it's a disaster-related project using keywords
        is_disaster = False
        if re.search(r'disaster|FEMA|recovery|fire|emergency|CalOES|CalJPIA', details, re.IGNORECASE) or \
           re.search(r'Disaster Recovery Projects', project_name, re.IGNORECASE) or \
           re.search(r'\\(FEMA Project\\)|\\(CalJPIA Project\\)|\\(CalOES Project\\)', project_name, re.IGNORECASE):
            is_disaster = True

        if is_disaster:
            # Check if the start date is in 2022 within the 'Project Schedule' section of the details
            schedule_match = re.search(r'Project Schedule:.*?((?:Complete Design|Advertise|Begin Construction|Final Design|st):\\s*(?:2022[\\s\\-A-Za-z]*|Spring 2022|Fall 2022|Summer 2022|Winter 2022))', details, re.DOTALL)
            if schedule_match:
                date_info = schedule_match.group(1)
                if '2022' in date_info:
                    disaster_projects_2022_names.append(project_name)

# Further filter out any generic headers that might have been picked up
final_disaster_projects_2022 = []
for project in list(set(disaster_projects_2022_names)):
    # Convert to lowercase for case-insensitive comparison
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
            lower_project.startswith('page')):
        final_disaster_projects_2022.append(project)

print("__RESULT__:")
print(json.dumps(final_disaster_projects_2022))"""

env_args = {'var_function-call-14874373830466001573': ['civic_docs'], 'var_function-call-6587384332537770908': [], 'var_function-call-9226438263479244870': 'file_storage/function-call-9226438263479244870.json', 'var_function-call-3865910938844144022': []}

exec(code, env_args)
