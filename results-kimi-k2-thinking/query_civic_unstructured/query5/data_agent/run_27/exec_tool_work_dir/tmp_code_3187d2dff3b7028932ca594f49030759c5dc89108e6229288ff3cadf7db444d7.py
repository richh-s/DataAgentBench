code = """import json

# Load data
funding_data = json.load(open('file_storage/functions.query_db:5.json'))
civic_docs = json.load(open('file_storage/functions.query_db:6.json'))

# Build funding map
funding_map = {}
for r in funding_data:
    funding_map[r['Project_Name']] = int(r['Amount'])

# Find disaster projects from funding data that are related to 2022
disaster_2022_projects = {}

# Disaster project suffixes
suffixes = ['FEMA Project', 'CalOES Project', 'CalJPIA Project']

for project_name, amount in funding_map.items():
    # Check if project has a disaster suffix and mentions 2022
    has_suffix = False
    for suffix in suffixes:
        if suffix in project_name:
            has_suffix = True
            break
    
    if has_suffix and '2022' in project_name:
        disaster_2022_projects[project_name] = amount

# Also check for projects with FEMA/CalOES/CalJPIA and 2022
for project_name, amount in funding_map.items():
    if '2022' in project_name:
        if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
            disaster_2022_projects[project_name] = amount

# Now analyze civic documents for additional context
# Look for disaster projects mentioned with 2022 dates
doc_text = []
for doc in civic_docs:
    doc_text.append(doc['text'])

full_text = ' '.join(doc_text)

# For each disaster project in funding, check if mentioned with 2022
for project_name, amount in funding_map.items():
    # Check if it's a disaster project
    is_disaster = False
    for suffix in suffixes:
        if suffix in project_name:
            is_disaster = True
            break
    
    if not is_disaster:
        if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
            is_disaster = True
    
    if is_disaster:
        # Check if this project is mentioned with 2022 in the documents
        if project_name in full_text and '2022' in full_text:
            # Verify they're in the same document
            for doc in doc_text:
                if project_name in doc and '2022' in doc:
                    disaster_2022_projects[project_name] = amount

# Remove duplicates and prepare final list
final_list = list(disaster_2022_projects.items())
total = sum(amount for _, amount in final_list)

result = dict(total_funding=total, project_count=len(final_list), projects=final_list)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}}

exec(code, env_args)
