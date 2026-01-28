code = """import json
import re

# Load funding data
funding_data = locals()['var_functions.query_db:6']

# Load documents
documents_path = locals()['var_functions.query_db:0']
with open(documents_path, 'r') as f:
    documents = json.load(f)

print('__RESULT__:')

# Create dictionary of funding projects
funding_dict = {}
for f in funding_data:
    funding_dict[f['Project_Name']] = f

# Projects to look for in documents
project_names = list(funding_dict.keys())

# Extract project info from documents
found_projects = []

for doc in documents:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if len(line_clean) < 10 or not line_clean[0].isupper():
            continue
            
        # Check if any project name matches
        for proj_name in project_names:
            clean_proj = proj_name.replace('(FEMA Project)', '').replace('(CalOES Project)', '').replace('(CalJPIA/FEMA Project)', '').strip()
            if clean_proj and clean_proj.lower() in line_clean.lower():
                # Found a match
                status = 'unknown'
                proj_type = 'disaster' if 'FEMA' in proj_name else 'capital'
                
                # Look for status in nearby lines
                for j in range(max(0, i-8), min(len(lines), i+12)):
                    nearby = lines[j].lower()
                    if 'design' in nearby and ('complete' in nearby or 'final' in nearby):
                        status = 'design'
                        break
                    elif 'complete' in nearby and ('construction' in nearby or 'project' in nearby):
                        if 'completed' in nearby or 'was completed' in nearby:
                            status = 'completed'
                            break
                    elif 'construction' in nearby:
                        if 'under construction' in nearby or 'currently' in nearby:
                            status = 'construction'
                            break
                    elif 'not started' in nearby:
                        status = 'not started'
                        break
                
                found_projects.append({
                    'project_name': proj_name,
                    'funding_source': funding_dict[proj_name]['Funding_Source'],
                    'amount': int(funding_dict[proj_name]['Amount']),
                    'status': status,
                    'type': proj_type
                })
                break  # Only match once per line

# Remove duplicates
unique_projects = []
seen = set()
for p in found_projects:
    name = p['project_name']
    if name not in seen:
        unique_projects.append(p)
        seen.add(name)

# Add projects from funding that weren't found in documents
for proj_name, info in funding_dict.items():
    if proj_name not in seen:
        unique_projects.append({
            'project_name': proj_name,
            'funding_source': info['Funding_Source'],
            'amount': int(info['Amount']),
            'status': 'unknown',
            'type': 'disaster' if 'FEMA' in proj_name else 'unknown'
        })

# Format for output
output = []
for proj in unique_projects:
    output.append({
        'project_name': proj['project_name'],
        'funding_source': proj['funding_source'],
        'amount': proj['amount'],
        'status': proj['status'],
        'type': proj['type']
    })

print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'message': 'Found 5 documents', 'first_doc_keys': ['_id', 'filename', 'text'], 'text_sample_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'emergency_count': 2, 'fema_count': 5, 'total_docs': 5}, 'var_functions.query_db:6': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
