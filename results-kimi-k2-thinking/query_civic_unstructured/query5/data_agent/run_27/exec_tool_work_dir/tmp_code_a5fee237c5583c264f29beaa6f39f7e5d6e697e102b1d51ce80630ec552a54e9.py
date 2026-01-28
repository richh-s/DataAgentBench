code = """import json

# Load data
funding_data = json.load(open('file_storage/functions.query_db:5.json'))
civic_docs = json.load(open('file_storage/functions.query_db:6.json'))

# Build funding map
funding_map = {}
for r in funding_data:
    funding_map[r['Project_Name']] = int(r['Amount'])

# Find all disaster-related projects in funding data
all_disaster_projects = []
markers = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']

for name, amount in funding_map.items():
    is_disaster = False
    for marker in markers:
        if marker in name:
            is_disaster = True
            break
    if not is_disaster:
        if 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name:
            is_disaster = True
    
    if is_disaster:
        all_disaster_projects.append(name)

print('Found', len(all_disaster_projects), 'disaster projects in funding data')
print('Sample:', all_disaster_projects[:5])

# Now check which ones started in 2022 according to civic docs
projects_in_2022 = {}

doc_text_combined = '\n'.join([doc['text'] for doc in civic_docs])

for project in all_disaster_projects:
    # Check if project name appears in civic docs with 2022
    if project in doc_text_combined and '2022' in doc_text_combined:
        # Look for the project in context
        for doc in civic_docs:
            text = doc['text']
            if project in text:
                # Check if 2022 appears in the same document
                if '2022' in text:
                    projects_in_2022[project] = funding_map[project]
                    break

# Also look for any projects (in docs) that mention 2022 and disaster keywords
for doc in civic_docs:
    text = doc['text']
    if '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 5 and '2022' in line:
                # If it's a disaster project
                for marker in markers:
                    if marker in line:
                        # Find matching funding
                        for name, amount in funding_map.items():
                            if name in line or line in name:
                                projects_in_2022[name] = amount

# Consolidate results
final_projects = list(projects_in_2022.items())
total_funding = sum(amount for _, amount in final_projects)

result = dict(total_funding=total_funding, project_count=len(final_projects), projects=final_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}}

exec(code, env_args)
