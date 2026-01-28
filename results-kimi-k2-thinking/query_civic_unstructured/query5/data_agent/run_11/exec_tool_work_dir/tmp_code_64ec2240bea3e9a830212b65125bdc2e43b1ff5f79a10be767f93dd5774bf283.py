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

def extract_projects_with_dates(docs):
    projects = []
    
    for doc in docs:
        text = doc.get('text', '')
        doc_lines = text.split('\n')
        
        # Look for disaster/FEMA specific sections
        disaster_section = False
        current_project = None
        
        for i, line in enumerate(doc_lines):
            line = line.strip()
            
            # Detect disaster section headers
            if any(keyword in line for keyword in ['Disaster Recovery Projects', 'FEMA Projects', 'CalOES Projects', 'CalJPIA Projects']):
                disaster_section = True
                continue
            
            # Skip headers and metadata
            if len(line) < 10 or any(skip in line for skip in ['To:', 'Prepared', 'Approved', 'Date:', 'Meeting', 'Subject:', 'Page', 'Agenda']):
                continue
            
            # Look for project names that are likely disaster-related
            # They often include FEMA/CalOES/CalJPIA or are in disaster sections
            if disaster_section and line and not line.startswith('(') and not line.startswith('•'):
                # Check if next line suggests this is a project
                if i + 1 < len(doc_lines):
                    next_line = doc_lines[i + 1].strip()
                    if next_line.startswith('(') or 'Updates:' in next_line:
                        current_project = line
                        
                        # Look for 2022 start date in following lines
                        for j in range(i+1, min(i+15, len(doc_lines))):
                            detail_line = doc_lines[j]
                            
                            # Look for schedule/completion info containing 2022
                            schedule_match = re.search(r'(\d{4})(?:\s*[-–]\s*(Spring|Summer|Fall|Winter|[A-Za-z]+))?', detail_line)
                            if schedule_match:
                                year = int(schedule_match.group(1))
                                if year == 2022:
                                    projects.append({
                                        'Project_Name': current_project,
                                        'start_date': schedule_match.group(0),
                                        'type': 'disaster',
                                        'context': detail_line.strip()
                                    })
                                    break
                        
                        # Also look for lines that mention 2022 explicitly
                        for j in range(i+1, min(i+15, len(doc_lines))):
                            detail_line = doc_lines[j]
                            if '2022' in detail_line:
                                match = re.search(r'(\d{4})(?:\s*[-–]\s*(Spring|Summer|Fall|Winter|[A-Za-z]+))?', detail_line)
                                if match and int(match.group(1)) == 2022:
                                    projects.append({
                                        'Project_Name': current_project,
                                        'start_date': match.group(0),
                                        'type': 'disaster',
                                        'context': detail_line.strip()
                                    })
                                    break
    
    return projects

# Extract projects
disaster_projects_2022 = extract_projects_with_dates(civic_docs)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Filter for disaster projects in funding
funding_disaster_mask = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Fire|Woolsey|Disaster', case=False, na=False)

# Get unique disaster project names from funding
disaster_funding_projects = funding_df[funding_disaster_mask]['Project_Name'].unique()

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_2022_from_docs': len(disaster_projects_2022),
    'sample_projects': disaster_projects_2022[:5],
    'total_disaster_projects_in_funding': len(disaster_funding_projects),
    'sample_funding_disaster': list(disaster_funding_projects)[:10]
}, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:24': {'total_disaster_projects_in_funding': 27, 'sample_disaster_funding': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}], 'total_funding_amount': 1410000}}

exec(code, env_args)
