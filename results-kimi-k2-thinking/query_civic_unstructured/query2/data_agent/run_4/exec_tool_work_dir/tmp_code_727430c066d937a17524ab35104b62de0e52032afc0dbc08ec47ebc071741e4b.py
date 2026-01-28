code = """import json
import re

# Load the data from the stored variables
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:6']

# Load the data if they are file paths
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert funding amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])

# Function to extract projects from civic document text
def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    current_project = None
    project_block = []
    
    skip_patterns = [
        'Public Works', 'Commission', 'Agenda', 'To:', 'Prepared by',
        'Approved by', 'Date', 'Meeting date', 'Subject',
        'RECOMMENDED ACTION', 'DISCUSSION', 'Page', 'Item'
    ]
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and headers
        if not line:
            continue
            
        should_skip = any(pattern in line for pattern in skip_patterns)
        if should_skip:
            continue
        
        # Check if this looks like a project name
        if (len(line) < 150 and 
            (line.istitle() or 'project' in line.lower() or 'improvements' in line.lower() or 
             'repairs' in line.lower() or 'replacement' in line.lower() or 'drainage' in line.lower())):
            
            # Save previous project if exists
            if current_project and project_block:
                projects.append({
                    'name': current_project,
                    'text': '\n'.join(project_block)
                })
            
            # Start new project
            current_project = line
            project_block = [line]
        else:
            # Continue current project block
            if current_project:
                project_block.append(line)
    
    # Add the last project
    if current_project and project_block:
        projects.append({
            'name': current_project,
            'text': '\n'.join(project_block)
        })
    
    return projects

# Extract all projects
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    for project in projects:
        project['doc_id'] = doc['_id']
        project['filename'] = doc['filename']
        all_projects.append(project)

print('__RESULT__:')
print(json.dumps({
    'total_projects_extracted': len(all_projects),
    'sample_projects': all_projects[:7]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}}

exec(code, env_args)
