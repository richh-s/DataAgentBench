code = """import json
import re

with open(locals()['var_function-call-13556780500414071833'], 'r') as f:
    civic_docs_data = json.load(f)

projects_info = []

for doc in civic_docs_data:
    text = doc['text']

    # Split the document text into logical blocks based on major project headings.
    project_blocks = re.split("\\n(?=[A-Z][A-Za-z ]+(?:Project|Projects)\\n\\n)", text)

    for block in project_blocks:
        project_name = None
        # Extract the project name from the current block.
        project_name_match = re.search("^([A-Z][A-Za-z0-9\\s&/-]+(?:Project|Projects)?)(?:\\s*\\(cid:\\d+\\))?\\s*$", block, re.MULTILINE)
        
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            # Filter out general section headers
            if "Capital Improvement Projects" in project_name or \
               "Disaster Recovery Projects" in project_name or \
               "Public Works Commission" in project_name or \
               "Agenda Report" in project_name or \
               "Capital Improvement Program" in project_name or \
               "Status Report" in project_name or \
               "Updates" in project_name:
                project_name = None

        if project_name:
            # Determine project type
            project_type = 'capital'
            if 'Disaster Recovery Projects' in text or 'FEMA' in block or 'CalOES' in block or 'Woolsey Fire' in block:
                project_type = 'disaster'

            # Extract the start time/date
            start_time_match = re.search("Begin (?:Construction|Work|Project|Operation):\\s*([A-Za-z0-9-]+(?:\\s[A-Za-z0-9-]+)*)", block)
            start_time = start_time_match.group(1).strip() if start_time_match else None

            # Filter for disaster projects that started in 2022
            if project_type == 'disaster' and start_time and '2022' in start_time:
                projects_info.append({'Project_Name': project_name, 'st': start_time, 'type': project_type})

# Remove potential duplicate projects
unique_projects = {}
for p in projects_info:
    if p['Project_Name'] not in unique_projects:
        unique_projects[p['Project_Name']] = p

final_disaster_projects_2022 = list(unique_projects.values())

print('__RESULT__:')
print(json.dumps(final_disaster_projects_2022))"""

env_args = {'var_function-call-13556780500414071833': 'file_storage/function-call-13556780500414071833.json'}

exec(code, env_args)
