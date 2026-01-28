code = """import json, re

funding_file = 'file_storage/functions.query_db:8.json'
civic_file = 'file_storage/functions.query_db:5.json'

with open(funding_file, 'r') as f:
    all_funding = json.load(f)

with open(civic_file, 'r') as f:
    all_docs = json.load(f)

# Get FEMA/emergency projects from funding
target_projects = []
for f in all_funding:
    name = f.get('Project_Name', '')
    if 'FEMA' in name or 'emergency' in name.lower():
        target_projects.append({
            'Project_Name': name,
            'Funding_Source': f.get('Funding_Source'),
            'Amount': f.get('Amount')
        })

# Find these projects in civic docs to get status
for doc in all_docs:
    text = doc.get('text', '')
    for proj in target_projects:
        if proj['Project_Name'] in text:
            proj['found_in_docs'] = True

print('__RESULT__:')
print(json.dumps({'total_matches': len(target_projects), 'projects': target_projects[:20]}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:6': {'funding_count': 10, 'funding_columns': ['Funding_ID', 'project_name_db', 'Funding_Source', 'Amount']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_path': 'file_storage/functions.query_db:8.json', 'civic_path': 'file_storage/functions.query_db:5.json', 'funding_exists': True, 'civic_exists': True}, 'var_functions.execute_python:14': {'funding_records': 500, 'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
