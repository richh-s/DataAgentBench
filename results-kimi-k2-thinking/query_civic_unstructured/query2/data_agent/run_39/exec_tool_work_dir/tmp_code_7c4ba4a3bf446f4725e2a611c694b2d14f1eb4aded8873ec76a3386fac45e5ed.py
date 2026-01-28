code = """import json
import re

# Load the MongoDB data
mongo_file_path = locals()['var_functions.query_db:2']
with open(mongo_file_path, 'r') as f:
    mongo_data = json.load(f)

# Load the funding data
funding_file_path = locals()['var_functions.query_db:5']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Extract projects from MongoDB by searching for completed projects in the text
park_projects_completed_2022 = []

for doc in mongo_data:
    text = doc.get('text', '')
    
    # Look for patterns indicating park projects completed in 2022
    # Pattern: project name followed by updates mentioning completion in 2022
    
    # Find all project sections (they often start with a project name on its own line)
    lines = text.split('\n')
    
    # States for parsing
    current_project = None
    capturing_project = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and document headers
        if not line or line.startswith('Page') or line.startswith('Agenda Item'):
            continue
            
        # Check if this line looks like a project name (not a header/bullet)
        if (len(line) > 5 and 
            not line.startswith('To:') and not line.startswith('Prepared by:') and
            not line.startswith('Approved by:') and not line.startswith('Subject:') and
            not line.startswith('RECOMMENDED ACTION:') and not line.startswith('DISCUSSION:') and
            not line.startswith('Date prepared:') and not line.startswith('Meeting date:') and
            not line.startswith('Public Works') and not line.startswith('Commission') and
            '(cid:' not in line and line != 'Capital Improvement Projects (Design)' and
            line != 'Capital Improvement Projects (Construction)' and line != 'Capital Improvement Projects (Not Started)'):
            
            current_project = line
            capturing_project = True
            continue
        
        # If we're capturing a project, look for completion info
        if capturing_project and current_project:
            # Look for completion in 2022
            if 'completed' in line.lower() and '2022' in line:
                # Check if it's a park project
                if 'park' in current_project.lower():
                    park_projects_completed_2022.append(current_project)
            
            # Reset after we've processed the project section
            if line.startswith('Capital Improvement') or i > 0 and lines[i-1].strip().startswith('Capital Improvement'):
                capturing_project = False
                current_project = None

# Remove duplicates
park_projects_completed_2022 = list(set(park_projects_completed_2022))

print('__RESULT__:')
print(json.dumps(park_projects_completed_2022))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
