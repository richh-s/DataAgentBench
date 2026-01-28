code = """import json

# Load data
funding_data = locals()['var_functions.query_db:6']

documents_path = locals()['var_functions.query_db:0']
with open(documents_path, 'r') as doc_file:
    documents = json.load(doc_file)

print('__RESULT__:')

# Build funding dictionary
funding_dict = {}
for record in funding_data:
    funding_dict[record['Project_Name']] = record

# Find projects in documents
results = []
found_project_names = set()

for doc in documents:
    doc_lines = doc['text'].splitlines()
    
    for line_num, line_text in enumerate(doc_lines):
        line_text = line_text.strip()
        
        if len(line_text) < 10:
            continue
        if not line_text[0].isupper():
            continue
            
        for proj_name in funding_dict:
            clean_name = proj_name.replace('(FEMA Project)', '').replace('(CalOES Project)', '').strip()
            
            if clean_name and clean_name.lower() in line_text.lower():
                funding_info = funding_dict[proj_name]
                amount_val = int(funding_info['Amount'])
                funding_source_val = funding_info['Funding_Source']
                
                # Determine project type
                project_type = 'disaster' if 'FEMA' in proj_name else 'capital'
                
                # Find status
                status_val = 'unknown'
                context_start = max(0, line_num - 5)
                context_end = min(len(doc_lines), line_num + 10)
                context_text = ' '.join(doc_lines[context_start:context_end]).lower()
                
                if 'design' in context_text:
                    status_val = 'design'
                elif 'completed' in context_text:
                    status_val = 'completed'
                elif 'construction' in context_text:
                    status_val = 'construction'
                elif 'not started' in context_text:
                    status_val = 'not started'
                
                results.append({
                    'project_name': proj_name,
                    'funding_source': funding_source_val,
                    'amount': amount_val,
                    'status': status_val,
                    'type': project_type
                })
                
                found_project_names.add(proj_name)
                break

# Remove duplicates
final_results = []
seen_names = set()
for item in results:
    if item['project_name'] not in seen_names:
        final_results.append(item)
        seen_names.add(item['project_name'])

# Add projects not found in documents
for proj_name, funding_info in funding_dict.items():
    if proj_name not in seen_names:
        final_results.append({
            'project_name': proj_name,
            'funding_source': funding_info['Funding_Source'],
            'amount': int(funding_info['Amount']),
            'status': 'unknown',
            'type': 'disaster' if 'FEMA' in proj_name else 'unknown'
        })

print(json.dumps(final_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'message': 'Found 5 documents', 'first_doc_keys': ['_id', 'filename', 'text'], 'text_sample_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'emergency_count': 2, 'fema_count': 5, 'total_docs': 5}, 'var_functions.query_db:6': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
