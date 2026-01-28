code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:66'], 'r') as f:
    funding = json.load(f)
with open(locals()['var_functions.query_db:67'], 'r') as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    name = r.get('Project_Name', '')
    if name:
        fund_map[name] = fund_map.get(name, 0) + int(r.get('Amount', 0))

# Find disaster projects with 2022 dates from civic docs
disaster_projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)-1):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower():
            continue
        if 'Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]:
            proj = line
            is_disaster = False
            has_2022 = False
            for j in range(i+1, min(i+12, len(lines))):
                cl = lines[j].upper()
                # Check disaster indicators
                for ind in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']:
                    if ind in cl:
                        is_disaster = True
                # Check 2022 date indicators
                if '2022' in cl and ('DESIGN' in cl or 'CONSTRUCTION' in cl or 'BEGIN' in cl or 'COMPLETE' in cl):
                    has_2022 = True
            if is_disaster and has_2022:
                disaster_projects_2022.append(proj)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

# Calculate total funding
total_funding = 0
for proj in disaster_projects_2022:
    # Try exact match and common variations
    if proj in fund_map:
        total_funding += fund_map[proj]
        continue
    # Check for variations with disaster suffixes
    variations = [proj + suff for suff in [' (FEMA Project)', ' (FEMA/CalOES Project)', ' (CalOES Project)', ' (CalJPIA Project)']]
    for var in variations:
        if var in fund_map:
            total_funding += fund_map[var]
            break

result = {
    'total_funding': total_funding,
    'disaster_projects_count': len(disaster_projects_2022),
    'sample_projects': disaster_projects_2022[:5]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'total_funding_for_disaster_related_projects': 1410000, 'number_of_disaster_projects': 27, 'sample_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.execute_python:96': {'total_disaster_related_funding': 1410000, 'projects': 27}, 'var_functions.execute_python:100': {'total_funding_for_disaster_projects': 1410000, 'disaster_projects_count': 27}}

exec(code, env_args)
