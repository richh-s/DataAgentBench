code = """import json
import re

with open(locals()['var_function-call-9226438263479244870'], 'r') as f:
    documents = json.load(f)

disaster_projects_2022_names = []

for doc in documents:
    text = doc['text']
    
    # Use a more robust pattern to split documents into project sections.
    # Look for a line that starts with an uppercase letter, followed by text, and ends with a common project suffix.
    # This is followed by a newline and '(cid:190) Updates:'.
    # The split also captures the project name as part of the split result.
    project_sections = re.split(r'\n([A-Z][A-Za-z0-9 &\\-/,'.()]*?(?: Project| Improvements| Plan| Repairs| Study| System)?)\n\\s*\\(cid:190\\)\s*Updates:', text)

    # The first element of project_sections might be leading text before any project, so we ignore it.
    # Then, elements at odd indices are project names, and even indices are their details.
    if len(project_sections) > 1:
        for i in range(1, len(project_sections), 2):
            project_name = project_sections[i].strip()
            project_details = project_sections[i+1].strip() if (i+1 < len(project_sections)) else ""

            is_disaster = False
            # Check for disaster keywords in the project name or its details
            if re.search(r'disaster|FEMA|recovery|fire|emergency|CalOES|CalJPIA', project_name + " " + project_details, re.IGNORECASE):
                is_disaster = True

            if is_disaster:
                # Look for '2022' within the 'Project Schedule:' part of the details.
                # The date can be in various formats like '2022-Spring', '2022-Fall', '2022-02', etc.
                schedule_match = re.search(r'Project Schedule:.*?((?:Begin Construction|Advertise|Complete Design|Final Design|st):\\s*(?:2022[\\s\\-A-Za-z]*|Spring 2022|Fall 2022|Summer 2022|Winter 2022))' , project_details, re.DOTALL)
                
                if schedule_match:
                    date_info = schedule_match.group(1)
                    if '2022' in date_info:
                        disaster_projects_2022_names.append(project_name)

# Filter out duplicates and common non-project headers
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
            lower_project.startswith('fiscal year') or
            lower_project.startswith('malibu bluffs park') # Specific to this dataset if it's a false positive
           ):
        final_disaster_projects_2022.append(project)

print("__RESULT__:")
print(json.dumps(final_disaster_projects_2022))"""

env_args = {'var_function-call-14874373830466001573': ['civic_docs'], 'var_function-call-6587384332537770908': [], 'var_function-call-9226438263479244870': 'file_storage/function-call-9226438263479244870.json', 'var_function-call-3865910938844144022': []}

exec(code, env_args)
