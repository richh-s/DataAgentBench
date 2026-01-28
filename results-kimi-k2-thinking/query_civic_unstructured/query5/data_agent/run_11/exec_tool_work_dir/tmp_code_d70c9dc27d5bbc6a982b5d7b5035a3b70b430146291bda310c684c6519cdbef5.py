code = """import json
import re

# Load disaster documents
docs_path = locals()['var_functions.query_db:42']
with open(docs_path, 'r') as f:
    docs_2022 = json.load(f)

# Load funding data
funding_path = locals()['var_functions.query_db:12']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Find all disaster-related project names in 2022 documents
found_projects = set()
for doc in docs_2022:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10: 
            continue
        
        # Skip metadata lines
        if any(x in line for x in ['To:', 'Prepared', 'Approved', 'Date:', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Page']):
            continue
        
        # If line doesn't start with bullet and next line has project indicators
        if not line.startswith('(') and not line.startswith('•') and not line.startswith('cid:'):
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith('(') or 'Updates:' in next_line:
                    # Check if disaster-related and 2022 appears nearby
                    context = ' '.join(lines[max(0,i-3):i+5])
                    if ('FEMA' in context or 'CalOES' in context or 'CalJPIA' in context) and '2022' in context:
                        found_projects.add(line)

# Create funding dataframe
import pandas as pd
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Filter disaster funding
disaster_funding = funding_df[funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)]

# Match with extracted projects
included_projects = []
for fund_project in disaster_funding['Project_Name'].unique():
    base = fund_project.split(' (')[0]
    for found in found_projects:
        if base.lower() in found.lower() or found.lower() in base.lower():
            included_projects.append(fund_project)

# Calculate total funding for matched projects
valid_mask = disaster_funding['Project_Name'].isin(included_projects) | disaster_funding['Project_Name'].str.contains('2022', na=False)
final_funding = disaster_funding[valid_mask]

total = int(final_funding['Amount'].sum())
count = len(final_funding)

result = {
    'total_funding_2022': total,
    'project_count': count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:24': {'total_disaster_projects_in_funding': 27, 'sample_disaster_funding': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}], 'total_funding_amount': 1410000}, 'var_functions.query_db:34': [{'total_funding': '1410000'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
