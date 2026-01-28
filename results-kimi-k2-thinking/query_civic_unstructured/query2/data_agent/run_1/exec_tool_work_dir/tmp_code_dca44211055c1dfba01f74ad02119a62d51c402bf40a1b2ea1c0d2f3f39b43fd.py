code = """import json
import re

# Load funding records
funding_file = locals()['var_functions.query_db:24']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:26']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding map by project name
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name', '').strip()
    if name:
        funding_map[name] = int(rec.get('Amount', 0))

# Extract projects from civic documents
all_projects = []

# Pattern to match project names - lines that are likely project titles
project_line_pattern = re.compile(r'^[A-Z][a-zA-Z0-9\s\&\-\(\)]{10,80}$')

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_section = ''
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Determine current section/status
        if 'Projects (Construction)' in line:
            current_section = 'completed'
        elif 'Projects (Design)' in line:
            current_section = 'design'
        elif 'Projects (Not Started)' in line:
            current_section = 'not_started'
        
        # Look for park projects in construction/completed section
        if current_section == 'completed' and 'park' in line.lower():
            # Skip if line is too short or looks like a header
            if len(line) < 15 or 'capital improvement' in line.lower():
                continue
            
            # Look for completion date in this or next few lines
            completion_date = None
            for j in range(max(0, i-2), min(len(lines), i+5)):
                if '2022' in lines[j]:
                    # Look for month names
                    date_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+2022', lines[j], re.IGNORECASE)
                    if date_match:
                        completion_date = date_match.group(1)
                        break
            
            if completion_date:
                all_projects.append(line)

# Find funding for these park projects
park_project_funding = {}
for park_project in all_projects:
    # Direct match
    if park_project in funding_map:
        park_project_funding[park_project] = funding_map[park_project]
    else:
        # Fuzzy match - check if any funded project contains this name
        for funded_name in funding_map:
            if park_project.lower() in funded_name.lower() or funded_name.lower() in park_project.lower():
                park_project_funding[park_project] = funding_map[funded_name]
                break

# Calculate total funding
total_funding = sum(park_project_funding.values())

result = {
    'park_projects_found': all_projects,
    'projects_with_funding': list(park_project_funding.keys()),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'funding_records_count': 10, 'civic_docs_count': 5, 'funding_projects_count': 10}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_data_type': "<class 'list'>"}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'funding_records_loaded': 500, 'civic_docs_loaded': 5}}

exec(code, env_args)
