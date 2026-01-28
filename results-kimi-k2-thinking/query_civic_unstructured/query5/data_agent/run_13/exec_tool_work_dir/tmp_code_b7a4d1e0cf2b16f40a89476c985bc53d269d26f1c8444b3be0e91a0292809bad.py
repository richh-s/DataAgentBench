code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:28']
if isinstance(funding_path, str):
    with open(funding_path, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = locals()['var_functions.query_db:28']

# Load civic documents data
civic_docs_path = locals()['var_functions.query_db:2']
if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:2']

# Step 1: Identify disaster-related projects from funding data
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'warning', 'siren']
funding_disaster_projects = {}

for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if disaster-related
    is_disaster = any(keyword.lower() in project_name.lower() for keyword in disaster_keywords)
    
    if is_disaster:
        # Store by project name for later lookup
        funding_disaster_projects[project_name] = {
            'amount': amount,
            'funding_id': record.get('Funding_ID')
        }

# Step 2: Parse civic documents to find project start dates
disaster_projects_with_dates = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 150:
            continue
        
        # Skip headers/footers and non-project lines
        if any(skip in line for skip in ['Page', 'Agenda', 'Public Works', 'Commission', 'Item', 'To:', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date', 'Subject', 'RECOMMENDED ACTION', 'DISCUSSION', '•', 'cid:']):
            continue
        
        # Check if this line is a project name (look at context)
        # Project names are often followed by Updates:, Schedule: or Project Description:
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if ('Updates:' in next_line or 'Schedule:' in next_line or 'Project Description:' in next_line or 
                next_line.startswith('(') or 'Updates' in line or 'Schedule' in line):
                
                # This might be a project name - check if it matches any disaster project
                for disaster_proj_name in funding_disaster_projects.keys():
                    # Check for exact match or close match
                    if (line == disaster_proj_name or 
                        disaster_proj_name.startswith(line) or 
                        line.startswith(disaster_proj_name.split('(')[0].strip())):
                        
                        current_project = disaster_proj_name
                        break
        
        # If we have a current project, look for start dates in this or next few lines
        if current_project:
            # Look for 2022 in current or next 5 lines
            context = '\n'.join(lines[i:min(len(lines), i + 6)])
            if '2022' in context:
                # Found a disaster project with 2022 date
                start_indicator = ''
                if '2022' in line:
                    start_indicator = line
                else:
                    # Find the specific line with 2022
                    for j in range(i, min(len(lines), i + 6)):
                        if '2022' in lines[j]:
                            start_indicator = lines[j].strip()
                            break
                
                disaster_projects_with_dates.append({
                    'project_name': current_project,
                    'amount': funding_disaster_projects[current_project]['amount'],
                    'start_context': start_indicator,
                    'filename': filename
                })
                current_project = None  # Reset after finding

# Step 3: Sum funding for unique projects
unique_projects = {}
total_funding = 0

for proj in disaster_projects_with_dates:
    proj_name = proj['project_name']
    if proj_name not in unique_projects:
        unique_projects[proj_name] = proj['amount']
        total_funding += proj['amount']

print('__RESULT__')
print(json.dumps({
    'total_disaster_projects_found': len(disaster_projects_with_dates),
    'unique_disaster_projects_2022': len(unique_projects),
    'total_funding_2022': total_funding,
    'project_details': list(unique_projects.keys())[:10]  # Sample
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5}, 'var_functions.execute_python:14': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'civic_docs_full_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'civic_docs_total': 5, 'funding_records_total': 500, 'sample_doc_filename': 'malibucity_agenda_03222023-2060.txt'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
