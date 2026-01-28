code = """import json
import os
import re
import pandas as pd
from collections import defaultdict

# Load funding data
funding_file = locals()['var_functions.query_db:8']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:9']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)
# Convert amount to numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Function to extract project information from text
def extract_projects_from_text(text):
    projects = []
    
    # Find project sections - look for project names followed by updates/schedule
    # Common patterns in the text
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically title case, not bullet points)
        # Skip empty lines, bullets, and common headers
        if (line and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('-') and 
            not line.startswith('□') and 
            not line.startswith('cid:') and
            line.upper() != line and  # Skip all caps headers
            len(line.split()) > 2 and  # At least 3 words
            not any(x in line.lower() for x in ['prepared by', 'approved by', 'subject:', 'to:', 'date', 'meeting', 'agenda', 'item', 'public works'])):
            
            # Check if this looks like a project name (ends with Project or contains key terms)
            if (line.endswith('Project') or 
                any(keyword in line for keyword in ['Improvement', 'Repair', 'Drainage', 'Resurfacing', 'Replacement', 'Bridge', 'Culvert', 'Road', 'Street', 'Park']) or
                '2022' in line or '2023' in line):
                
                # Save previous project if exists
                if current_project and project_info:
                    projects.append({
                        'Project_Name': current_project.strip(),
                        'info': project_info
                    })
                
                current_project = line
                project_info = {'text': ''}
        
        # If we have a current project, accumulate its text
        elif current_project:
            project_info['text'] += line + ' '
            
            # Look for dates in the text
            if 'Complete Design:' in line or 'Advertise:' in line or 'Begin Construction:' in line:
                if 'Complete Design:' in line and '2022' in line:
                    project_info['start_date'] = line.split('Complete Design:')[1].strip()
                elif 'Advertise:' in line and '2022' in line:
                    project_info['start_date'] = line.split('Advertise:')[1].strip()
                elif 'Begin Construction:' in line and '2022' in line:
                    project_info['start_date'] = line.split('Begin Construction:')[1].strip()
    
    # Add the last project
    if current_project and project_info:
        projects.append({
            'Project_Name': current_project.strip(),
            'info': project_info
        })
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

# Filter for Spring 2022 projects
spring_2022_projects = []

for project in all_projects:
    text_lower = project['info']['text'].lower()
    
    # Check for Spring 2022 indicators
    spring_indicators = [
        '2022-spring',
        '2022-march',
        '2022-april', 
        '2022-may',
        'spring 2022',
        'march 2022',
        'april 2022',
        'may 2022'
    ]
    
    has_spring_2022 = any(indicator in text_lower for indicator in spring_indicators)
    
    # Also check start dates in project info
    start_date = project['info'].get('start_date', '')
    if start_date and '2022' in start_date:
        has_spring_2022 = True
    
    if has_spring_2022:
        # Determine project type based on name and content
        project_name_lower = project['Project_Name'].lower()
        
        project_type = 'capital'  # default
        if any(x in project_name_lower for x in ['fema', 'disaster', 'recovery', 'fire']):
            project_type = 'disaster'
        elif any(x in project_name_lower for x in ['park', 'road', 'drainage', 'bridge', 'culvert', 'street']):
            project_type = 'capital'
        
        # Determine status
        status = 'not started'
        if 'complete design' in text_lower:
            status = 'design'
        if 'construction' in text_lower and ('completed' in text_lower or 'complete' in text_lower):
            status = 'completed'
            
        # Extract topics
        topics = []
        for topic_keyword in ['park', 'road', 'fema', 'drainage', 'bridge', 'culvert', 'street', 'fire', 'emergency', 'storm', 'repair', 'improvement', 'replacement']:
            if topic_keyword in project_name_lower or topic_keyword in text_lower:
                topics.append(topic_keyword)
        
        spring_2022_projects.append({
            'Project_Name': project['Project_Name'],
            'type': project_type,
            'status': status,
            'topics': ','.join(topics)
        })

# Create DataFrame of Spring 2022 projects
spring_df = pd.DataFrame(spring_2022_projects)

print('__RESULT__:')
print(json.dumps({
    'spring_2022_project_count': len(spring_df),
    'projects': spring_df.to_dict('records')[:10] if not spring_df.empty else []
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_docs': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}], 'sample_civic': 9796}}

exec(code, env_args)
