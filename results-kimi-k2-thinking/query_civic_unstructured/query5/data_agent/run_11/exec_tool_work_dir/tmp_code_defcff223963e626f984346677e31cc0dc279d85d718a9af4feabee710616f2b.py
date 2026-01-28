code = """import json
import re

# Load all civic documents
civic_path = locals()['var_functions.query_db:2']
with open(civic_path, 'r') as f:
    all_docs = json.load(f)

# Load all funding data
funding_path = locals()['var_functions.query_db:12']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# First, identify disaster projects from civic documents that mention 2022
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster Recovery']
projects_2022 = set()

for doc in all_docs:
    text = doc.get('text', '')
    
    # Check if document mentions disaster keywords and 2022
    has_disaster = any(keyword in text for keyword in disaster_keywords)
    has_2022 = '2022' in text
    
    if has_disaster and has_2022:
        # Extract text lines to find project names
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip empty lines and metadata
            if not line or len(line) < 10:
                continue
            if any(skip in line for skip in ['To:', 'Prepared', 'Approved', 'Date:', 'Page', 'Agenda', 'Subject:', 'RECOMMENDED', 'DISCUSSION']):
                continue
            
            # Look for project names (not bullet points)
            if not line.startswith('(') and not line.startswith('•') and not line.startswith('cid:'):
                # Check if this looks like a project name
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line.startswith('(') or 'Updates:' in next_line or 'Project Schedule:' in next_line:
                        # Check if disaster-related
                        context = ' '.join(lines[max(0,i-3):i+10])
                        if any(keyword in context for keyword in disaster_keywords):
                            # Check if 2022 appears in context
                            if '2022' in context:
                                projects_2022.add(line.strip())

# Now get all disaster funding records
import pandas as pd
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Filter for disaster projects
disaster_mask = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)
disaster_funding_df = funding_df[disaster_mask]

# Match with projects that started in 2022
matched_projects = []
for fund_project in disaster_funding_df['Project_Name'].unique():
    base_name = fund_project.split(' (')[0].strip()
    # Check if any extracted 2022 project matches this
    for proj_2022 in projects_2022:
        if base_name.lower() in proj_2022.lower() or proj_2022.lower() in base_name.lower():
            matched_projects.append(fund_project)
            break

# Filter to only matched projects
final_funding_df = disaster_funding_df[disaster_funding_df['Project_Name'].isin(matched_projects)]

# Calculate totals
total_funding = int(final_funding_df['Amount'].sum())
total_projects = len(final_funding_df)

# Get sample projects
sample_projects = final_funding_df[['Project_Name', 'Amount']].head().to_dict('records')

result = {
    'total_funding_2022': total_funding,
    'number_of_projects': total_projects,
    'sample_projects': sample_projects
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:24': {'total_disaster_projects_in_funding': 27, 'sample_disaster_funding': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}], 'total_funding_amount': 1410000}, 'var_functions.query_db:34': [{'total_funding': '1410000'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:48': [], 'var_functions.query_db:50': [], 'var_functions.query_db:52': [{'total_funding': 'None'}]}

exec(code, env_args)
