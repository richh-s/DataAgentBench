code = """import json

# Load funding data
funding_data = json.load(open('file_storage/functions.query_db:5.json'))

# Build funding map
funding_map = {}
for record in funding_data:
    funding_map[record['Project_Name']] = int(record['Amount'])

# Use the civic documents filtered for 2022 and disaster terms
# This captures projects mentioned in 2022 context
import os
if os.path.exists('file_storage/functions.query_db:49.json'):
    civic_2022_disaster = json.load(open('file_storage/functions.query_db:49.json'))
else:
    civic_2022_disaster = []

print('Documents with 2022 and disaster terms:', len(civic_2022_disaster))

# Extract all project names mentioned in these documents
document_projects = set()

for doc in civic_2022_disaster:
    text = doc['text']
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        # Look for project name patterns (lines that are likely project names)
        if len(line) > 5 and len(line) < 150:
            # Check if line starts with capital letter and doesn't start with common non-project words
            if line[0].isupper() and not line.startswith('Page') and not line.startswith('Item'):
                document_projects.add(line)

print('Potential project names found in documents:', len(document_projects))

# Find disaster projects with 2022 in their name (most direct evidence)
direct_2022_disaster = {}
for project_name, amount in funding_map.items():
    # Check if it's a disaster project
    is_disaster = False
    for marker in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']:
        if marker in project_name:
            is_disaster = True
            break
    
    if not is_disaster and ('FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name):
        is_disaster = True
    
    # Check if it has 2022 in the name
    if is_disaster and '2022' in project_name:
        direct_2022_disaster[project_name] = amount

print('Direct 2022 disaster projects:', len(direct_2022_disaster))

# Also find projects that mention 2022 AND are disaster projects in the documents
doc_based_projects = {}

for project_name, amount in funding_map.items():
    # Check if it's a disaster project
    is_disaster = False
    for marker in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']:
        if marker in project_name:
            is_disaster = True
            break
    
    if not is_disaster and ('FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name):
        is_disaster = True
    
    if is_disaster:
        # Check if this project is mentioned in the 2022 disaster documents
        for doc in civic_2022_disaster:
            if project_name in doc['text'] or any(project_name in line for line in document_projects if project_name in line):
                doc_based_projects[project_name] = amount
                break

print('Document-based disaster projects:', len(doc_based_projects))

# Add projects that start with "2022 " in their name (very likely started in 2022)
starts_with_2022 = {}
for project_name, amount in funding_map.items():
    if project_name.startswith('2022 '):
        # Check if it's disaster related
        is_disaster = False
        text_lower = project_name.lower()
        if 'fema' in text_lower or 'caloes' in text_lower or 'caljpia' in text_lower or 'disaster' in text_lower:
            is_disaster = True
        
        # Also check civic documents context
        if not is_disaster:
            for doc in civic_2022_disaster:
                if project_name in doc['text']:
                    # Check surrounding context
                    text = doc['text']
                    if 'disaster' in text.lower() or 'fema' in text.lower():
                        is_disaster = True
                        break
        
        if is_disaster:
            starts_with_2022[project_name] = amount

print('Projects starting with 2022:', len(starts_with_2022))

# Combine all approaches
all_2022_disaster = {}

# Add direct matches
for project, amount in direct_2022_disaster.items():
    all_2022_disaster[project] = amount

# Add document-based
for project, amount in doc_based_projects.items():
    all_2022_discaster[project] = amount  # Note: fixed typo in previous runs

# Add 2022-starters
for project, amount in starts_with_2022.items():
    all_2022_disaster[project] = amount

# Fix typo from previous variable name
all_2022_disaster = {}
for project, amount in direct_2022_disaster.items():
    all_2022_disaster[project] = amount
for project, amount in doc_based_projects.items():
    all_2022_disaster[project] = amount
for project, amount in starts_with_2022.items():
    all_2022_disaster[project] = amount

# Calculate total
total_funding = sum(all_2022_disaster.values())
project_list = list(all_2022_disaster.items())
project_list.sort(key=lambda x: x[1], reverse=True)

result = dict(
    total_funding=total_funding,
    project_count=len(project_list),
    projects=project_list
)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:46': {'total_funding': 1410000, 'project_count': 27, 'projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000], ['Outdoor Warningn Sirens - Design (FEMA Project)', 84000], ['Storm Drain Master Plan (FEMA Project)', 80000], ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 44000], ['Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 92000], ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 43000], ['Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 32000], ['Westward Beach Road Shoulder Repairs (CalOES Project)', 77000]]}, 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json'}

exec(code, env_args)
