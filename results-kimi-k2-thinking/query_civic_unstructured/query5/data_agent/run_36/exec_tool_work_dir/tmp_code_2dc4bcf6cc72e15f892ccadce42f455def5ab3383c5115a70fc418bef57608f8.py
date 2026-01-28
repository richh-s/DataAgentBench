code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

all_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split by project sections (look for patterns like project names followed by updates/schedule)
    # Look for lines that look like project names (title case, followed by status/category)
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Skip header/footer lines
        if any(skip in line for skip in ['Page ', 'Agenda Item', 'Public Works', 'Commission', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
            continue
            
        # Look for project status categories
        if any(category in line for category in ['Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']):
            continue
            
        # Check if this might be a project name (not a detail line)
        # Project names typically:
        # - Start with capital letters
        # - Don't start with bullet points or special markers
        # - Are followed by project details
        if (len(line) > 10 and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('cid:') and
            not line.startswith('Updates:') and
            not line.startswith('Project Schedule:') and
            not line.startswith('Complete') and
            not line.startswith('Advertise:') and
            not line.startswith('Begin') and
            'Project Description:' not in line):
            
            # Save previous project if exists
            if current_project and project_info:
                project_info['Project_Name'] = current_project
                all_projects.append(project_info)
                
            # Start new project
            current_project = line
            project_info = {
                '_id': doc['_id'],
                'filename': filename,
                'topic': '',
                'type': '',
                'status': '',
                'st': '',
                'et': ''
            }
            
            # Try to infer type from name
            if any(keyword in line.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'recovery']):
                project_info['type'] = 'disaster'
            elif any(keyword in line.lower() for keyword in ['street', 'road', 'park', 'drainage', 'sewer', 'bridge', 'sidewalk', 'traffic', 'signal', 'infrastructure']):
                project_info['type'] = 'capital'
                
            # Try to infer topics
            topics = []
            if 'road' in line.lower() or 'street' in line.lower():
                topics.append('road')
            if 'park' in line.lower():
                topics.append('park')
            if 'drain' in line.lower() or 'drainage' in line.lower() or 'storm' in line.lower():
                topics.append('drainage')
            if 'fema' in line.lower():
                topics.append('fema')
            if 'fire' in line.lower():
                topics.append('fire')
            if 'bridge' in line.lower():
                topics.append('bridge')
            if 'guardrail' in line.lower():
                topics.append('guardrail')
                
            project_info['topic'] = ', '.join(topics)
            continue
            
        # Look for status and date information
        if current_project:
            line_lower = line.lower()
            if any(status in line_lower for status in ['design', 'construction', 'not started', 'completed']):
                if 'design' in line_lower:
                    project_info['status'] = 'design'
                elif 'construction' in line_lower:
                    project_info['status'] = 'construction'
                elif 'not started' in line_lower:
                    project_info['status'] = 'not started'
                elif 'completed' in line_lower:
                    project_info['status'] = 'completed'
                    
            # Look for dates (2022, 2023, etc.)
            year_match = re.search(r'(20\d{2})', line)
            if year_match:
                year = year_match.group(1)
                if not project_info['st']:
                    project_info['st'] = year
                project_info['et'] = year
                
            # Look for seasonal dates
            if any(season in line for season in ['Spring', 'Summer', 'Fall', 'Winter']):
                year_match = re.search(r'(20\d{2})', line)
                if year_match:
                    year = year_match.group(1)
                    season = re.search(r'(Spring|Summer|Fall|Winter)', line).group(1)
                    date_str = f"{year}-{season}"
                    if not project_info['st']:
                        project_info['st'] = date_str
                    project_info['et'] = date_str
    
    # Add last project
    if current_project and project_info:
        project_info['Project_Name'] = current_project
        all_projects.append(project_info)

print("__RESULT__:")
print(json.dumps({
    "total_projects_extracted": len(all_projects),
    "sample_projects": all_projects[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
