code = """import json
import re
import os

# Load data from files
funding_file_path = 'file_storage/functions.query_db:8.json'
civic_file_path = 'file_storage/functions.query_db:5.json'

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_category = None
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Detect category headers
        if 'Capital Improvement Projects (Design)' in line:
            current_category = 'capital_design'
        elif 'Capital Improvement Projects (Construction)' in line:
            current_category = 'capital_construction'
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_category = 'capital_not_started'
        elif 'Disaster Recovery Projects (Design)' in line:
            current_category = 'disaster_design'
        elif 'Disaster Recovery Projects (Construction)' in line:
            current_category = 'disaster_construction'
        elif 'Disaster Recovery Projects (Not Started)' in line:
            current_category = 'disaster_not_started'
        
        # Skip empty lines and known markers
        if not line or line.startswith('(cid:') or 'Project Schedule:' in line or 'Updates:' in line:
            continue
            
        # Extract project name (typically a line that's not a bullet point)
        if current_category and line and not line.startswith('(') and not line.startswith('•') and len(line) > 10:
            # Check if this looks like a project title (not a continuation)
            if not any(keyword in line.lower() for keyword in ['updates:', 'project schedule:', 'complete', 'advertise', 'begin', 'final design']):
                # This is likely a project name
                current_project = line.strip()
                
                # Determine type based on category
                project_type = 'disaster' if 'disaster' in current_category else 'capital'
                
                # Determine status based on category
                if 'design' in current_category:
                    status = 'design'
                elif 'construction' in current_category:
                    status = 'completed' if 'completed' in text.lower() else 'design'
                elif 'not_started' in current_category:
                    status = 'not_started'
                else:
                    status = 'design'
                
                # Check for FEMA/emergency keywords
                has_fema = 'FEMA' in line
                has_emergency = 'emergency' in line.lower()
                
                # Extract topics from project name
                topics = []
                if 'FEMA' in line:
                    topics.append('FEMA')
                if any(word in line.lower() for word in ['drain', 'storm', 'drainage']):
                    topics.append('drainage')
                if any(word in line.lower() for word in ['park', 'playground']):
                    topics.append('park')
                if any(word in line.lower() for word in ['road', 'street', 'highway']):
                    topics.append('road')
                if any(word in line.lower() for word in ['bridge', 'culvert', 'retaining wall']):
                    topics.append('infrastructure')
                if any(word in line.lower() for word in ['warning', 'siren', 'sign']):
                    topics.append('emergency warning')
                
                projects.append({
                    'Project_Name': current_project,
                    'type': project_type,
                    'status': status,
                    'topic': ','.join(topics) if topics else '',
                    'is_fema_related': has_fema,
                    'is_emergency_related': has_emergency or 'emergency warning' in topics
                })

# Filter for projects related to emergency or FEMA
filtered_projects = [p for p in projects if p['is_fema_related'] or p['is_emergency_related']]

print('__RESULT__:')
print(json.dumps({
    'total_projects_extracted': len(projects),
    'emergency_fema_projects': len(filtered_projects),
    'sample_projects': filtered_projects[:5]
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:6': {'funding_count': 10, 'funding_columns': ['Funding_ID', 'project_name_db', 'Funding_Source', 'Amount']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_path': 'file_storage/functions.query_db:8.json', 'civic_path': 'file_storage/functions.query_db:5.json', 'funding_exists': True, 'civic_exists': True}, 'var_functions.execute_python:14': {'funding_records': 500, 'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
