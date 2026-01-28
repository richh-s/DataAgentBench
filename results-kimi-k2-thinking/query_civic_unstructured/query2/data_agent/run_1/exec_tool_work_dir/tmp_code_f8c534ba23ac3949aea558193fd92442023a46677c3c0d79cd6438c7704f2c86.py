code = """import json
import re

# Load funding records
fpath = locals()['var_functions.query_db:24']
with open(fpath) as f:
    funding = json.load(f)

# Load civic documents
cpath = locals()['var_functions.query_db:26']
with open(cpath) as f:
    civic_docs = json.load(f)

# Build funding map
funding_map = {}
for rec in funding:
    name = rec.get('Project_Name', '').strip()
    if name:
        funding_map[name] = int(rec.get('Amount', 0))

# Extract park projects completed in 2022 from civic docs
park_projects = []

for doc in civic_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    status = ''
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Track status based on sections
        if 'Construction)' in line:
            status = 'completed'
        elif 'Not Started)' in line:
            status = 'not_started'
        elif 'Design)' in line:
            status = 'design'
        
        # Look for park projects
        if 'park' in line.lower() and len(line) > 10:
            # Skip headers
            if 'Capital Improvement' in line or 'Project' == line:
                continue
            
            # Check for completion date
            date = None
            for j in range(i, min(i+3, len(lines))):
                if '2022' in lines[j]:
                    m = re.search(r'(\w+\s+2022)', lines[j])
                    if m:
                        date = m.group(1)
                        break
            
            if status == 'completed' and date:
                park_projects.append({
                    'name': line,
                    'date': date
                })

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': park_projects,
    'count': len(park_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'funding_records_count': 10, 'civic_docs_count': 5, 'funding_projects_count': 10}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_data_type': "<class 'list'>"}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'funding_records_loaded': 500, 'civic_docs_loaded': 5}}

exec(code, env_args)
