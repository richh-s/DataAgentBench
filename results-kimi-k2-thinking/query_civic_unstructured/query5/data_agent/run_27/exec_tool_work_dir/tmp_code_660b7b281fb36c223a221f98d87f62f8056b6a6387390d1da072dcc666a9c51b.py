code = """import json

with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:6.json', 'r') as f:
    civic_docs = json.load(f)

# Build funding map
funding_map = {}
for record in funding_data:
    funding_map[record['Project_Name']] = int(record['Amount'])

# Look for disaster projects that started in 2022
# Disaster projects often have these markers in their names
disaster_markers = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']

# Collect all disaster-related projects from funding data that mention 2022 or are FEMA/CalOES/CalJPIA
disaster_funding = {}
for project_name, amount in funding_map.items():
    # Check if it's a disaster project
    is_disaster = False
    for marker in disaster_markers:
        if marker in project_name:
            is_disaster = True
            break
    
    # Also check for FEMA/CalOES/CalJPIA anywhere in the name
    if not is_disaster:
        if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name or 'fema' in project_name.lower():
            is_disaster = True
    
    if is_disaster:
        disaster_funding[project_name] = amount

# Now check which ones started in 2022
# This can be: 1) project name contains 2022, or 2) mentioned in civic docs with 2022
projects_with_2022 = {}

# Direct: project names containing 2022
for project_name, amount in disaster_funding.items():
    if '2022' in project_name:
        projects_with_2022[project_name] = amount

# For projects without 2022 in name, check civic docs for mentions
# Look for projects mentioned in civic docs with 2022 context
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 10:
            continue
        
        # Check if this line mentions a disaster project
        for project_name, amount in disaster_funding.items():
            if project_name in line:
                # Check surrounding context for 2022
                if '2022' in text[max(0, text.index(line)-200):text.index(line)+200]:
                    if '2022-' in text or '2022 ' in text:
                        projects_with_2022[project_name] = amount

# Also look for any disaster projects explicitly started in 2022 in the civic docs
for doc in civic_docs:
    text = doc['text']
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for lines that might be project names
            if len(line) > 10 and len(line) < 150:
                # Check if it's likely a disaster project
                for marker in disaster_markers:
                    if marker in line:
                        # Check if 2022 appears in this project section
                        section = '\n'.join(lines[max(0,i-2):i+10])
                        if '2022' in section:
                            projects_with_2022[line] = funding_map.get(line, 0)

# Remove zero amounts
final_projects = {k:v for k,v in projects_with_2022.items() if v > 0}

# Calculate total total_funding = sum(final_projects.values())

total_funding = sum(final_projects.values())

result = dict(total_funding=total_funding, project_count=len(final_projects), projects=list(final_projects.items()))
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}}

exec(code, env_args)
