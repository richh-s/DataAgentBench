code = """import json
import re
import pandas as pd

# Load all data files
funding_path = locals()['var_functions.query_db:12']
all_docs_path = locals()['var_functions.query_db:2']

with open(funding_path) as f:
    funding = json.load(f)
with open(all_docs_path) as f:
    all_docs = json.load(f)

# Get ALL disaster funding
funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)
all_disaster_funding = funding_df[funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)]

# Extract all disaster project names from documents that reference 2022
projects_2022_names = set()
for doc in all_docs:
    text = doc.get('text', '')
    if '2022' in text and ('FEMA' in text or 'CalOES' in text or 'CalJPIA' in text):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10: 
                continue
            if any(x in line for x in ['To:', 'Prepared', 'Approved', 'Date', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Page', 'Agenda', 'Commission', 'Chair']):
                continue
            
            if not line.startswith('(') and not line.startswith('•') and not line.startswith('cid:'):
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line.startswith('(') or 'Updates:' in next_line:
                        context = ' '.join(lines[max(0,i-2):i+3])
                        if (any(kw in context for kw in ['FEMA', 'CalOES', 'CalJPIA']) and 
                            '2022' in context[:200]):  # 2022 near this project
                            projects_2022_names.add(line.strip())

# Match funding records with extracted project names
matched_funding = []
for fund_record in all_disaster_funding.to_dict('records'):
    fund_name = fund_record['Project_Name']
    base_fund_name = fund_name.split(' (')[0].strip()
    
    # Check for direct match or partial match
    for proj_name in projects_2022_names:
        proj_base = proj_name.split(' (')[0].strip()
        # Check if either base name contains the other (partial match)
        if (proj_base.lower() in base_fund_name.lower() or 
            base_fund_name.lower() in proj_base.lower() or
            any(word in base_fund_name.lower() and len(word) > 5 for word in proj_base.lower().split())):
            matched_funding.append(fund_record)
            break

# Also include any funding records that explicitly contain 2022
explicit_2022 = all_disaster_funding[all_disaster_funding['Project_Name'].str.contains('2022', na=False)]
for rec in explicit_2022.to_dict('records'):
    if rec not in matched_funding:
        matched_funding.append(rec)

# Create final dataframe
final_df = pd.DataFrame(matched_funding).drop_duplicates()

# Calculate total
if not final_df.empty:
    total_funding_2022 = int(final_df['Amount'].sum())
    project_count = len(final_df)
    projects_list = final_df[['Project_Name', 'Amount']].to_dict('records')
else:
    total_funding_2022 = 0
    project_count = 0
    projects_list = []

result = {
    'total_disaster_funding_2022': total_funding_2022,
    'number_of_projects': project_count,
    'sample_projects': projects_list[:10]
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:24': {'total_disaster_projects_in_funding': 27, 'sample_disaster_funding': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}], 'total_funding_amount': 1410000}, 'var_functions.query_db:34': [{'total_funding': '1410000'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:48': [], 'var_functions.query_db:50': [], 'var_functions.query_db:52': [{'total_funding': 'None'}], 'var_functions.query_db:56': [{'total_funding': 'None'}], 'var_functions.execute_python:58': {'total_funding_2022': 112000, 'project_count': 2, 'projects': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': 18000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': 94000}]}}

exec(code, env_args)
