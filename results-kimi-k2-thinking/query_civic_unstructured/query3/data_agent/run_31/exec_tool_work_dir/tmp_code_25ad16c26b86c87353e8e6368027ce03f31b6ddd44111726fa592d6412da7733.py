code = """import json
import re

funding_file = 'file_storage/functions.query_db:8.json'
civic_file = 'file_storage/functions.query_db:5.json'

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# First, identify all FEMA/emergency related project names from funding data
fema_project_names = set()
fema_funding_map = {}

for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        fema_project_names.add(proj_name)
        fema_funding_map[proj_name] = {
            'Funding_Source': fund.get('Funding_Source'),
            'Amount': fund.get('Amount')
        }

# Now extract projects from civic documents
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check if document contains FEMA or emergency
    if 'fema' in lower_text or 'emergency' in lower_text:
        lines = text.split('\n')
        section = None
        
        for line in lines:
            line_clean = line.strip()
            if not line_clean:
                continue
                
            # Detect sections
            if 'Design' in line_clean:
                section = 'design'
            elif 'Construction' in line_clean:
                section = 'construction'
            elif 'Not Started' in line_clean:
                section = 'not_started'
            
            # Look for project names containing FEMA or emergency
            if 'FEMA' in line_clean or 'emergency' in line_clean.lower():
                if len(line_clean) > 10 and not line_clean.startswith('('):
                    proj_type = 'disaster' if 'Disaster' in text else 'capital'
                    
                    extracted_projects.append({
                        'Project_Name': line_clean,
                        'type': proj_type,
                        'status': section,
                        'topic': 'FEMA' if 'FEMA' in line_clean else 'emergency'
                    })

print('__RESULT__:')
result = {
    'fema_project_names_count': len(fema_project_names),
    'extracted_projects_count': len(extracted_projects),
    'sample_fema_names': list(fema_project_names)[:10],
    'sample_extracted': extracted_projects[:10]
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:6': {'funding_count': 10, 'funding_columns': ['Funding_ID', 'project_name_db', 'Funding_Source', 'Amount']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_path': 'file_storage/functions.query_db:8.json', 'civic_path': 'file_storage/functions.query_db:5.json', 'funding_exists': True, 'civic_exists': True}, 'var_functions.execute_python:14': {'funding_records': 500, 'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
