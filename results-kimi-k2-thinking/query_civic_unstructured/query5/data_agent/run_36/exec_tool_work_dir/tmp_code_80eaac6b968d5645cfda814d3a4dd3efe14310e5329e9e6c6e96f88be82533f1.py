code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

all_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Use regex to find project names and their information
    # Look for patterns that indicate project names
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and common header/footer content
        if not line or len(line) < 5:
            continue
        
        if any(pattern in line for pattern in ['Page', 'Agenda Item', 'Public Works', 'Commission', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION:']):
            continue
        
        # Try to identify project names (lines that aren't detail lines)
        detail_indicators = [
            'Complete', 'Advertise', 'Begin', 'Updates:', 'Project Schedule:',
            'Project Description:', 'Project Updates:', 'cid:', '•', '-'
        ]
        
        if not any(indicator in line for indicator in detail_indicators):
            if len(line) > 10 and (line == line.upper() or (not line.startswith(' ') and not line.startswith('\t'))):
                if current_project:
                    project_info['Project_Name'] = current_project
                    all_projects.append(project_info)
                
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
                
                # Infer type from project name
                if any(keyword in line.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'recovery']):
                    project_info['type'] = 'disaster'
                
                # Infer topics
                topics = []
                if 'road' in line.lower() or 'street' in line.lower():
                    topics.append('road')
                if 'park' in line.lower():
                    topics.append('park')
                if 'drain' in line.lower() or 'storm' in line.lower():
                    topics.append('drainage')
                if 'fema' in line.lower():
                    topics.append('fema')
                if 'fire' in line.lower():
                    topics.append('fire')
                
                project_info['topic'] = ', '.join(topics)
                
                continue
        
        if current_project:
            # Extract status and dates
            if 'design' in line.lower():
                project_info['status'] = 'design'
            elif 'construction' in line.lower():
                project_info['status'] = 'construction'
            elif 'not started' in line.lower():
                project_info['status'] = 'not started'
            elif 'completed' in line.lower():
                project_info['status'] = 'completed'
            
            # Extract years
            year_match = re.search(r'(20\d{2})', line)
            if year_match:
                year = year_match.group(1)
                if not project_info['st']:
                    project_info['st'] = year
                project_info['et'] = year
    
    if current_project:
        project_info['Project_Name'] = current_project
        all_projects.append(project_info)

print("__RESULT__:")
print(json.dumps({
    "projects_extracted": len(all_projects),
    "sample": all_projects[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
