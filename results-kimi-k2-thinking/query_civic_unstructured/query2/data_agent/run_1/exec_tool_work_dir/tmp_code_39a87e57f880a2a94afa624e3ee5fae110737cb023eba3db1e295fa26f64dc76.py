code = """import json
import re

# Load data
funding_path = locals()['var_functions.query_db:24']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

civic_path = locals()['var_functions.query_db:26']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding map
funding_by_project = {}
for record in funding_records:
    project_name = record.get('Project_Name', '').strip()
    if project_name:
        funding_by_project[project_name] = int(record.get('Amount', 0))

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_status = ''
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check section headers
        if 'Construction)' in line:
            current_status = 'completed'
        elif 'Design)' in line:
            current_status = 'design'
        elif 'Not Started)' in line:
            current_status = 'not started'
        
        # Look for project names (simple heuristic: starts with capital letter, not a bullet)
        if (line[0].isupper() and 
            not line.startswith('\u2022') and 
            not line.startswith('(') and
            len(line) > 10 and
            'Project' not in line[:20] and  # Not a header
            any(word in line.lower() for word in ['park', 'project', 'improvements', 'repairs', 'facility'])):
            
            # Skip common headers
            if line in ['Public Works Commission', 'Agenda Report', 'Capital Improvement Projects']:
                continue
            
            project_name = line
            
            # Check if this is a park project
            is_park = 'park' in project_name.lower()
            
            # Look for completion dates in nearby lines
            completion_date = None
            for j in range(i, min(i+5, len(lines))):
                next_line = lines[j].lower()
                if '2022' in lines[j] and ('completed' in next_line or 'complete' in next_line):
                    # Extract month/year
                    date_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+2022', lines[j], re.IGNORECASE)
                    if date_match:
                        completion_date = date_match.group(0)
                        break
            
            projects.append({
                'name': project_name,
                'status': current_status,
                'is_park': is_park,
                'completion_date': completion_date
            })

# Find park projects completed in 2022
park_projects_2022 = [p for p in projects if p['is_park'] and p['status'] == 'completed' and p['completion_date']]

print('__RESULT__:')
print(json.dumps({
    'projects_found': len(projects),
    'park_projects_2022': park_projects_2022,
    'count': len(park_projects_2022)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'funding_records_count': 10, 'civic_docs_count': 5, 'funding_projects_count': 10}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_data_type': "<class 'list'>"}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'funding_records_loaded': 500, 'civic_docs_loaded': 5}}

exec(code, env_args)
