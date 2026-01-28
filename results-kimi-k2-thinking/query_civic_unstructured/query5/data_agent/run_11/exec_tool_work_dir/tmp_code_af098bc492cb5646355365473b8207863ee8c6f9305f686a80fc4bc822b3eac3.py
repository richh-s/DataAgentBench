code = """import json, pandas as pd, re

civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:12']

with open(civic_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

# Extract all funding records that are disaster-related
disaster_terms = ['FEMA', 'CalOES', 'CalJPIA']

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Filter for disaster projects
disaster_mask = funding_df['Project_Name'].str.contains('|'.join(disaster_terms), case=False, na=False)
disaster_funding = funding_df[disaster_mask]

# Now check which of these appeared in 2022 in the civic documents
# Extract project names from documents that mention disaster keywords
projects_2022 = []
for doc in civic_docs:
    if any(term in doc['text'] for term in disaster_terms):
        text = doc['text']
        # Find all occurrences of potential disaster project names
        # They often have specific patterns
        for term in disaster_terms:
            if term in text:
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if term in line and len(line.strip()) > 10 and not line.startswith('(') and not line.startswith('•'):
                        if '2022' in ''.join(lines[max(0,i-5):i+10]):
                            projects_2022.append(line.strip())

# Filter disaster funding to only projects that started in 2022
final_projects_2022 = []
for project_name in disaster_funding['Project_Name'].unique():
    base_name = project_name.split(' (')[0].strip()
    # Check if base name appears in 2022 projects
    for p2022 in projects_2022:
        if base_name.lower() in p2022.lower() or p2022.lower() in base_name.lower():
            final_projects_2022.append(project_name)
            break

# Get final funding amounts
final_funding_df = disaster_funding[disaster_funding['Project_Name'].isin(final_projects_2022)]
total_amount = int(final_funding_df['Amount'].sum())
project_count = len(final_funding_df)

print('__RESULT__:')
print(json.dumps({
    'total_funding_2022': total_amount,
    'project_count': project_count,
    'top_projects': final_funding_df[['Project_Name','Amount']].head().to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:24': {'total_disaster_projects_in_funding': 27, 'sample_disaster_funding': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}], 'total_funding_amount': 1410000}}

exec(code, env_args)
