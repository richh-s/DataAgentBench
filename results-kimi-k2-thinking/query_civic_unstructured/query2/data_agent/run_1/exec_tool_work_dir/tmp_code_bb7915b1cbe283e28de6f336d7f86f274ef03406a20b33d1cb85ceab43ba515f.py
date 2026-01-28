code = """import json
import re

# Load data
funding_path = locals()['var_functions.query_db:24']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

civic_path = locals()['var_functions.query_db:26']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Create a map of project names to funding amounts
funding_by_project = {}
for record in funding_records:
    project_name = record.get('Project_Name', '').strip()
    if project_name:
        amount = int(record.get('Amount', 0))
        funding_by_project[project_name] = amount

# Extract project information from civic documents
projects = []

# Regular expressions for parsing
project_patterns = [
    r'^([A-Z][a-zA-Z0-9\s\&\-\(\)]+?(?:Project|Improvements|Repairs|Facility|Structure|Park|Road|Lane|System|Plan|Study|Playground|Walkway|Benches))$',
]

completion_patterns = [
    r'(?:completed|complete|completion)[^.]*?(\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+202[0-9]\b)',
    r'(?:Construction was completed|completed)[^,]*,\s*(\w+\s+202[0-9])',
]

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    current_section = ''
    current_status = ''
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Check for section headers
        if 'Capital Improvement Projects (Construction)' in line or 'Projects (Construction)' in line:
            current_section = 'construction'
            current_status = 'completed'
        elif 'Capital Improvement Projects (Design)' in line or 'Projects (Design)' in line:
            current_section = 'design'
            current_status = 'design'
        elif 'Capital Improvement Projects (Not Started)' in line or 'Projects (Not Started)' in line:
            current_section = 'not_started'
            current_status = 'not started'
        
        # Look for project names (lines that look like project titles)
        project_match = None
        for pattern in project_patterns:
            match = re.match(pattern, line)
            if match:
                project_name = match.group(1).strip()
                # Exclude common headers and generic terms
                if project_name not in ['Discussion', 'Background', 'RECOMMENDED ACTION', 'SUBJECT']:
                    project_match = project_name
                    break
        
        if project_match:
            project_name = project_match
            # Look ahead for completion information
            completion_date = None
            look_ahead = 3  # Look ahead up to 3 lines
            for j in range(i, min(i + look_ahead, len(lines))):
                next_line = lines[j]
                for pattern in completion_patterns:
                    date_match = re.search(pattern, next_line, re.IGNORECASE)
                    if date_match:
                        completion_date = date_match.group(1)
                        break
                if completion_date:
                    break
            
            # Determine topic
            topics = []
            if 'park' in project_name.lower():
                topics.append('park')
            if 'drain' in project_name.lower():
                topics.append('drainage')
            if 'road' in project_name.lower():
                topics.append('road')
            if 'storm' in project_name.lower():
                topics.append('storm drain')
            
            projects.append({
                'project_name': project_name,
                'status': current_status,
                'completion_date': completion_date,
                'topics': topics,
                'is_park': 'park' in [t.lower() for t in topics],
                'filename': filename
            })
        
        i += 1

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for project in projects:
    if project['is_park'] and project['status'] == 'completed':
        if project['completion_date'] and '2022' in project['completion_date']:
            park_projects_2022.append(project)

print('__RESULT__:')
print(json.dumps({
    'total_projects_parsed': len(projects),
    'park_projects_2022': park_projects_2022,
    'park_projects_2022_count': len(park_projects_2022),
    'sample_projects': projects[:5] if projects else []
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'funding_records_count': 10, 'civic_docs_count': 5, 'funding_projects_count': 10}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_data_type': "<class 'list'>"}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'funding_records_loaded': 500, 'civic_docs_loaded': 5}}

exec(code, env_args)
