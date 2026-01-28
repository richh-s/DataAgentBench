code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:2']

with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Extract project information from text
all_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    doc_id = doc.get('_id', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns - project names followed by status info
    # Use regex to find project sections
    
    # Split by common project indicators
    project_blocks = re.split(r'\n\s*\n', text)
    
    for block in project_blocks:
        block = block.strip()
        if not block or len(block) < 30:
            continue
        
        # Skip non-project blocks
        if any(skip in block for skip in ['Page', 'Agenda Item', 'Public Works', 'Commission', 'Chair', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION']):
            continue
        
        # Extract lines
        lines = block.split('\n')
        project_name = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Skip detail lines
            if any(indicator in line for indicator in ['Complete', 'Advertise', 'Begin', 'Updates:', 'Project Schedule:', 'Project Description:', 'Project Updates:']):
                continue
            
            # Check if this could be a project name
            if len(line) > 10 and not line.startswith('(') and not line.startswith('•') and not line.startswith('-'):
                # Remove leading numbers/bullets
                clean_line = re.sub(r'^[\d\s\.•-]+', '', line)
                if len(clean_line) > 10:
                    project_name = clean_line
                    break
        
        if project_name:
            project_info = {
                'Project_Name': project_name,
                '_id': doc_id,
                'filename': filename,
                'topic': '',
                'type': '',
                'status': '',
                'st': '',
                'et': ''
            }
            
            # Infer type from name
            if any(keyword in project_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'recovery']):
                project_info['type'] = 'disaster'
            
            # Infer topics
            topics = []
            name_lower = project_name.lower()
            if 'road' in name_lower or 'street' in name_lower:
                topics.append('road')
            if 'park' in name_lower:
                topics.append('park')
            if 'drain' in name_lower or 'storm' in name_lower:
                topics.append('drainage')
            if 'fema' in name_lower:
                topics.append('fema')
            if 'fire' in name_lower:
                topics.append('fire')
            project_info['topic'] = ', '.join(topics)
            
            # Extract status and dates from block
            block_lower = block.lower()
            if 'design' in block_lower:
                project_info['status'] = 'design'
            elif 'construction' in block_lower:
                project_info['status'] = 'construction'
            elif 'not started' in block_lower:
                project_info['status'] = 'not started'
            elif 'completed' in block_lower:
                project_info['status'] = 'completed'
            
            # Extract years
            year_matches = re.findall(r'(20\d{2})', block)
            if year_matches:
                project_info['st'] = year_matches[0]
                project_info['et'] = year_matches[-1]
            
            # Extract seasonal dates
            season_pattern = r'(Spring|Summer|Fall|Winter)\s+(20\d{2})'
            season_matches = re.findall(season_pattern, block)
            if season_matches:
                dates = [f"{year}-{season}" for season, year in season_matches]
                if dates:
                    project_info['st'] = dates[0]
                    project_info['et'] = dates[-1]
            
            all_projects.append(project_info)

print("__RESULT__:")
print(json.dumps({
    "projects": len(all_projects),
    "disaster_projects": [p for p in all_projects if p['type'] == 'disaster'],
    "sample": all_projects[:6]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
