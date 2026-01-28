code = """import json
import pandas as pd

# Load data
funding_file = locals()['var_functions.query_db:8']
civic_file = locals()['var_functions.query_db:9']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract projects starting in Spring 2022 from civic documents
spring_2022_project_names = []

for doc in civic_docs:
    text = doc['text']
    # Look for Spring 2022 patterns more broadly
    if '2022' in text and ('Spring' in text or 'March' in text or 'April' in text or 'May' in text):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Find lines that look like project names (contain keywords, not headers)
            if any(keyword in line for keyword in ['Project', 'Repair', 'Drainage', 'Improvement', 'Replacement']):
                if len(line) > 10 and not line.startswith('(') and not line.isupper():
                    spring_2022_project_names.append(line)

# Remove duplicates
spring_2022_project_names = list(set(spring_2022_project_names))

# Match with funding data - use partial matching since names might not be exact
matched_projects = []
total_funding = 0

for project_name in spring_2022_project_names:
    # Look for exact or close matches in funding data
    matches = funding_df[funding_df['Project_Name'].str.contains(project_name.split('(')[0].strip()[:30], case=False, na=False)]
    
    if not matches.empty:
        for _, match in matches.iterrows():
            matched_projects.append({
                'Project_Name': project_name,
                'Funding_Project_Name': match['Project_Name'],
                'Amount': match['Amount']
            })
            total_funding += match['Amount']
    else:
        # Try reverse - see if project name contains funding project name
        for _, funding_row in funding_df.iterrows():
            if funding_row['Project_Name'] in project_name:
                matched_projects.append({
                    'Project_Name': project_name,
                    'Funding_Project_Name': funding_row['Project_Name'],
                    'Amount': funding_row['Amount']
                })
                total_funding += funding_row['Amount']
                break

print('__RESULT__:')
print(json.dumps({
    'spring_2022_projects': spring_2022_project_names,
    'matched_projects': matched_projects,
    'total_projects': len(matched_projects),
    'total_funding': int(total_funding)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_docs': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}], 'sample_civic': 9796}, 'var_functions.execute_python:20': {'total_funding_records': 500, 'sample_projects': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': 21000}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': 39000}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': 87000}]}}

exec(code, env_args)
