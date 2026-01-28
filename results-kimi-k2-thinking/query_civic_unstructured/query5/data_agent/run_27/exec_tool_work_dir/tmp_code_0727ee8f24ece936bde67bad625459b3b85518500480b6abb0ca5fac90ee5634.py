code = """import json
import re

# Load funding data
funding_data = json.load(open('file_storage/functions.query_db:5.json'))

# Load civic documents
all_civic_docs = json.load(open('file_storage/functions.query_db:6.json'))

# Build funding map
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Find disaster projects that started in 2022
disaster_projects_2022 = {}

# First, identify all disaster-related projects from funding
all_disaster_projects = {}
for project_name, amount in funding_map.items():
    # Check if it's a disaster project
    is_disaster = False
    
    # Check for explicit markers
    if '(FEMA Project)' in project_name or '(CalOES Project)' in project_name or '(CalJPIA Project)' in project_name:
        is_disaster = True
    
    # Check for FEMA/CalOES/CalJPIA in name
    if not is_disaster and ('FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name):
        is_disaster = True
    
    if is_disaster:
        all_disaster_projects[project_name] = amount

print('Found', len(all_disaster_projects), 'disaster projects in funding data')

# Now check civic documents for which ones started in 2022
for project_name in all_disaster_projects.keys():
    amount = all_disaster_projects[project_name]
    
    # Check each civic document
    for doc in all_civic_docs:
        text = doc['text']
        
        # If project is mentioned in this document
        if project_name in text:
            # Check if 2022 appears in the document (indicating 2022 timeframe)
            if '2022' in text:
                # More specifically, check if this project section mentions 2022
                # Find the project mention and check surrounding context
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if project_name in line:
                        # Check this line and nearby lines for 2022 date indicators
                        start = max(0, i-3)
                        end = min(len(lines), i+8)
                        context = '\n'.join(lines[start:end])
                        
                        # Look for start/completion dates with 2022
                        date_indicators = [
                            '2022-', '2022 Spring', '2022 Summer', '2022 Fall', '2022 Winter',
                            '2022 January', '2022 February', '2022 March', '2022 April', '2022 May',
                            '2022 June', '2022 July', '2022 August', '2022 September', '2022 October',
                            '2022 November', '2022 December', 'Spring 2022', 'Summer 2022', 'Fall 2022',
                            'January 2022', 'February 2022', 'March 2022', 'April 2022', 'May 2022',
                            'June 2022', 'July 2022', 'August 2022', 'September 2022', 'October 2022',
                            'November 2022', 'December 2022', 'Start.*2022', 'Complete.*2022',
                            '2022.*Start', '2022.*Complete', '2022.*Construction', 'Construction.*2022'
                        ]
                        
                        for indicator in date_indicators:
                            if re.search(indicator, context, re.IGNORECASE):
                                disaster_projects_2022[project_name] = amount
                                break
                        
                        # If we found a match, no need to check more lines for this project
                        if project_name in disaster_projects_2022:
                            break

# Also catch projects explicitly named with years (like "2022 Morning View...")
for doc in all_civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        # Look for lines that start with year patterns
        if line.startswith('2022 ') and len(line) > 10:
            # Check if this is a disaster project
            for project_name, amount in all_disaster_projects.items():
                # If the line contains the project name or they're similar
                if (project_name in line or line in project_name) and len(project_name) > 10:
                    disaster_projects_2022[project_name] = amount
                    break

# Consolidate results
total_funding = sum(disaster_projects_2022.values())
project_list = [[name, amount] for name, amount in disaster_projects_2022.items()]
project_list.sort(key=lambda x: x[1], reverse=True)

result = {
    'total_funding': total_funding,
    'project_count': len(project_list),
    'projects': project_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}, 'var_functions.execute_python:42': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:46': {'total_funding': 1410000, 'project_count': 27, 'projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000], ['Outdoor Warningn Sirens - Design (FEMA Project)', 84000], ['Storm Drain Master Plan (FEMA Project)', 80000], ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 44000], ['Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 92000], ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 43000], ['Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 32000], ['Westward Beach Road Shoulder Repairs (CalOES Project)', 77000]]}, 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json', 'var_functions.execute_python:56': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.execute_python:62': {'total_funding': 0, 'project_count': 0, 'projects': []}}

exec(code, env_args)
