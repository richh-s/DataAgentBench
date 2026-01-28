code = """import json
import re

# Load MongoDB data
mongo_file_path = locals()['var_functions.query_db:2']
with open(mongo_file_path, 'r') as f:
    mongo_data = json.load(f)

# Load funding data
funding_file_path = locals()['var_functions.query_db:5']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Extract projects from MongoDB text
park_projects_2022 = []

for doc in mongo_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # States for parsing
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and document headers
        if not line or line.startswith('Page') or line.startswith('Agenda Item'):
            continue
            
        # Check if this line looks like a project name
        # Project names are typically on their own line and not standard headers
        is_header = False
        header_patterns = ['To:', 'Prepared by:', 'Approved by:', 'Subject:', 'RECOMMENDED ACTION:', 
                          'DISCUSSION:', 'Date prepared:', 'Meeting date:', 'Public Works', 'Commission',
                          'Capital Improvement Projects', 'Disaster Recovery Projects']
        
        for pattern in header_patterns:
            if line.startswith(pattern):
                is_header = True
                break
        
        # Check for bullet points and other non-project lines
        if '(cid:' in line or line.startswith('●') or line.startswith('•') or line.startswith('■'):
            is_header = True
            
        if not is_header and len(line) > 5 and len(line) < 200:
            # This might be a project name - store it
            current_project = line
            continue
        
        # If we have a current project, look for completion info
        if current_project:
            # Check if this line mentions completion in 2022
            if 'completed' in line.lower() and '2022' in line:
                # Check if it's a park project
                if 'park' in current_project.lower():
                    park_projects_2022.append(current_project)
                    current_project = None  # Reset after finding

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

print('__RESULT__:')
print(json.dumps({"park_projects_2022": park_projects_2022, "count": len(park_projects_2022)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
