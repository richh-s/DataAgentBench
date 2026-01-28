code = """import json

# Load data
funding_data = json.load(open('file_storage/functions.query_db:5.json', 'r'))
civic_docs = json.load(open('file_storage/functions.query_db:6.json', 'r'))

# Build funding map: project name -> amount
funding_map = {}
for record in funding_data:
    funding_map[record['Project_Name']] = int(record['Amount'])

# Identify disaster-related projects that started in 2022
# These have markers like (FEMA Project), (CalOES Project), etc.
disaster_markers = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']

# Projects to track
projects_2022 = set()

# 1. First, get projects with 2022 in their name and disaster markers
for project_name in funding_map.keys():
    if '2022' in project_name:
        for marker in disaster_markers:
            if marker in project_name:
                projects_2022.add(project_name)

# 2. Also check for disaster projects mentioned with 2022 in civic docs
for doc in civic_docs:
    text = doc['text']
    if '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 10 and len(line) < 150:
                # Check if this is a disaster project
                for marker in disaster_markers:
                    if marker in line:
                        # Check if 2022 appears nearby in the document
                        if '2022-' in text or '2022 ' in text:
                            projects_2022.add(line)
                        break

# 3. Also include any FEMA/CalOES/CalJPIA projects from funding data that mention 2022
for project_name in funding_map.keys():
    if '2022' in project_name:
        if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
            projects_2022.add(project_name)

# Calculate total funding
total_funding = 0
valid_projects = []

for project in projects_2022:
    if project in funding_map:
        amount = funding_map[project]
        total_funding += amount
        valid_projects.append((project, amount))

# Sort by amount for clarity
valid_projects.sort(key=lambda x: x[1], reverse=True)

result = dict(total_funding=total_funding, project_count=len(valid_projects), projects=valid_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}}

exec(code, env_args)
