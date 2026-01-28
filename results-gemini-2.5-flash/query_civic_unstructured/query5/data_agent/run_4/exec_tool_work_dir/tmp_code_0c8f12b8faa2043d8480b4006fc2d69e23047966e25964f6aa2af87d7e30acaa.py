code = """import json
import re

file_path = locals()['var_function-call-6790680028144073528']
with open(file_path, 'r') as f:
    docs = json.load(f)

extracted_projects = []

for doc in docs:
    text = doc['text']

    # Regex to find project blocks.
    # A project block usually starts with a capitalized Project Name
    # followed by a newline, then a bullet point (cid:190) and a descriptor.
    # It ends before the next similar project structure or a major section header.

    project_block_pattern = re.compile(
        r'(?P<project_name>[A-Z][A-Za-z0-9\s,&./()-]+?)\n\n'  # Project Name
        r'(?P<details_block>'
        r'(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:|\(cid:190\) Project Schedule:)'
        r'[\s\S]*?'
        r'(?=(?:[A-Z][A-Za-z0-9\s,&./()-]+?\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:|\(cid:190\) Project Schedule:))|\Z|Capital Improvement Projects|Disaster Recovery Projects)'
        r')',
        re.DOTALL
    )

    for match in project_block_pattern.finditer(text):
        project_name = match.group('project_name').strip()
        details_block = match.group('details_block').strip()

        project_type = 'capital'  # Default type
        # Check for disaster indicators within the project details block or name
        if ('Disaster Recovery Projects' in details_block or
            'FEMA' in details_block or
            'CalOES' in details_block or
            '(FEMA Project)' in project_name or
            '(CalOES Project)' in project_name):
            project_type = 'disaster'

        start_date = 'Unknown'
        # Search for start dates within the details block
        start_date_match = re.search(
            r'(?:Begin Construction|Advertise|Complete Design|Final Design|Project Schedule|Estimated Schedule):[\s]*((?:2022|2023|Spring|Summer|Fall|Winter)[a-zA-Z0-9-]*|delayed)',
            details_block, re.IGNORECASE
        )
        if start_date_match:
            start_date = start_date_match.group(1)

        extracted_projects.append({
            'Project_Name': project_name,
            'type': project_type,
            'st': start_date
        })

# Filter for disaster projects that started in 2022
disaster_projects_2022_names = []
for project in extracted_projects:
    if project['type'] == 'disaster' and isinstance(project['st'], str) and '2022' in project['st'] and project['st'] != 'delayed':
        disaster_projects_2022_names.append(project['Project_Name'])

unique_disaster_projects_2022_names = list(set(disaster_projects_2022_names))

print('__RESULT__:')
print(json.dumps(unique_disaster_projects_2022_names))"""

env_args = {'var_function-call-6790680028144073528': 'file_storage/function-call-6790680028144073528.json', 'var_function-call-12440770224826216985': []}

exec(code, env_args)
