code = """import json
import re

file_path = locals()['var_function-call-6790680028144073528']
with open(file_path, 'r') as f:
    docs = json.load(f)

extracted_projects = []

for doc in docs:
    text = doc['text']

    # Normalize newlines. The input from MongoDB likely has escaped newlines like '\\n'
    # When loaded by json.load, these become actual '\n' characters in the string.
    # So we match on actual '\n' in regex.
    
    # We are looking for project blocks that start with a Project_Name and contain project details.
    # A project name is typically a line (or multiple lines) followed by bullet points (cid:190).
    # The project details will contain the type and schedule.
    
    # Regex to find project blocks. A block starts with a project name and its description/schedule.
    # This pattern captures the Project_Name and then the details block associated with it.
    # It assumes project details are always introduced by a bullet point followed by "Updates:", "Project Schedule:", etc.
    # The non-greedy `[\s\S]*?` ensures it stops before the next similar pattern or section header.
    project_block_pattern = re.compile(
        r'(?P<project_name>[A-Z][A-Za-z0-9\s,&./()-]+?)\n\n'  # Project Name (can be multiple words, caps, numbers, etc.)
        r'(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:|\(cid:190\) Project Schedule:|\(cid:190\) Project Description:)'  # Start of project details
        r'(?P<project_details>[\s\S]*?)'
        r'(?=(?:[A-Z][A-Za-z0-9\s,&./()-]+?\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:|\(cid:190\) Project Schedule:))|\Z|Capital Improvement Projects|Disaster Recovery Projects)'
        , re.DOTALL
    )

    for match in project_block_pattern.finditer(text):
        project_name = match.group('project_name').strip()
        project_details_text = match.group('project_details').strip()

        project_type = 'capital' # Default type
        # Check for disaster keywords in project details or name
        if ('Disaster Recovery Projects' in project_details_text or
            'FEMA' in project_details_text or
            'CalOES' in project_details_text or
            '(FEMA Project)' in project_name or
            '(CalOES Project)' in project_name):
            project_type = 'disaster'

        start_date = 'Unknown'
        # Search for start dates within the project details block
        start_date_match = re.search(
            r'(?:Begin Construction|Advertise|Complete Design|Final Design|Project Schedule):\s*((?:2022|2023|Spring|Summer|Fall|Winter)[a-zA-Z0-9-]*)',
            project_details_text, re.IGNORECASE
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
    # Make sure 'st' is a string before checking for '2022'
    if project['type'] == 'disaster' and isinstance(project['st'], str) and '2022' in project['st']:
        disaster_projects_2022_names.append(project['Project_Name'])

unique_disaster_projects_2022_names = list(set(disaster_projects_2022_names))

print('__RESULT__:')
print(json.dumps(unique_disaster_projects_2022_names))"""

env_args = {'var_function-call-6790680028144073528': 'file_storage/function-call-6790680028144073528.json', 'var_function-call-12440770224826216985': []}

exec(code, env_args)
