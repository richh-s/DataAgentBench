code = """import json
import re

# Load funding data
f_path = locals()['var_functions.query_db:66']
c_path = locals()['var_functions.query_db:67']

with open(f_path, 'r') as f:
    funding = json.load(f)
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding map and identify disaster-related projects
fund_map = {}
disaster_projects = {}
for r in funding:
    name = r.get('Project_Name', '')
    amount = int(r.get('Amount', 0))
    if name:
        fund_map[name] = fund_map.get(name, 0) + amount
        # Check if this is a disaster-related project
        if any(ind in name.upper() for ind in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY', 'DISASTER', 'RECOVERY']):
            disaster_projects[name] = amount

# Find 2022 disaster project references in civic documents
disaster_2022_references = set()
for doc in civic_docs:
    text = doc.get('text', '')
    # Check if document contains both disaster keywords and 2022 dates
    has_disaster = any(ind in text.upper() for ind in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER'])
    has_2022 = '2022' in text and ('DESIGN' in text.upper() or 'CONSTRUCTION' in text.upper() or 'BEGIN' in text.upper())
    
    if has_disaster and has_2022:
        # Look for project names that match our disaster projects
        for disaster_proj in disaster_projects.keys():
            # Check if base project name (without suffixes) appears in text
            base_name = disaster_proj.split(' (')[0]
            if base_name in text:
                disaster_2022_references.add(disaster_proj)

# Calculate total funding for disaster-related projects that have 2022 references
total_funding = 0
for proj in disaster_2022_references:
    total_funding += disaster_projects.get(proj, 0)

# Add any 2022 disaster projects from funding data directly
for proj_name, amount in fund_map.items():
    if '2022' in proj_name and any(ind in proj_name.upper() for ind in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY', 'DISASTER']):
        if proj_name not in disaster_2022_references:
            total_funding += amount

result = {
    'total_funding_for_disaster_projects_started_in_2022': total_funding,
    'disaster_projects_matched': len(disaster_2022_references),
    'total_disaster_projects_in_dataset': len(disaster_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'total_funding_for_disaster_related_projects': 1410000, 'number_of_disaster_projects': 27, 'sample_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.execute_python:96': {'total_disaster_related_funding': 1410000, 'projects': 27}, 'var_functions.execute_python:100': {'total_funding_for_disaster_projects': 1410000, 'disaster_projects_count': 27}, 'var_functions.execute_python:110': {'total_funding_for_disaster_projects_2022': 0, 'disaster_projects_found': 0, 'projects_matched': 0}}

exec(code, env_args)
