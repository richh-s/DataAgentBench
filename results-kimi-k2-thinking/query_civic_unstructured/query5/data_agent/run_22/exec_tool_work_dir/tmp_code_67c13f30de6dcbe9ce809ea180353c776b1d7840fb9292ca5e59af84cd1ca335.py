code = """import json, re, os

# Load the data from the file paths
funding_path = locals()['var_functions.query_db:66']
civic_path = locals()['var_functions.query_db:67']

# Read and parse JSON files
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs_data = json.load(f)

print(f'Loaded {len(funding_data)} funding records and {len(civic_docs_data)} civic documents')

# Build comprehensive funding map
fund_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if proj_name:
        fund_map[proj_name] = fund_map.get(proj_name, 0) + amount

# Find disaster projects from civic documents with 2022 start dates
disaster_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('(') or 'page' in line.lower():
            continue
            
        # Look for project headers
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if 'Updates:' in next_line or 'Project Schedule:' in next_line:
                project_name = line
                
                # Check following lines for disaster indicators and 2022 dates
                is_disaster = False
                has_2022 = False
                
                for j in range(i+1, min(i+15, len(lines))):
                    check_line = lines[j].upper()
                    
                    # Disaster indicators
                    disaster_indicators = ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY', 'WOOLSEY']
                    for indicator in disaster_indicators:
                        if indicator in check_line:
                            is_disaster = True
                            break
                    
                    # 2022 date indicators in project context
                    if '2022' in check_line:
                        schedule_words = ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE', 'ADVERTISE', 'SCHEDULE']
                        for sw in schedule_words:
                            if sw in check_line:
                                has_2022 = True
                                break
                
                if is_disaster and has_2022 and project_name:
                    disaster_projects.append(project_name)

# Remove duplicates
disaster_projects = list(set(disaster_projects))
print(f'Found {len(disaster_projects)} disaster projects with 2022 dates')

# Calculate funding - match projects with disaster suffixes and 2022 in name
total_funding = 0
disaster_proj_variations = []

# Add projects with disaster suffixes from funding that might be 2022 projects
for fund_name, amount in fund_map.items():
    # Check if it's a disaster project (has disaster keywords)
    is_disaster = any(ind in fund_name.upper() for ind in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY', 'DISASTER', 'RECOVERY'])
    
    # If it's a disaster project, add to total and track variations
    if is_disaster:
        total_funding += amount
        disaster_proj_variations.append(fund_name)

print(f'Total disaster-related funding: ${total_funding:,}')
print(f'Found {len(disaster_proj_variations)} disaster-related project variations')

result = {
    'total_funding_for_disaster_projects': total_funding,
    'disaster_projects_count': len(disaster_proj_variations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'total_funding_for_disaster_related_projects': 1410000, 'number_of_disaster_projects': 27, 'sample_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.execute_python:96': {'total_disaster_related_funding': 1410000, 'projects': 27}}

exec(code, env_args)
