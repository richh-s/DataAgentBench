code = """import json
import pandas as pd

funding_file = locals()['var_functions.query_db:8']
civic_file = locals()['var_functions.query_db:9']

with open(funding_file, 'r') as f:
    funding = json.load(f)
with open(civic_file, 'r') as f:
    civic = json.load(f)

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

spring_projects = []
for doc in civic:
    text = doc['text'].lower()
    has_2022 = '2022' in text
    has_spring = 'spring' in text or 'march' in text or 'april' in text or 'may' in text
    if has_2022 and has_spring:
        for line in doc['text'].split('\n'):
            line = line.strip()
            if len(line) > 10 and not line.startswith('(') and line.isupper() == False:
                if any(word in line for word in ['Project', 'Repair', 'Drainage', 'Road']):
                    spring_projects.append(line)

spring_projects = list(set(spring_projects))

matched = []
total_funding = 0
for project in spring_projects:
    short_name = project.split('(')[0].strip()[:30]
    mask = funding_df['Project_Name'].str.contains(short_name, case=False, na=False)
    matching_rows = funding_df[mask]
    if not matching_rows.empty:
        for _, row in matching_rows.iterrows():
            matched.append({'project': project, 'funding': row['Project_Name'], 'amount': row['Amount']})
            total_funding += row['Amount']

print('__RESULT__:')  
print(json.dumps({'count': len(matched), 'total_funding': int(total_funding)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_docs': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}], 'sample_civic': 9796}, 'var_functions.execute_python:20': {'total_funding_records': 500, 'sample_projects': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': 21000}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': 39000}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': 87000}]}}

exec(code, env_args)
