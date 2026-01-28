code = """import json
import re

# Load the disaster documents that mention 2022
docs_path = locals()['var_functions.query_db:42']
with open(docs_path, 'r') as f:
    docs_2022 = json.load(f)

# Load all funding data
funding_path = locals()['var_functions.query_db:12']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Extract disaster project names from 2022 documents
project_names_2022 = set()

for doc in docs_2022:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines and metadata
        if not line or len(line) < 10:
            continue
        if any(skip in line for skip in ['To:', 'Prepared', 'Approved', 'Date:', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Page', 'Agenda']):
            continue
        
        # Look for lines that might be project names followed by project details
        if not line.startswith('(') and not line.startswith('•') and not line.startswith('cid:'):
            # Check if next line has project indicators
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith('(') or 'Updates:' in next_line or 'Project Schedule:' in next_line:
                    # Check if this line or nearby context has disaster keywords
                    context = ' '.join(lines[max(0,i-3):i+5])
                    if any(kw in context for kw in ['FEMA', 'CalOES', 'CalJPIA']):
                        # Check if 2022 appears in nearby context
                        if '2022' in context:
                            project_names_2022.add(line)

print(f"Found {len(project_names_2022)} potential disaster projects from 2022 documents")
print(f"Sample projects: {list(project_names_2022)[:10]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:24': {'total_disaster_projects_in_funding': 27, 'sample_disaster_funding': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}], 'total_funding_amount': 1410000}, 'var_functions.query_db:34': [{'total_funding': '1410000'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
