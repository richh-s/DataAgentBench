code = """import json
import re

with open(locals()['var_function-call-9226438263479244870'], 'r') as f:
    documents = json.load(f)

disaster_projects_2022 = []

for doc in documents:
    text = doc['text']

    # This regex tries to capture a project name and its entire description block.
    # It looks for a line that seems like a project name, then captures everything until the next such line or end of document.
    # The pattern for project name: A line starting with an uppercase letter, followed by various characters,
    # and potentially ending with common project-related words like 'Project', 'Improvements', etc.
    # This is followed by '(cid:190) Updates:' and then captures all content until the next project header or end of the document.
    project_blocks = re.findall(
        r'([A-Z][A-Za-z0-9 &\\-/,'.()]+(?: Project| Improvements| Plan| Repairs| Study| System)?)\\n\\s*\\(cid:190\\)\\s*Updates:(.*?)(?=\\n\\s*[A-Z][A-Za-z0-9 &\\-/,'.()]+(?: Project| Improvements| Plan| Repairs| Study| System)?\\n\\s*\\(cid:190\\)\\s*Updates:|$)',
        text, re.DOTALL
    )

    for project_name, details in project_blocks:
        project_name = project_name.strip()
        details = details.strip()

        is_disaster_project = False
        # Check for disaster-related keywords in both project name and details
        if re.search(r'disaster|FEMA|recovery|fire|emergency|CalOES|CalJPIA', project_name + details, re.IGNORECASE):
            is_disaster_project = True

        if is_disaster_project:
            # Now, check for '2022' within the 'Project Schedule' section of the details
            schedule_match = re.search(
                r'Project Schedule:.*?((?:Complete Design|Advertise|Begin Construction|Final Design|st):\\s*(?:2022[\\s\\-A-Za-z]*|Spring 2022|Fall 2022|Summer 2022|Winter 2022))',
                details, re.DOTALL
            )
            if schedule_match:
                date_info = schedule_match.group(1)
                if '2022' in date_info:
                    disaster_projects_2022.append(project_name)

# Remove duplicates and filter out known non-project headers
final_disaster_projects_2022 = []
for project in list(set(disaster_projects_2022)):
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
