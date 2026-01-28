code = """import json
import re

# Read civic documents
civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding_file = locals()['var_functions.query_db:6']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Function to extract project information from civic document text
def extract_projects_from_text(text):
    projects = []
    
    # Split by lines to process
    lines = text.split('\n')
    
    current_project = None
    in_disaster_section = False
    
    # Look for patterns that indicate disaster projects
    disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery']
    
    # Also look for project names that contain disaster indicators
    for line in lines:
        line = line.strip()
        
        # Look for project names - typically capitalized and at the start of a line
        # Common pattern is project name followed by updates or schedule
        if line and not line.startswith('(') and not line.startswith('cid:'):
            # Check if this might be a project name
            if (len(line.split()) >= 2 and  # At least 2 words
                (line.istitle() or line.isupper()) and  # Title case or all caps
                not any(keyword in line.lower() for keyword in ['project schedule', 'updates', 'recommended action', 
                                                             'subject', 'to:', 'from:', 'date:', 'meeting date:'])):
                
                project_name = line
                
                # Check if it's disaster-related
                is_disaster = any(indicator in project_name for indicator in disaster_indicators)
                
                # Check for date patterns in nearby lines
                # Look for 2022 in schedule lines
                found_2022_start = False
                
                # Search within a window of lines after the project name
                line_idx = lines.index(line)
                for i in range(line_idx, min(line_idx + 10, len(lines))):
                    schedule_line = lines[i].strip()
                    if ('2022' in schedule_line and 
                        any(time_word in schedule_line.lower() for time_word in ['complete design', 'advertise', 'begin construction', 'start', 'construction', 'complete'])):
                        found_2022_start = True
                        break
                
                if is_disaster and found_2022_start:
                    projects.append({
                        'project_name': project_name,
                        'type': 'disaster',
                        'start_year': '2022'
                    })
    
    return projects

# Extract all projects from all civic documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

print('__RESULT__:')
print(json.dumps({
    'extracted_disaster_projects': all_projects,
    'count': len(all_projects)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
