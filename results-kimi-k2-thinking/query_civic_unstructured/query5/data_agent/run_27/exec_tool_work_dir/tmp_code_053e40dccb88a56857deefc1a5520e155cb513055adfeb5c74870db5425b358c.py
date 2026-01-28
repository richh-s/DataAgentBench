code = """import json

# Load funding data
funding_data = json.load(open('file_storage/functions.query_db:5.json'))

# Load civic docs data (all docs and filtered 2022 disaster docs)
civic_all = json.load(open('file_storage/functions.query_db:6.json'))

civic_2022_disaster_file = 'file_storage/functions.query_db:49.json' 
try:
    civic_2022_disaster = json.load(open(civic_2022_disaster_file))
except:
    civic_2022_disaster = []

# Build funding map
funding_map = {}
for record in funding_data:
    funding_map[record['Project_Name']] = int(record['Amount'])

# Disaster project markers
markers = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']

# Strategy 1: Projects with 2022 in name AND disaster markers
strategy1 = {}
for name, amount in funding_map.items():
    if '2022' in name:
        for marker in markers:
            if marker in name:
                strategy1[name] = amount
                break

# Strategy 2: Disaster projects from funding data
# These are projects with FEMA/CalOES/CalJPIA markers (even without 2022 in name)
disaster_projects = {}
for name, amount in funding_map.items():
    for marker in markers:
        if marker in name:
            disaster_projects[name] = amount
            break

# Strategy 3: Check if disaster projects are mentioned with 2022 in civic docs
strategy3 = {}
all_doc_text = ' '.join([doc['text'] for doc in civic_all])

for project_name, amount in disaster_projects.items():
    if project_name in all_doc_text and '2022' in all_doc_text:
        strategy3[project_name] = amount

# Strategy 4: Projects that start with 2022 and are disaster-related in description
for name, amount in funding_map.items():
    if name.startswith('2022 '):
        # Check if mentioned in civic docs with disaster context
        for doc in civic_2022_disaster:
            if name in doc['text']:
                strategy3[name] = amount
                break

# Combine all strategies, removing duplicates
all_projects = {}

# Add strategy 1 (most reliable: 2022 in name + disaster marker)
for name, amount in strategy1.items():
    all_projects[name] = amount

# Add strategy 3 (disaster projects mentioned with 2022 context)
for name, amount in strategy3.items():
    if name not in all_projects:
        all_projects[name] = amount

# Calculate total
total_funding = sum(all_projects.values())
project_list = sorted([(name, amt) for name, amt in all_projects.items()], key=lambda x: x[1], reverse=True)

print('Total funding for disaster projects started in 2022: $', total_funding)
print('Number of projects:', len(project_list))
print('\nTop projects:')
for name, amount in project_list[:10]:
    print('  ', name, ': $', amount)

result = dict(total_funding=total_funding, project_count=len(project_list), projects=project_list)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:46': {'total_funding': 1410000, 'project_count': 27, 'projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000], ['Outdoor Warningn Sirens - Design (FEMA Project)', 84000], ['Storm Drain Master Plan (FEMA Project)', 80000], ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 44000], ['Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 92000], ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 43000], ['Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 32000], ['Westward Beach Road Shoulder Repairs (CalOES Project)', 77000]]}, 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json'}

exec(code, env_args)
