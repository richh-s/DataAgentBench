code = """# Extract project information from civic documents
import json
import re
import pandas as pd

# Load the full dataset
with open('file_storage/functions.query_db:10.json', 'r') as f:
    civic_docs = json.load(f)

# Function to extract project information from text
def extract_projects_from_text(text, doc_id, filename):
    projects = []
    
    # Look for capital and disaster project sections
    # Pattern 1: Projects with year in name (e.g., "2022 Morning View Resurfacing")
    year_project_pattern = r'(\d{4})\s+([A-Z][a-zA-Z\s&\-]+?)(?=\n|$|\()'
    
    # Pattern 2: Project descriptions with schedule info
    project_section_pattern = r'([A-Z][a-zA-Z\s&\-]+?(?:\(FEMA\s+Project\)|\(CalOES\s+Project\)|\(CalJPIA\s+Project\)|\(FEMA\/CalOES\s+Project\))?)\s+(?:Updates:|Project\s+Schedule:|Estimated\s+Schedule:)(.*?)(?=\n\s*\n|\Z)'

    # Pattern 3: Simple project names in lists
    simple_project_pattern = r'^\s*([A-Z][a-zA-Z\s&\-/]+?(?:\(FEMA\s+Project\)|\(CalOES\s+Project\)|\(CalJPIA\s+Project\)|\(FEMA\/CalOES\s+Project\))?)\s*$'
    
    text_lines = text.split('\n')
    
    for i, line in enumerate(text_lines):
        line = line.strip()
        
        # Skip empty lines and common headers
        if not line or 'Page ' in line or 'Agenda Item' in line or line.isupper() and len(line) < 50:
            continue
            
        # Look for project names (usually title case, not all caps)
        if (len(line) > 10 and 
            not line.isupper() and 
            not line.startswith('(') and
            not any(keyword in line for keyword in ['To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects', 'Disaster Recovery Projects'])):
            
            # Check if this looks like a project name
            if re.match(r'^[A-Z][a-zA-Z\s&\-/,]+$', line) or \
               re.match(r'^[A-Z][a-zA-Z\s&\-/,]+\s+\(FEMA\s+[^)]+\)$', line) or \
               re.match(r'^\d{4}\s+[A-Z][a-zA-Z\s&\-/]+$', line):
                
                # Check if next lines have schedule info
                schedule = ''
                status = 'not started'
                start_time = ''
                end_time = ''
                topics = []
                project_type = 'capital'  # default
                
                # Look ahead for schedule/project info
                look_ahead = min(i + 10, len(text_lines))
                for j in range(i+1, look_ahead):
                    next_line = text_lines[j].strip()
                    
                    if 'Project Schedule:' in next_line or 'Estimated Schedule:' in next_line:
                        # Found schedule info, collect the following schedule details
                        schedule_start = j + 1
                        for k in range(schedule_start, min(schedule_start + 5, len(text_lines))):
                            schedule_line = text_lines[k].strip()
                            if schedule_line and ':' in schedule_line:
                                schedule += schedule_line + ' | '
                                if 'Begin' in schedule_line or 'Complete Design' in schedule_line:
                                    # Extract dates
                                    date_match = re.search(r'(Spring|Summer|Fall|Winter)\s+(\d{4})', schedule_line)
                                    if date_match:
                                        if 'Begin' in schedule_line or 'Complete Design' in schedule_line:
                                            start_time = f"{date_match.group(2)}-{date_match.group(1)}"
                                        if 'Complete' in schedule_line or 'Begin Construction' in schedule_line:
                                            end_time = f"{date_match.group(2)}-{date_match.group(1)}"
                        break
                    
                    elif 'Updates:' in next_line:
                        # Look for status information
                        update_start = j + 1
                        for k in range(update_start, min(update_start + 5, len(text_lines))):
                            update_line = text_lines[k].strip()
                            if update_line:
                                if any(phrase in update_line for phrase in ['under construction', 'construction was completed', 'construction completed']):
                                    if 'under construction' in update_line:
                                        status = 'in_progress'
                                    elif 'completed' in update_line:
                                        status = 'completed'
                                break
                        break
                
                # Determine project type (capital vs disaster)
                if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency']):
                    project_type = 'disaster'
                elif any(keyword in line for keyword in ['park', 'road', 'street', 'bridge', 'drainage', 'storm', 'water', 'traffic', 'facility', 'playground']):
                    project_type = 'capital'
                
                # Extract topics
                if any(keyword in line.lower() for keyword in ['park']):
                    topics.append('park')
                if any(keyword in line.lower() for keyword in ['road', 'street', 'highway']):
                    topics.append('road')
                if 'FEMA' in line:
                    topics.append('FEMA')
                if any(keyword in line.lower() for keyword in ['drainage', 'storm drain']):
                    topics.append('drainage')
                if 'emergency' in line.lower():
                    topics.append('emergency warning')
                
                projects.append({
                    'Project_Name': line,
                    'topic': ','.join(topics),
                    'type': project_type,
                    'status': status,
                    'st': start_time,
                    'et': end_time,
                    'doc_id': doc_id,
                    'filename': filename
                })
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'], doc['_id'], doc['filename'])
    all_projects.extend(projects)

projects_df = pd.DataFrame(all_projects)

print('__RESULT__:')
print(json.dumps({
    "total_projects_extracted": len(projects_df),
    "sample_projects": projects_df.head(10).to_dict('records'),
    "unique_project_names": len(projects_df['Project_Name'].unique()),
    "projects_with_dates": len(projects_df[projects_df['st'] != '']),
    "all_start_dates": projects_df[projects_df['st'] != '']['st'].tolist()[:20]
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['civic_docs'], 'var_functions.execute_python:16': {'funding_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:6.json', 'civic_result_type': "<class 'str'>", 'civic_result_preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'funding_records': 500, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
