code = """import json
import re
from collections import defaultdict

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

# Convert funding amounts to integer for summing
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Extract all project names and their completion status from the civic documents
def extract_project_info(civic_docs):
    projects_info = []
    
    for doc in civic_docs:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        
        # Look for patterns indicating project completion in 2022
        completion_patterns = [
            r'Construction was completed[^\n]*2022',
            r'Construction was completed,\s+(\w+\s+2022)',
            r'Construction was completed[^\n]*November 2022',
            r'Construction was completed[^\n]*January 2023[^\n]*2022',
            r'Completed Construction[^\n]*2022',
            r'Notice of completion filed[^\n]*2022',
            r'Notice of completion filed[^\n]*January 2023[^\n]*2022',
        ]
        
        # Find all project-like headers (title case lines)
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Heuristic for project names: reasonable length, title-like, not common headers
            if (len(line) > 10 and len(line) < 150 and 
                not line.startswith(('(', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:')) and
                not any(phrase in line for phrase in ['Status Report', 'City Council', 'Public Works Commission', 'Capital Improvement Projects', 'Disaster Recovery Projects']) and
                (line[0].isupper() or line[0].isdigit())):
                
                # Look ahead to find status
                project_info = {
                    'name': line,
                    'filename': filename,
                    'completed_2022': False,
                    'has_park_topic': False
                }
                
                # Check if this is a park project based on name
                if 'park' in line.lower():
                    project_info['has_park_topic'] = True
                
                # Look ahead up to 15 lines for completion status
                for j in range(i+1, min(i+15, len(lines))):
                    next_line = lines[j]
                    
                    # Check for 2022 completion
                    for pattern in completion_patterns:
                        if re.search(pattern, next_line, re.IGNORECASE):
                            project_info['completed_2022'] = True
                            break
                    
                    # Also check if it's a park project from context
                    if 'park' in next_line.lower():
                        project_info['has_park_topic'] = True
                
                projects_info.append(project_info)
    
    return projects_info

# Extract project information
projects_info = extract_project_info(civic_docs)

# Filter for park projects completed in 2022
park_projects_2022 = [p for p in projects_info if p['completed_2022'] and p['has_park_topic']]

# Get unique project names
park_project_names = list(set([p['name'].strip() for p in park_projects_2022]))

print('__RESULT__:')
print(json.dumps({
    'total_projects_found': len(projects_info),
    'park_projects_2022_count': len(park_project_names),
    'park_projects_2022': park_project_names
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
