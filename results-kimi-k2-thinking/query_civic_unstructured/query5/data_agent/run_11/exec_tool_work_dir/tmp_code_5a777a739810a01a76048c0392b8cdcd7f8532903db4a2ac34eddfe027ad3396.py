code = """import json
import pandas as pd
import re

# Load civic documents
civic_file_path = locals()['var_functions.query_db:2']
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file_path = locals()['var_functions.query_db:12']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

def extract_disaster_projects_2022(docs):
    projects = []
    
    for doc in docs:
        text = doc.get('text', '')
        if not any(kw in text for kw in ['FEMA', 'CalOES', 'CalJPIA', 'Disaster Recovery']):
            continue
            
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10:
                continue
            
            # Skip headers/metadata
            if any(marker in line for marker in ['To:', 'Prepared', 'Approved', 'Date:', 'Meeting']):
                continue
            if any(marker in line for marker in ['Subject:', 'RECOMMENDED', 'Page', 'Agenda']):
                continue
            
            # Check if line is likely a project name (not a bullet point, not a header)
            if not line.startswith('(') and not line.startswith('•') and not line.startswith('cid:'):
                # Check if next line suggests it's a project
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line.startswith('(') or 'Updates:' in next_line:
                        # Look for 2022 in following lines
                        found_2022 = False
                        for j in range(i+1, min(i+12, len(lines))):
                            detail = lines[j]
                            if '2022' in detail or re.search(r'\b2022\b', detail):
                                found_2022 = True
                                break
                        
                        if found_2022:
                            # Determine if it's disaster-related based on context or name
                            is_disaster = any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA']) or \
                                         any(keyword in text[max(0, i-200):i+200] for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'Disaster Recovery'])
                            
                            if is_disaster:
                                projects.append(line.strip())
    
    return list(set(projects))

# Extract disaster projects starting in 2022
disaster_projects_2022 = extract_disaster_projects_2022(civic_docs)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Filter for disaster projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Fire', 'Woolsey', 'Disaster']
mask = funding_df['Project_Name'].str.contains('|'.join(disaster_keywords), case=False, na=False)
disaster_funding_df = funding_df[mask].copy()

# Filter for projects that started in 2022 based on document analysis
matching_projects = []
for project_name in disaster_funding_df['Project_Name'].unique():
    # Check if base project name (without suffix) matches any extracted projects
    base_name = project_name.split(' (')[0].strip()
    for extracted_project in disaster_projects_2022:
        if base_name.lower() in extracted_project.lower() or extracted_project.lower() in base_name.lower():
            matching_projects.append(project_name)
            break

# Filter to only matching projects
final_funding = disaster_funding_df[disaster_funding_df['Project_Name'].isin(matching_projects)]

total_funding = int(final_funding['Amount'].sum())
project_count = len(final_funding)

result = {
    'total_disaster_funding_2022': total_funding,
    'number_of_projects': project_count,
    'matching_projects': final_funding[['Project_Name', 'Amount']].head(10).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:24': {'total_disaster_projects_in_funding': 27, 'sample_disaster_funding': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}], 'total_funding_amount': 1410000}}

exec(code, env_args)
