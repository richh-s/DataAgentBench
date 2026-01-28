code = """import json
import re

# Load data from files
funding_file_path = 'file_storage/functions.query_db:8.json'
civic_file_path = 'file_storage/functions.query_db:5.json'

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_category = None
    
    for line in lines:
        line = line.strip()
        
        # Detect sections
        if 'Disaster Recovery Projects' in text:
            proj_type = 'disaster'
        else:
            proj_type = 'capital'
        
        # Detect status based on section
        if 'Capital Improvement Projects (Design)' in line or 'Disaster Recovery Projects (Design)' in line:
            current_category = 'design'
        elif 'Capital Improvement Projects (Construction)' in line or 'Disaster Recovery Projects (Construction)' in line:
            current_category = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line or 'Disaster Recovery Projects (Not Started)' in line:
            current_category = 'not_started'
        
        # Skip empty or continuation lines
        if not line or line.startswith('(') or 'Updates:' in line or 'Project Schedule:' in line:
            continue
        
        # Look for project names (heuristic: longer lines that aren't continuation phrases)
        if current_category and len(line) > 15:
            skip_phrases = ['Complete', 'Advertise', 'Begin', 'Final', 'Project is currently', 'Construction was completed']
            if not any(phrase in line for phrase in skip_phrases):
                # This might be a project name
                project_name = line
                
                # Check for FEMA or emergency
                is_fema = 'FEMA' in line
                is_emergency = 'emergency' in line.lower() or 'siren' in line.lower() or 'warning' in line.lower()
                
                # If related to emergency/FEMA, add it
                if is_fema or is_emergency:
                    topics = []
                    if is_fema:
                        topics.append('FEMA')
                    if is_emergency or 'siren' in line.lower() or 'warning' in line.lower():
                        topics.append('emergency')
                    
                    projects.append({
                        'Project_Name': project_name,
                        'type': proj_type,
                        'status': current_category,
                        'topic': ','.join(topics),
                        'is_fema_related': is_fema,
                        'is_emergency_related': is_emergency or 'siren' in line.lower() or 'warning' in line.lower()
                    })

# Also check project names in funding data for FEMA/emergency keywords
fema_funding_projects = []
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower() or 'siren' in proj_name.lower() or 'warning' in proj_name.lower():
        fema_funding_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': fund.get('Funding_Source'),
            'Amount': fund.get('Amount'),
            'is_fema_related': 'FEMA' in proj_name,
            'is_emergency_related': 'emergency' in proj_name.lower() or 'siren' in proj_name.lower() or 'warning' in proj_name.lower()
        })

print('__RESULT__:')
print(json.dumps({
    'civic_projects': projects,
    'funding_projects_with_keywords': fema_funding_projects,
    'total_civic': len(projects),
    'total_funding_keyword_matches': len(fema_funding_projects)
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:6': {'funding_count': 10, 'funding_columns': ['Funding_ID', 'project_name_db', 'Funding_Source', 'Amount']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_path': 'file_storage/functions.query_db:8.json', 'civic_path': 'file_storage/functions.query_db:5.json', 'funding_exists': True, 'civic_exists': True}, 'var_functions.execute_python:14': {'funding_records': 500, 'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
