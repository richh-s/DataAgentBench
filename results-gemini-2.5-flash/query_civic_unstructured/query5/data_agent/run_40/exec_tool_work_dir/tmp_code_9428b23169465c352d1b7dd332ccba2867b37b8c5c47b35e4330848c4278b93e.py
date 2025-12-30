code = """import json
import re

with open(locals()['var_function-call-9226438263479244870'], 'r') as f:
    documents = json.load(f)

disaster_projects_2022_names = []

for doc in documents:
    text = doc['text']
    
    # Split the document by a pattern that indicates a new project starts.
    # This pattern looks for a capitalized line (potential project name) followed by '(cid:190) Updates:'
    # We use a non-greedy match for the project name itself to avoid over-matching.
    project_blocks = re.split(r'\n([A-Z][A-Za-z0-9 &\\-/,'.()]*?(?: Project| Improvements| Plan| Repairs| Study| System)?)\n\\s*\\(cid:190\\)\s*Updates:', text)

    # The split operation results in a list where:
    # - project_blocks[0] is typically text before the first project (or empty).
    # - project_blocks[1], project_blocks[3], ... are project names.
    # - project_blocks[2], project_blocks[4], ... are the details/updates for the preceding project name.
    
    # So, we iterate through the project names and their corresponding details.
    # We start from index 1 for project names and index 2 for details.
    for i in range(1, len(project_blocks), 2):
        project_name = project_blocks[i].strip()
        # Ensure there are details for this project name
        if (i + 1) < len(project_blocks):
            details_block = project_blocks[i+1].strip()
        else:
            details_block = ""

        is_disaster = False
        # Check for disaster-related keywords in both project name and details block
        if re.search(r'disaster|FEMA|recovery|fire|emergency|CalOES|CalJPIA', project_name + " " + details_block, re.IGNORECASE):
            is_disaster = True

        if is_disaster:
            # Now, check for '2022' within the 'Project Schedule:' part of the details block.
            # The date can be in various flexible formats like '2022-Spring', '2022-Fall', '2022-02', etc.
            # We look for 'Project Schedule:' followed by any characters, then '2022'.
            schedule_match = re.search(r'Project Schedule:.*?(2022[\\s\\-A-Za-z]*|Spring 2022|Fall 2022|Summer 2022|Winter 2022)', details_block, re.DOTALL)
            
            if schedule_match:
                # If a schedule match containing '2022' is found, add the project name.
                disaster_projects_2022_names.append(project_name)

# Filter out duplicates and known generic headings that are not actual project names.
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
            lower_project.startswith('malibu bluffs park') # Specific false positive observed in some documents
           ):
        final_disaster_projects_2022.append(project)

print("__RESULT__:")
print(json.dumps(final_disaster_projects_2022))"""

env_args = {'var_function-call-14874373830466001573': ['civic_docs'], 'var_function-call-6587384332537770908': [], 'var_function-call-9226438263479244870': 'file_storage/function-call-9226438263479244870.json', 'var_function-call-3865910938844144022': []}

exec(code, env_args)
