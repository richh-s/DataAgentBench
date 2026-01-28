code = """import json
import re

# Load the civic docs data
civic_docs_key = 'var_functions.query_db:0'
civic_docs_path = locals()[civic_docs_key]
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_key = 'var_functions.query_db:1'
funding_path = locals()[funding_key]
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integer
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Function to check if a line is likely a project name
def is_project_name(line):
    if not line or len(line) < 10 or len(line) > 150:
        return False
    if line.startswith(('(', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:')):
        return False
    if any(phrase in line for phrase in ['Status Report', 'City Council', 'Public Works Commission', 'Capital Improvement Projects', 'Disaster Recovery Projects']):
        return False
    if not (line[0].isupper() or line[0].isdigit()):
        return False
    return True

# Extract projects that were completed in 2022 and are park-related
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if is_project_name(line):
            project_name = line
            is_park_project = 'park' in project_name.lower()
            completed_in_2022 = False
            
            # Look ahead up to 20 lines
            for j in range(i+1, min(i+20, len(lines))):
                next_line = lines[j]
                
                # Check for completion in 2022
                if 'completed' in next_line.lower() and '2022' in next_line:
                    completed_in_2022 = True
                elif 'Construction was completed' in next_line and 'November 2022' in next_line:
                    completed_in_2022 = True
                elif 'Construction was completed,' in next_line and '2022' in next_line:
                    completed_in_2022 = True
                elif 'Notice of completion filed' in next_line and ('2022' in next_line or 'January 2023' in next_line):
                    completed_in_2022 = True
                    
                # Check if park-related
                if 'park' in next_line.lower():
                    is_park_project = True
            
            # If this project was completed in 2022 and is park-related, add it
            if completed_in_2022 and is_park_project:
                park_projects_2022.append(project_name)
        
        i += 1

# Remove duplicates
park_projects_2022_unique = list(set(park_projects_2022))

print('__RESULT__:')
print(json.dumps({
    'all_park_projects_2022': park_projects_2022_unique,
    'count': len(park_projects_2022_unique)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
