code = """import json

# Load funding data
with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
with open('file_storage/functions.query_db:6.json', 'r') as f:
    civic_docs = json.load(f)

# Create funding map
funding_map = {}
for record in funding_data:
    funding_map[record['Project_Name']] = int(record['Amount'])

# Identify disaster projects
funding_disaster_projects = set()
for project_name in funding_map.keys():
    if '(FEMA Project)' in project_name or '(CalOES Project)' in project_name or '(CalJPIA Project)' in project_name:
        funding_disaster_projects.add(project_name)
    elif 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
        funding_disaster_projects.add(project_name)

print('Disaster projects in funding:', len(funding_disaster_projects))

# Find which disaster projects started in 2022
disaster_2022_projects = {}

# Combine all civic text
all_text = ' '.join([doc['text'] for doc in civic_docs])

# For each disaster project, check if mentioned with 2022
for project_name in funding_disaster_projects:
    if project_name in all_text and '2022' in all_text:
        # More specific: check the project is actually mentioned in 2022 context
        for doc in civic_docs:
            doc_text = doc['text']
            if project_name in doc_text and '2022' in doc_text:
                disaster_2022_projects[project_name] = funding_map[project_name]
                break

# Also include projects with 2022 in the name
for project_name in funding_disaster_projects:
    if '2022' in project_name:
        disaster_2022_projects[project_name] = funding_map[project_name]

# Calculate total
total_amount = sum(disaster_2022_projects.values())
project_list = []
for project_name, amount in disaster_2022_projects.items():
    project_list.append([project_name, amount])

project_list.sort(key=lambda x: x[1], reverse=True)

result = {
    'total_funding': total_amount,
    'project_count': len(project_list),
    'projects': project_list
}

print('Total:', total_amount)
print('Projects found:', len(project_list))

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:46': {'total_funding': 1410000, 'project_count': 27, 'projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000], ['Outdoor Warningn Sirens - Design (FEMA Project)', 84000], ['Storm Drain Master Plan (FEMA Project)', 80000], ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 44000], ['Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 92000], ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 43000], ['Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 32000], ['Westward Beach Road Shoulder Repairs (CalOES Project)', 77000]]}, 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json', 'var_functions.execute_python:56': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:62': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.list_db:66': ['civic_docs']}

exec(code, env_args)
