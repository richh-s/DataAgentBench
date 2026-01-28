code = """import json
import re

# Load all data
with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:6.json', 'r') as f:
    civic_docs = json.load(f)

# Build funding map for fast lookup
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Extract disaster-related projects that started in 2022 from civic documents
disaster_projects_2022 = set()  # Set of project names

# Disaster indicators
disaster_markers = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'Disaster', 'fire', 'Fire', 'emergency warning']
funding_disaster_markers = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']

print('Processing', len(civic_docs), 'civic documents...')

for doc in civic_docs:
    text = doc['text']
    
    # Find project sections
    # Projects often appear with bullet points or specific formatting
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project names (typically start with capital letter, reasonable length)
        if 10 <= len(line) <= 200 and line[0].isupper():
            # Skip lines that are clearly not project names
            if any(skip in line for skip in ['Page', 'Item', 'Agenda', 'Public Works', 'Commission', 'Meeting']):
                continue
                
            # Check if this is a disaster project
            is_disaster = False
            
            # Check for explicit markers in the line
            for marker in disaster_markers:
                if marker in line:
                    is_disaster = True
                    break
            
            # Check if this line matches any disaster project from funding
            if not is_disaster:
                for funding_project in funding_map.keys():
                    # If the funding project (with disaster marker) is mentioned here
                    for marker in funding_disaster_markers:
                        if marker in funding_project and (funding_project in line or line in funding_project):
                            is_disaster = True
                            break
                    if is_disaster:
                        break
            
            # Check surrounding context for disaster indicators
            if not is_disaster:
                # Look at previous 3 and next 5 lines
                context_start = max(0, i-3)
                context_end = min(len(lines), i+6)
                context_lines = lines[context_start:context_end]
                context_text = ' '.join(context_lines).lower()
                
                # Check for disaster keywords in context
                for marker in ['fema', 'caloes', 'caljpia', 'disaster', 'fire']:
                    if marker in context_text:
                        is_disaster = True
                        break
            
            # If this is a disaster project, check for 2022 start date
            if is_disaster:
                # Check if 2022 appears in project name
                if '2022' in line:
                    disaster_projects_2022.add(line)
                else:
                    # Check context for 2022 mentions that indicate start date
                    context_start = max(0, i-2)
                    context_end = min(len(lines), i+15)
                    context_lines = lines[context_start:context_end]
                    context_text = ' '.join(context_lines)
                    
                    # Look for date patterns with 2022
                    date_patterns = [
                        '2022-', '2022 Spring', '2022 Summer', '2022 Fall', '2022 Winter',
                        '2022 January', '2022 February', '2022 March', '2022 April', '2022 May',
                        '2022 June', '2022 July', '2022 August', '2022 September', '2022 October',
                        '2022 November', '2022 December', 'Spring 2022', 'Summer 2022', 'Fall 2022',
                        'September 2022', 'October 2022', 'November 2022', 'December 2022'
                    ]
                    
                    for pattern in date_patterns:
                        if pattern in context_text:
                            disaster_projects_2022.add(line)
                            break

# Now match extracted project names with funding data
matched_projects = {}
unmatched_projects = set()

for project_name in disaster_projects_2022:
    if project_name in funding_map:
        matched_projects[project_name] = funding_map[project_name]
    else:
        # Try to find partial matches
        for funding_project, amount in funding_map.items():
            # Check if one contains the other
            if (funding_project in project_name or project_name in funding_project) and len(project_name) > 10:
                matched_projects[funding_project] = amount
                break
        else:
            unmatched_projects.add(project_name)

# Also include projects from funding data that explicitly have 2022 AND disaster markers
for funding_project, amount in funding_map.items():
    # Check if project has disaster markers
    is_disaster = False
    for marker in funding_disaster_markers:
        if marker in funding_project:
            is_disaster = True
            break
    
    if not is_disaster:
        if 'FEMA' in funding_project or 'CalOES' in funding_project or 'CalJPIA' in funding_project:
            is_disaster = True
    
    # If disaster project has 2022 in name, include it
    if is_disaster and '2022' in funding_project:
        matched_projects[funding_project] = amount

# Remove duplicates and calculate total
total_funding = sum(matched_projects.values())
project_list = sorted([(name, amount) for name, amount in matched_projects.items()], 
                     key=lambda x: x[1], reverse=True)

result = {
    'total_funding': total_funding,
    'project_count': len(project_list),
    'projects': project_list,
    'unmatched_count': len(unmatched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:46': {'total_funding': 1410000, 'project_count': 27, 'projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000], ['Outdoor Warningn Sirens - Design (FEMA Project)', 84000], ['Storm Drain Master Plan (FEMA Project)', 80000], ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 44000], ['Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 92000], ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 43000], ['Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 32000], ['Westward Beach Road Shoulder Repairs (CalOES Project)', 77000]]}, 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json', 'var_functions.execute_python:56': {'total_funding': 0, 'project_count': 0, 'projects': []}}

exec(code, env_args)
