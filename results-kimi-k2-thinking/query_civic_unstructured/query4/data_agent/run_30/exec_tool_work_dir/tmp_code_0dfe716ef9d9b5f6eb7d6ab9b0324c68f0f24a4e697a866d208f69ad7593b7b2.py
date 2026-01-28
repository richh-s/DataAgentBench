code = """import json
import re
from collections import defaultdict

# Load data
civic_docs_path = locals()['var_functions.query_db:5']
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:5']

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project headings - common patterns
    # Pattern 1: Lines that look like project names (often title case, sometimes with year)
    # Pattern 2: Lines ending with "Project" or containing "Improvements", "Repairs", etc.
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and obvious non-project headings
        if not line or line in ['Public Works Commission', 'Agenda Report', 'Public Works', 
                               'Commission Meeting', 'Item', 'To:', 'Prepared by:', 
                               'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:',
                               'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects (Design)',
                               'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
            i += 1
            continue
        
        # Look for project name patterns
        # Pattern: Lines that are mostly uppercase first letters (title case) and contain keywords
        project_keywords = ['Project', 'Improvements', 'Repairs', 'Installation', 'Replacement', 
                           'Upgrade', 'Renovation', 'System', 'Facility', 'Structure', 'Phase', 'Study']
        
        if (line.istitle() or any(keyword in line for keyword in project_keywords)) and len(line) > 10:
            
            # Check if this might be a project name
            project_name = line
            
            # Look ahead for dates and status information
            start_date = None
            end_date = None
            status = None
            project_type = None
            topics = []
            
            j = i + 1
            while j < min(i + 20, len(lines)):  # Look ahead up to 20 lines for project details
                next_line = lines[j].strip()
                
                # Look for dates
                if 'Project Schedule:' in next_line or 'Estimated Schedule:' in next_line or 'Complete' in next_line:
                    # Check following lines for date patterns
                    k = j + 1
                    while k < min(j + 10, len(lines)):
                        schedule_line = lines[k].strip()
                        
                        # Look for date patterns like "2022-Spring", "2022-March", etc.
                        date_patterns = [
                            r'(\d{4}-Spring)',
                            r'(\d{4}-Fall)',
                            r'(\d{4}-Summer)',
                            r'(\d{4}-Winter)',
                            r'(\d{4}-March)',
                            r'(\d{4}-April)',
                            r'(\d{4}-May)',
                            r'(\d{4}-June)',
                            r'(\d{4}-July)',
                            r'(\d{4}-August)',
                            r'(\d{4}-September)',
                            r'(\d{4}-October)',
                            r'(\d{4}-November)',
                            r'(\d{4}-December)',
                            r'(\d{4}-January)',
                            r'(\d{4}-February)'
                        ]
                        
                        for pattern in date_patterns:
                            matches = re.findall(pattern, schedule_line)
                            if matches:
                                for match in matches:
                                    if not start_date:
                                        start_date = match
                                    else:
                                        end_date = match
                        
                        if ':' in schedule_line and not any(x in schedule_line for x in ['Complete', 'Design', 'Construction', 'Advertise', 'Begin']):
                            break
                        k += 1
                
                # Look for status indicators
                if 'Updates:' in next_line:
                    k = j + 1
                    while k < min(j + 5, len(lines)):
                        update_line = lines[k].strip()
                        if 'currently under construction' in update_line.lower():
                            status = 'construction'
                        elif 'completed' in update_line.lower():
                            status = 'completed'
                        elif 'design' in update_line.lower() or 'finalize the design' in update_line.lower():
                            status = 'design'
                        elif 'not started' in update_line.lower():
                            status = 'not started'
                        elif update_line and not update_line.startswith('('):
                            break
                        k += 1
                
                # Determine type based on keywords
                type_keywords = {
                    'capital': ['infrastructure', 'park', 'road', 'bridge', 'drainage', 'storm drain', 
                               'water treatment', 'guardrail', 'median', 'crosswalk', 'skate park', 
                               'playground', 'berms', 'street', 'resurfacing', 'traffic', 'signal'],
                    'disaster': ['FEMA', 'fire', 'woolsey', 'emergency warning', 'siren', 'disaster', 
                               'recovery', 'CalOES', 'CalJPIA']
                }
                
                lower_line = line.lower()
                if any(kw in lower_line for kw in type_keywords['disaster']):
                    project_type = 'disaster'
                elif any(kw in lower_line for kw in type_keywords['capital']):
                    project_type = 'capital'
                
                # Extract topics
                all_keywords = type_keywords['capital'] + type_keywords['disaster']
                for kw in all_keywords:
                    if kw in lower_line and kw not in topics:
                        topics.append(kw)
                
                # Break if we hit another potential project heading or a major section
                if next_line in ['Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 
                               'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects'] or \
                   (k < len(lines) and lines[k].strip() in ['Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']):
                    break
                
                j += 1
            
            # Add project if it has meaningful data
            if project_name and len(project_name) > 5:
                projects.append({
                    'Project_Name': project_name,
                    'st': start_date,
                    'et': end_date,
                    'status': status,
                    'type': project_type,
                    'topic': ', '.join(topics) if topics else None,
                    'source_file': filename
                })
        
        i += 1

# Look for projects with Spring 2022 start date
spring_2022_projects = []
for project in projects:
    if project['st'] and '2022' in project['st']:
        if any(season in project['st'].lower() for season in ['spring', 'march', 'april', 'may']):
            spring_2022_projects.append(project)

print("__RESULT__:")
print(json.dumps(spring_2022_projects, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}}

exec(code, env_args)
