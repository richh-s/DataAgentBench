code = """import json
import re
import pandas as pd

# Load the full civic documents
civic_file = locals()['var_functions.query_db:9']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Function to extract projects with Spring 2022 start dates
spring_2022_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip headers, bullets, and irrelevant lines
        if (not line or 
            line.startswith('(') or 
            line.startswith('•') or 
            line.startswith('□') or
            line.startswith('cid:') or
            line.isupper() or
            len(line) < 5 or
            'Prepared by:' in line or
            'Subject:' in line or
            'To:' in line or
            'Page' in line):
            continue
        
        # Look for potential project names (contain keywords, not just headers)
        project_keywords = ['Project', 'Repair', 'Drainage', 'Resurfacing', 'Replacement', 'Bridge', 'Culvert', 'Road', 'Street', 'Park', 'Improvement']
        has_project_keyword = any(keyword in line for keyword in project_keywords)
        
        # Avoid capturing section headers
        if has_project_keyword and len(line) > 10 and not line.endswith(':'):
            # Check if this line looks like a project name
            if not any(header in line for header in ['Agenda', 'Commission', 'Meeting', 'Status Report', 'Capital Improvement', 'Design)', 'Construction)']):
                current_project = line
                
                # Look ahead for Spring 2022 dates
                context_start = max(0, i-2)
                context_end = min(len(lines), i+6)
                context = ' '.join(lines[context_start:context_end])
                
                # Check for Spring 2022 patterns
                spring_2022_patterns = [
                    r'2022[-\s]Spring',
                    r'Spring[-\s]2022',
                    r'2022[-\s][Mm]arch',
                    r'[Mm]arch[-\s]2022',
                    r'2022[-\s][Aa]pril',
                    r'[Aa]pril[-\s]2022',
                    r'2022[-\s][Mm]ay',
                    r'[Mm]ay[-\s]2022'
                ]
                
                # Check for project schedule dates in Spring 2022
                schedule_patterns = [
                    r'[Cc]omplete [Dd]esign:[^\n]*?(Spring|March|April|May)[^\n]*?2022',
                    r'[Aa]dvertise:[^\n]*?(Spring|March|April|May)[^\n]*?2022',
                    r'[Bb]egin [Cc]onstruction:[^\n]*?(Spring|March|April|May)[^\n]*?2022'
                ]
                
                has_spring_2022 = any(re.search(pattern, context, re.IGNORECASE) for pattern in spring_2022_patterns)
                has_schedule_spring_2022 = any(re.search(pattern, context, re.IGNORECASE) for pattern in schedule_patterns)
                
                if has_spring_2022 or has_schedule_spring_2022:
                    spring_2022_projects.append(current_project)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

print('__RESULT__:')
print(json.dumps({
    'spring_2022_projects': spring_2022_projects,
    'count': len(spring_2022_projects)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_docs': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}], 'sample_civic': 9796}, 'var_functions.execute_python:20': {'total_funding_records': 500, 'sample_projects': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': 21000}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': 39000}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': 87000}]}}

exec(code, env_args)
