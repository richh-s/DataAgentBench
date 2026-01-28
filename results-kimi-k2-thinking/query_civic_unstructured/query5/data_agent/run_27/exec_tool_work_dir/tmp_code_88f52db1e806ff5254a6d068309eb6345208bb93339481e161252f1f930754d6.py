code = """import json

# Load funding and civic documents
funding_data = json.load(open('file_storage/functions.query_db:5.json'))
civic_docs = json.load(open('file_storage/functions.query_db:6.json'))

# Create funding lookup table
funding_lookup = {}
for record in funding_data:
    funding_lookup[record['Project_Name']] = int(record['Amount'])

# Find disaster-related projects that started in 2022
disaster_projects_2022_funding = {}

# Check each funding record
for project_name, amount in funding_lookup.items():
    # Must be a disaster project
    is_disaster = False
    if '(FEMA Project)' in project_name:
        is_disaster = True
    elif '(CalOES Project)' in project_name:
        is_disaster = True
    elif '(CalJPIA Project)' in project_name:
        is_disaster = True
    elif 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
        is_disaster = True
    
    # Must have 2022 indicator
    has_2022 = False
    if '2022' in project_name:
        has_2022 = True
    
    # Get total if both conditions met
    if is_disaster and has_2022:
        disaster_projects_2022_funding[project_name] = amount

# Calculate total funding
total_funding = sum(disaster_projects_2022_funding.values())

# Create sorted list of projects
project_list = []
for name, amount in disaster_projects_2022_funding.items():
    project_list.append([name, amount])

project_list.sort(key=lambda x: x[1], reverse=True)

result = {
    'total_funding': total_funding,
    'project_count': len(project_list),
    'projects': project_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:46': {'total_funding': 1410000, 'project_count': 27, 'projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000], ['Outdoor Warningn Sirens - Design (FEMA Project)', 84000], ['Storm Drain Master Plan (FEMA Project)', 80000], ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 44000], ['Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 92000], ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 43000], ['Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 32000], ['Westward Beach Road Shoulder Repairs (CalOES Project)', 77000]]}, 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json', 'var_functions.execute_python:56': {'total_funding': 0, 'project_count': 0, 'projects': []}}

exec(code, env_args)
