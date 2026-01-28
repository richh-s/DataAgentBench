code = """import json
import re
from datetime import datetime

# Load data
civic_file = locals()['var_functions.query_db:8']
funding_records = locals()['var_functions.query_db:5']

if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into lines for easier parsing
    lines = text.split('\n')
    
    # Track current section/category
    current_section = ''
    current_status = ''
    
    # Look for project name patterns
    project_patterns = [
        r'^([A-Z][a-zA-Z\s\&\-\(\)]+?(?:Project|Improvements|Repairs|Facility|Structure|Park|Road|Lane|System|Plan|Study))$',  # General projects
        r'^(\d{4}\s+[A-Z][a-zA-Z\s\&\-\(\)]+?(?:Project|Improvements|Repairs))$',  # Projects starting with year
    ]
    
    # Status indicators
    status_indicators = {
        'completed': r'completed|Complete Construction|Notice of completion filed',
        'design': r'Design|design phase|Complete Design|Advertise|Begin Construction',
        'not started': r'Not Started|identified|preliminary design phase'
    }
    
    section_indicators = {
        'completed': r'Capital Improvement Projects \(Construction\)|Projects \(Construction\)',
        'design': r'Capital Improvement Projects \(Design\)|Projects \(Design\)',
        'not started': r'Capital Improvement Projects \(Not Started\)|Projects \(Not Started\)'
    }
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if this is a section header
        for status_type, pattern in section_indicators.items():
            if re.search(pattern, line, re.IGNORECASE):
                current_section = status_type
                break
        
        # Check for project names
        project_name = None
        for pattern in project_patterns:
            match = re.match(pattern, line.strip())
            if match:
                project_name = match.group(1).strip()
                break
        
        if project_name:
            # Determine status
            if current_section:
                current_status = current_section
            else:
                # Check if line contains status hints
                for status_type, pattern in status_indicators.items():
                    if re.search(pattern, line, re.IGNORECASE):
                        current_status = status_type
                        break
            
            # Default status if not determined
            if not current_status:
                current_status = 'unknown'
            
            # Extract date information (look for dates in subsequent lines)
            date_patterns = [
                r'([A-Za-z]+\s+\d{4})',  # "November 2022"
                r'(\d{4}-[A-Za-z]+)',     # "2022-Spring"
                r'(\d{4}-\d{2})',        # "2022-02"
            ]
            
            # Look for completion dates specifically
            completion_date_match = None
            if 'complete' in line.lower() and any(month in line.lower() for month in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']):
                completion_date_match = re.search(r'([A-Za-z]+\s+\d{4})', line, re.IGNORECASE)
            
            projects.append({
                'project_name': project_name,
                'status': current_status,
                'filename': filename,
                'completion_date': completion_date_match.group(1) if completion_date_match else None,
                'topics': 'park' if 'park' in project_name.lower() else 'unknown'
            })

# Filter for park-related projects completed in 2022
park_projects_completed_2022 = []

for project in projects:
    # Check if it's park-related
    is_park = 'park' in project['project_name'].lower()
    
    # Check if it's completed
    is_completed = project['status'] == 'completed' or 'complete' in project['status'].lower()
    
    # Check if completed in 2022
    completed_2022 = False
    if project['completion_date']:
        completed_2022 = '2022' in str(project['completion_date'])
    else:
        # Check if filename or other context suggests 2022
        if '2022' in project['filename']:
            completed_2022 = True
    
    if is_park and is_completed and completed_2022:
        park_projects_completed_2022.append(project)

print('__RESULT__:')
print(json.dumps({
    'total_projects_found': len(projects),
    'park_projects_completed_2022': park_projects_completed_2022,
    'count': len(park_projects_completed_2022)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'funding_records_count': 10, 'civic_docs_count': 5, 'funding_projects_count': 10}}

exec(code, env_args)
