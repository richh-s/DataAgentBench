code = """import json, os, re

# Load civic documents
civic_path = 'file_storage/functions.query_db:38.json'
civic_docs = json.load(open(civic_path, 'r'))

# Load funding data
funding_path = 'file_storage/functions.query_db:28.json'
funding_data = json.load(open(funding_path, 'r'))

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    try:
        amount = int(str(record.get('Amount', '0')))
    except:
        amount = 0
    funding_map[name] = amount

# Parse civic documents to find projects starting in Spring 2022
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Extract project name and schedule info
    lines = text.split('\n')
    current_section = ''
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect section type
        lower_line = line.lower()
        if 'capital improvement' in lower_line:
            if 'design' in lower_line:
                current_section = 'design'
            elif 'construction' in lower_line:
                current_section = 'construction'
            elif 'not started' in lower_line:
                current_section = 'not started'
        
        # Look for project names (usually in uppercase)
        if line.isupper() and len(line) > 10 and not line.startswith('('):
            project_name = line
            # Look ahead for schedule info
            project_info = {
                'name': project_name,
                'funding': 0
            }
            spring_2022_projects.append(project_info)
        
        # Look for Spring 2022 dates
        if '2022' in line and 'spring' in line.lower():
            if spring_2022_projects:
                # Get funding for the last project
                proj_name = spring_2022_projects[-1]['name']
                if proj_name in funding_map:
                    spring_2022_projects[-1]['funding'] = funding_map[proj_name]
                # TODO: Add better date parsing to properly link dates with projects

# Calculate total funding
total_funding = sum(p['funding'] for p in spring_2022_projects if p['funding'] > 0)
project_count = len(spring_2022_projects)

print('__RESULT__:')
print(json.dumps({'count': project_count, 'total_funding': total_funding}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records', 'var_functions.list_db:24': ['civic_docs'], 'var_functions.execute_python:26': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:28': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
