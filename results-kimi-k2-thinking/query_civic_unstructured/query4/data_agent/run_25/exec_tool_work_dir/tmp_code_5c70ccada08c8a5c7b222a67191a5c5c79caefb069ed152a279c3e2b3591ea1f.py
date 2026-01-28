code = """import json
import os
import re

# Load the civic documents from MongoDB result
civic_file = 'file_storage/functions.query_db:38.json'
if os.path.exists(civic_file):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = []

# Parse civic documents to extract projects with start dates
projects = []

for doc in civic_docs:
    if not isinstance(doc, dict):
        continue
        
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    section_type = ''
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect section type
        if line.startswith('Capital Improvement Projects'):
            if 'Design' in line:
                section_type = 'design'
            elif 'Construction' in line:
                section_type = 'construction'
            elif 'Not Started' in line:
                section_type = 'not started'
            continue
        
        # Look for project names (uppercase, no special chars at start)
        if line.isupper() and len(line) > 10 and not line.startswith('('):
            project = {
                'Project_Name': line,
                'topic': '',
                'type': 'capital',
                'status': section_type,
                'st': '',
                'et': ''
            }
            projects.append(project)
        
        # Look for schedule information
        if projects and ':' in line:
            parts = line.split(':', 1)
            if len(parts) == 2:
                field = parts[0].strip().lower()
                value = parts[1].strip()
                
                # Check for spring 2022 start dates
                if '2022' in value and 'spring' in value.lower():
                    if not projects[-1]['st']:
                        projects[-1]['st'] = value
                
                # Extract topics
                topics = []
                v_lower = value.lower()
                if 'drain' in v_lower or 'storm' in v_lower:
                    topics.append('drainage')
                if 'fema' in v_lower:
                    topics.append('FEMA')
                if 'road' in v_lower:
                    topics.append('road')
                if 'park' in v_lower:
                    topics.append('park')
                
                if topics:
                    projects[-1]['topic'] = ', '.join(topics)
        
        # Check for disaster project indicators
        if projects and ('fema' in line.lower() or 'caloes' in line.lower() or 'caljpia' in line.lower()):
            projects[-1]['type'] = 'disaster'

spring_2022_projects = []
for proj in projects:
    st = proj.get('st', '')
    if st and '2022' in st and 'spring' in st.lower():
        spring_2022_projects.append(proj)

# Load funding data
funding_file = 'file_storage/functions.query_db:28.json'
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = []

# Convert amounts to integers
for record in funding_data:
    try:
        record['Amount'] = int(str(record.get('Amount', '0')))
    except:
        record['Amount'] = 0

# Create funding map
funding_map = {record.get('Project_Name', ''): record['Amount'] for record in funding_data}

# Calculate total funding for Spring 2022 projects
total_funding = 0
matched_projects = []

for proj in spring_2022_projects:
    proj_name = proj['Project_Name']
    
    # Direct match
    if proj_name in funding_map:
        funding = funding_map[proj_name]
        total_funding += funding
        matched_projects.append({'name': proj_name, 'funding': funding})
        continue
    
    # Look for partial matches
    for fund_name, amount in funding_map.items():
        # Check if project name is contained in fund name or vice versa
        proj_lower = proj_name.lower()
        fund_lower = fund_name.lower()
        
        if proj_lower in fund_lower or fund_lower in proj_lower:
            total_funding += amount
            matched_projects.append({
                'name': proj_name,
                'funding': amount,
                'matched_to': fund_name
            })
            break

print('__RESULT__:')
print(json.dumps({
    'count': len(spring_2022_projects),
    'total_funding': total_funding,
    'projects': matched_projects,
    'all_spring_projects': spring_2022_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records', 'var_functions.list_db:24': ['civic_docs'], 'var_functions.execute_python:26': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:28': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
