code = """import json
import re

# Access the civic documents data
civic_docs_variable = var_functions.query_db:5
civic_docs_data = civic_docs_variable

# If it's a file path, load the data
if isinstance(civic_docs_data, str) and civic_docs_data.endswith('.json'):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

# Access the funding data
funding_variable = var_functions.query_db:6
funding_data = funding_variable

# If it's a file path, load the data
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Extract projects from civic documents
def extract_projects_from_text(text):
    projects = []
    
    # Look for project mentions with status indicators
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically start with capital letters and are not bullet points)
        if len(line) > 5 and not line.startswith('(') and not line.startswith('cid') and not line.startswith('Page'):
            # Skip headers and common non-project lines
            skip_patterns = ['RECOMMENDED ACTION', 'DISCUSSION', 'Subject', 'Prepared by', 'Approved by',
                           'To:', 'From:', 'Date:', 'Item', 'Public Works', 'Commission', 'Agenda']
            
            should_skip = False
            for pattern in skip_patterns:
                if pattern in line:
                    should_skip = True
                    break
            
            if should_skip:
                continue
            
            # Check if next lines contain project indicators
            next_text = '\n'.join(lines[i:min(i+20, len(lines))])
            
            # Determine status
            status = None
            if 'construction was completed' in next_text.lower() or 'completed' in next_text.lower():
                status = 'completed'
            elif 'design' in next_text.lower():
                status = 'design'
            elif 'not started' in next_text.lower():
                status = 'not started'
            
            # Check if it's a park-related project
            is_park = 'park' in line.lower()
            
            # Check if completed in 2022
            completed_2022 = False
            if status == 'completed':
                if '2022' in next_text.lower():
                    # Look for completion dates
                    date_patterns = [
                        r'completed[^\n]*2022',
                        r'november\s+2022',
                        r'december\s+2022',
                        r'2022[-\s](fall|november|december)'
                    ]
                    for pattern in date_patterns:
                        if re.search(pattern, next_text, re.I):
                            completed_2022 = True
                            break
            
            if is_park and status == 'completed' and completed_2022:
                projects.append({
                    'Project_Name': line,
                    'status': status,
                    'completed_year': 2022
                })
    
    return projects

# Process all documents
all_park_projects_2022 = []
for doc in civic_docs_data:
    projects = extract_projects_from_text(doc.get('text', ''))
    all_park_projects_2022.extend(projects)

# Remove duplicates based on project name
unique_projects = {}
for proj in all_park_projects_2022:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

park_projects_list = list(unique_projects.values())

print('__RESULT__:')
print(json.dumps({
    'park_projects_completed_2022': park_projects_list,
    'count': len(park_projects_list)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
