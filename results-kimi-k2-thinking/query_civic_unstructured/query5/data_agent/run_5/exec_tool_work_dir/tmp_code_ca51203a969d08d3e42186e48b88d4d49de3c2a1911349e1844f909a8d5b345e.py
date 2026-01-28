code = """import json
import re

# Load data
funding_path = locals()['var_functions.query_db:6']
civic_docs_path = locals()['var_functions.query_db:8']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project info from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    split_lines = text.split('
')
    
    current_project = None
    in_schedule_section = False
    
    for i, line in enumerate(split_lines):
        line = line.strip()
        
        # Look for project headers
        if len(line) > 10 and line == line.title() and not any(kw in line.lower() for kw in ['updates:', 'project schedule:', 'cip', 'public works']):
            if not any(line.startswith(prefix) for prefix in ['(', '-', '•', '·', 'c:', 'cid:']):
                # This might be a project name
                current_project = {
                    'Project_Name': line,
                    'st': None,
                    'et': None,
                    'type': None,
                    'status': None,
                    'topic': []
                }
        
        # Look for schedule section
        if 'project schedule:' in line.lower() or 'estimated schedule:' in line.lower():
            in_schedule_section = True
            
        # Extract dates from schedule section
        if in_schedule_section and current_project:
            # Look for lines with dates
            if re.search(r'\d{4}', line):
                # Check for start-related keywords
                if any(kw in line.lower() for kw in ['begin', 'start', 'advertise', 'initiate']):
                    if current_project['st'] is None:
                        current_project['st'] = line
                # Check for end/completion keywords
                elif any(kw in line.lower() for kw in ['complete', 'end', 'finish', 'completion']):
                    if current_project['et'] is None:
                        current_project['et'] = line
                        
        # Reset schedule section when we hit empty lines or new sections
        if line == '' and in_schedule_section:
            if current_project and (current_project['st'] or current_project['et']):
                projects.append(current_project)
            current_project = None
            in_schedule_section = False

first_ten_projects = projects[:10]
print('__RESULT__:')
print(json.dumps(first_ten_projects))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_records_count': 500, 'civic_docs_count': 5}}

exec(code, env_args)
