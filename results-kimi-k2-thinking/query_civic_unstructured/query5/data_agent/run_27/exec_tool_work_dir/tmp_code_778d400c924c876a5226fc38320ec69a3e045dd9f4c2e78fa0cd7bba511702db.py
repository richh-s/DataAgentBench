code = """import json

# Load all data
funding_data = json.load(open('file_storage/functions.query_db:5.json'))
all_civic_docs = json.load(open('file_storage/functions.query_db:6.json'))

# Build funding map
funding_map = {}
for record in funding_data:
    funding_map[record['Project_Name']] = int(record['Amount'])

# Disaster project markers based on naming conventions in the data
disaster_markers = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']

# Strategy: Find all disaster projects and check if they have 2022 context
disaster_projects_2022 = {}

# Method 1: Project names that contain both 2022 AND disaster markers
for project_name, amount in funding_map.items():
    if '2022' in project_name:
        for marker in disaster_markers:
            if marker in project_name:
                disaster_projects_2022[project_name] = amount

# Method 2: Disaster projects that reference 2022 in civic documents
# First, identify all disaster projects from funding data
all_disaster_projects = {}
for project_name, amount in funding_map.items():
    is_disaster = False
    for marker in disaster_markers:
        if marker in project_name:
            is_disaster = True
            break
    if not is_disaster:
        if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
            is_disaster = True
    
    if is_disaster:
        all_disaster_projects[project_name] = amount

# Check which disaster projects are mentioned with 2022 in civic docs
all_doc_text = '\n'.join([doc['text'] for doc in all_civic_docs])

for project_name, amount in all_disaster_projects.items():
    if project_name in all_doc_text and '2022' in all_doc_text:
        # Verify they're in the same region of text
        for doc in all_civic_docs:
            text = doc['text']
            if project_name in text and '2022' in text:
                disaster_projects_2022[project_name] = amount
                break

# Remove any projects with zero funding
final_projects = {k: v for k, v in disaster_projects_2022.items() if v > 0}

# Calculate total
total_funding = sum(final_projects.values())
project_list = [[name, amount] for name, amount in final_projects.items()]
project_list.sort(key=lambda x: x[1], reverse=True)

# Prepare final result
result = {
    "total_funding": total_funding,
    "project_count": len(project_list),
    "projects": project_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:46': {'total_funding': 1410000, 'project_count': 27, 'projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000], ['Outdoor Warningn Sirens - Design (FEMA Project)', 84000], ['Storm Drain Master Plan (FEMA Project)', 80000], ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 44000], ['Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 92000], ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 43000], ['Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 32000], ['Westward Beach Road Shoulder Repairs (CalOES Project)', 77000]]}, 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json'}

exec(code, env_args)
