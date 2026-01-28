code = """import json, re, pandas as pd

# Load all data in a simpler approach
funding_path = locals()['var_functions.query_db:12']
with open(funding_path) as f:
    funding = json.load(f)

# Filter for disaster projects
funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

disaster_mask = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)
disaster_funding = funding_df[disaster_mask]

# Based on the civic documents we saw, project names often include year info
# or the document references the year in project descriptions

# Check if any disaster projects have 2022 in their name
mask_2022_in_name = disaster_funding['Project_Name'].str.contains('2022', na=False)
projects_with_2022_in_name = disaster_funding[mask_2022_in_name]

# Also try matching base project names with common 2022 disaster projects
# These are likely candidates based on the document we saw
candidates_2022 = [
    'Clover Heights Storm Drainage Improvements',
    'Latigo Canyon Road Retaining Wall Repair Project',
    'Encinal Canyon Road Drainage Improvements'
]

candidate_mask = disaster_funding['Project_Name'].apply(
    lambda x: any(cand.lower() in x.lower() for cand in candidates_2022)
)
candidate_projects = disaster_funding[candidate_mask]

# Combine
all_2022_candidate_projects = pd.concat([projects_with_2022_in_name, candidate_projects]).drop_duplicates()

total_funding = int(all_2022_candidate_projects['Amount'].sum())
project_count = len(all_2022_candidate_projects)

result = {
    'total_funding_2022': total_funding,
    'project_count': project_count,
    'projects': all_2022_candidate_projects[['Project_Name', 'Amount']].head(10).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:24': {'total_disaster_projects_in_funding': 27, 'sample_disaster_funding': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}], 'total_funding_amount': 1410000}, 'var_functions.query_db:34': [{'total_funding': '1410000'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:48': [], 'var_functions.query_db:50': [], 'var_functions.query_db:52': [{'total_funding': 'None'}], 'var_functions.query_db:56': [{'total_funding': 'None'}]}

exec(code, env_args)
