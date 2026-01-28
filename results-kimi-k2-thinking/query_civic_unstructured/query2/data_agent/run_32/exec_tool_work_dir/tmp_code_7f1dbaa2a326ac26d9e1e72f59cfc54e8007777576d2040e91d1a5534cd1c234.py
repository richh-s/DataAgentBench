code = """import json
import pandas as pd
import re

# Load data
funding_path = locals()['var_functions.query_db:4']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Process funding data
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for project name indicators (typically capitalized, not bullet points)
        if line and len(line) > 10 and not line.startswith('(') and not line.startswith('•') \
           and not line.startswith('●') and not line.startswith('□') \
           and 'Project Schedule:' not in line and 'Project Description:' not in line \
           and 'Updates:' not in line and 'To:' not in line and 'From:' not in line \
           and 'Subject:' not in line and 'Prepared by:' not in line:
            
            # Check if this looks like a project name
            if any(keyword in line.lower() for keyword in ['project', 'improvements', 'repairs', 
                                                           'replacement', 'renovation', 'structure',
                                                           'walkway', 'drainage', 'resurfacing']):
                current_project = line
                # Look ahead for status and dates
                j = i + 1
                status = None
                date_info = None
                
                while j < min(i + 10, len(lines)):
                    next_line = lines[j].strip().lower()
                    
                    # Check for status
                    if 'completed' in next_line or 'completion' in next_line:
                        status = 'completed'
                        # Look for date in this line or nearby
                        if '2022' in next_line:
                            date_info = '2022'
                        elif j + 1 < len(lines) and '2022' in lines[j + 1]:
                            date_info = '2022'
                    elif 'construction was completed' in next_line and '2022' in next_line:
                        status = 'completed'
                        date_info = '2022'
                    elif 'status:' in next_line and 'completed' in next_line:
                        status = 'completed'
                        
                    j += 1
                
                if current_project and status == 'completed' and date_info == '2022':
                    projects.append({
                        'Project_Name': current_project,
                        'Status': status,
                        'Year': date_info
                    })
        
        i += 1

# Also look for completion statements with project names
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern: Project name followed by completion statement
    completion_patterns = [
        r'([^\n]+?)\n[^\n]*(?:construction was completed|completed)[^\n]*2022',
        r'([^\n]+?)\n[^\n]*notice of completion[^\n]*2022'
    ]
    
    for pattern in completion_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            project_name = match.strip()
            if len(project_name) > 10 and not any(skip in project_name.lower() 
                                                   for skip in ['project schedule', 'project description', 
                                                               'updates:', 'to:', 'from:', 'subject:']):
                projects.append({
                    'Project_Name': project_name,
                    'Status': 'completed',
                    'Year': '2022'
                })

# Remove duplicates
unique_projects = {}
for p in projects:
    name = p['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = p

projects_list = list(unique_projects.values())

print('__RESULT__:')
print(json.dumps({
    'total_projects_found': len(projects_list),
    'sample_projects': projects_list[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_documents': 5, 'park_projects_found': 21, 'total_park_funding': 1123000, 'completed_2022_projects_raw': 2}}

exec(code, env_args)
