code = """import json

# Load data
funding_data = json.load(open('file_storage/functions.query_db:5.json'))
civic_docs = json.load(open('file_storage/functions.query_db:6.json'))

# Build funding map
funding_map = {}
for r in funding_data:
    funding_map[r['Project_Name']] = int(r['Amount'])

# Find disaster projects with 2022 indicators
results = {}

# Direct: project names containing both "2022" and disaster markers
for name, amount in funding_map.items():
    if '2022' not in name:
        continue
    
    # Disaster markers
    if '(FEMA Project)' in name or '(CalOES Project)' in name or '(CalJPIA Project)' in name:
        results[name] = amount
    elif 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name:
        results[name] = amount

# Now check civic docs for 2022 disaster context that might not have 2022 in project name
all_text = '\n'.join([doc['text'] for doc in civic_docs])

# Look for disaster projects from funding that appear in 2022 context
for name, amount in funding_map.items():
    # Must be disaster project
    is_disaster = False
    for marker in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']:
        if marker in name:
            is_disaster = True
            break
    
    if not is_disaster and ('FEMA' in name or 'CalOES' in name or 'CalJPIA' in name):
        is_disaster = True
    
    # Check if mentioned in docs with 2022
    if is_disaster and name in all_text and '2022' in all_text:
        results[name] = amount

# Calculate total
total = sum(results.values())
projects = sorted([[k, v] for k, v in results.items()], key=lambda x: x[1], reverse=True)

output = {
    'total_funding': total,
    'project_count': len(projects),
    'projects': projects
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:46': {'total_funding': 1410000, 'project_count': 27, 'projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000], ['Outdoor Warningn Sirens - Design (FEMA Project)', 84000], ['Storm Drain Master Plan (FEMA Project)', 80000], ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 44000], ['Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 92000], ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 43000], ['Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 32000], ['Westward Beach Road Shoulder Repairs (CalOES Project)', 77000]]}, 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json', 'var_functions.execute_python:56': {'total_funding': 0, 'project_count': 0, 'projects': []}}

exec(code, env_args)
