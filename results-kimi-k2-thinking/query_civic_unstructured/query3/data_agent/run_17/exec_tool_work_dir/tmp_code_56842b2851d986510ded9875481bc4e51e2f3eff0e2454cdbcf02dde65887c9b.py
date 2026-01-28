code = """import json

# Load funding data
funding_data = locals()['var_functions.query_db:6']

# Load documents
documents_path = locals()['var_functions.query_db:0']
with open(documents_path, 'r') as f:
    documents = json.load(f)

print('__RESULT__:')

# Create funding dictionary
funding_dict = {}
for f in funding_data:
    funding_dict[f['Project_Name']] = f

found_projects = []

# Process each document
for doc in documents:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10:
            continue
        if not line[0].isupper():
            continue
            
        # Check each project name
        for proj_name in funding_dict:
            # Clean the project name for matching
            clean_proj = proj_name.replace('(FEMA Project)', '').replace('(CalOES Project)', '').strip()
            # Check if the project appears in the line
            if clean_proj and clean_proj.lower() in line.lower():
                # Get funding info
                funding_info = funding_dict[proj_name]
                amount = int(funding_info['Amount'])
                funding_source = funding_info['Funding_Source']
                
                # Determine type
                proj_type = 'disaster' if 'FEMA' in proj_name else 'capital'
                
                # Look for status in nearby lines
                status = 'unknown'
                nearby_text = '\n'.join(lines[max(0, i-5):min(len(lines), i+10)]).lower()
                
                if 'design' in nearby_text:
                    status = 'design'
                elif 'completed' in nearby_text:
                    status = 'completed'
                elif 'construction' in nearby_text:
                    status = 'construction'
                elif 'not started' in nearby_text:
                    status = 'not started'
                
                found_projects.append({
                    'project_name': proj_name,
                    'funding_source': funding_source,
                    'amount': amount,
                    'status': status,
                    'type': proj_type
                })
                break

# Remove duplicates
unique = []
seen = set()
for p in found_projects:
    if p['project_name'] not in seen:
        unique.append(p)
        seen.add(p['project_name'])

# Add missing projects from funding data
for proj_name, info in funding_dict.items():
    if proj_name not in seen:
        amount = int(info['Amount'])
        funding_source = info['Funding_Source']
        proj_type = 'disaster' if 'FEMA' in proj_name else 'unknown'
        
        unique.append({
            'project_name': proj_name,
            'funding_source': funding_source,
            'amount': amount,
            'status': 'unknown',
            'type': proj_type
        })

print(json.dumps(unique))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'message': 'Found 5 documents', 'first_doc_keys': ['_id', 'filename', 'text'], 'text_sample_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'emergency_count': 2, 'fema_count': 5, 'total_docs': 5}, 'var_functions.query_db:6': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
