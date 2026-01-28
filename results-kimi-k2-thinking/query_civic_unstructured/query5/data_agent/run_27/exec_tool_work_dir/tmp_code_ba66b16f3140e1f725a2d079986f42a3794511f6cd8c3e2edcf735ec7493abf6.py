code = """import json
import re

# Load all funding data
with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

# Build funding map
funding_map = {}
disaster_funding_projects = set()  # Track which ones are disaster-related

# Disaster markers to look for
disaster_markers = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']

for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount
    
    # Check if this is a disaster project
    is_disaster = False
    for marker in disaster_markers:
        if marker in project_name:
            is_disaster = True
            break
    
    if not is_disaster:
        if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
            is_disaster = True
    
    if is_disaster:
        disaster_funding_projects.add(project_name)

print('Total funding records:', len(funding_map))
print('Disaster-related funding projects:', len(disaster_funding_projects))
print('Sample disaster projects:', list(disaster_funding_projects)[:5])

# Now load civic documents and look for 2022 start dates
with open('file_storage/functions.query_db:6.json', 'r') as f:
    civic_docs = json.load(f)

print('Civic documents to search:', len(civic_docs))

# We'll collect projects that have 2022 start indicators
disaster_2022_funding = {}

# Method: Look for 2022 year references in civic docs that are NEAR disaster project mentions
for doc in civic_docs:
    text = doc['text']
    
    # Find all 2022 date mentions
    if '2022' not in text:
        continue
    
    # For each disaster project, check if it's mentioned in this doc near 2022
    for project_name in disaster_funding_projects:
        if project_name in text:
            # Extract context around the project mention
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if project_name in line:
                    # Check this line and nearby for 2022 date indicators
                    context_start = max(0, i-5)
                    context_end = min(len(lines), i+10)
                    context = ' '.join(lines[context_start:context_end])
                    
                    # Check for year 2022 in the context
                    if '2022' in context:
                        disaster_2022_funding[project_name] = funding_map[project_name]
                        break  # No need to check more lines for this project

# Also check for projects that explicitly have year 2022 in their name
for project_name in disaster_funding_projects:
    if '2022' in project_name:
        disaster_2022_funding[project_name] = funding_map[project_name]

# Calculate final total
total_funding = sum(disaster_2022_funding.values())
project_list = [[name, amount] for name, amount in disaster_2022_funding.items()]
project_list.sort(key=lambda x: x[1], reverse=True)

print('\nFinal results:')
print('Total funding:', total_funding)
print('Number of projects:', len(project_list))
print('Top 10 projects:')
for p in project_list[:10]:
    print('  ', p[0], ': $', p[1])

# Save result
result = {
    'total_funding': total_funding,
    'project_count': len(project_list),
    'projects': project_list
}

result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:46': {'total_funding': 1410000, 'project_count': 27, 'projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000], ['Outdoor Warningn Sirens - Design (FEMA Project)', 84000], ['Storm Drain Master Plan (FEMA Project)', 80000], ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 44000], ['Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 92000], ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 43000], ['Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 32000], ['Westward Beach Road Shoulder Repairs (CalOES Project)', 77000]]}, 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json', 'var_functions.execute_python:56': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:62': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.list_db:66': ['civic_docs']}

exec(code, env_args)
