code = """import json
import pandas as pd

# Load all funding data
funding_path = locals()['var_functions.query_db:12']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Filter for disaster-related projects
# Based on the hints, disaster projects have these keywords
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Fire', 'Disaster']
disaster_mask = funding_df['Project_Name'].str.contains('|'.join(disaster_keywords), case=False, na=False)

disaster_funding = funding_df[disaster_mask]

# Calculate totals
total_funding = int(disaster_funding['Amount'].sum())
project_count = len(disaster_funding)

# Get list of all disaster projects
disaster_projects_list = disaster_funding[['Project_Name', 'Amount']].to_dict('records')

result = {
    'total_disaster_funding_all': total_funding,
    'total_projects': project_count,
    'all_disaster_projects': disaster_projects_list
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:24': {'total_disaster_projects_in_funding': 27, 'sample_disaster_funding': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}], 'total_funding_amount': 1410000}, 'var_functions.query_db:34': [{'total_funding': '1410000'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:48': [], 'var_functions.query_db:50': [], 'var_functions.query_db:52': [{'total_funding': 'None'}], 'var_functions.query_db:56': [{'total_funding': 'None'}], 'var_functions.execute_python:58': {'total_funding_2022': 112000, 'project_count': 2, 'projects': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': 18000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': 94000}]}, 'var_functions.query_db:62': [{'total_disaster_funding': '1410000'}]}

exec(code, env_args)
