code = """import json
import re

# Load data
funding_file = globals()['var_functions.query_db:4']
civic_file = globals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding dictionary
funding_dict = {}
for record in funding_data:
    try:
        amount = int(record['Amount'])
        funding_dict[record['Project_Name']] = amount
    except:
        continue

# Parse civic documents
project_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project sections
    for i, line in enumerate(lines):
        line = line.strip()
        # Check if line might be a project name (starts with capital letter, reasonable length)
        if len(line) > 5 and line[0].isupper() and not line.startswith('(') and not line.startswith('Page') and not line.startswith('To:') and not line.startswith('From:') and not line.startswith('Subject:'):
            
            # Skip common headers
            skip_words = ['PUBLIC', 'AGENDA', 'ITEM', 'CAPITAL', 'DISASTER', 'DESIGN', 'CONSTRUCTION', 'NOT STARTED', 'RECOMMENDED ACTION']
            if any(word in line.upper() for word in skip_words):
                continue
            
            project_name = line
            
            # Look for status indicators
            status = None
            for j in range(i, min(i+15, len(lines))):
                next_line = lines[j].strip().lower()
                if 'design' in next_line or 'complete design' in next_line:
                    status = 'design'
                    break
                elif 'construction' in next_line and 'complete' in next_line:
                    status = 'completed'
                    break
                elif 'not started' in next_line:
                    status = 'not started'
                    break
            
            # Determine project type
            project_type = None
            if 'capital improvement' in text.lower():
                project_type = 'capital'
            elif 'disaster' in text.lower() or 'fema' in text.lower() or 'recovery' in text.lower():
                project_type = 'disaster'
            
            # Store if we found a status
            if status and project_name not in project_info:
                project_info[project_name] = {
                    'status': status,
                    'type': project_type,
                    'amount': funding_dict.get(project_name, 0)
                }

print("__RESULT__:")
print(json.dumps({
    "projects_found": len(project_info),
    "sample_projects": list(project_info.items())[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5'], 'var_functions.execute_python:20': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding_name': 'Birdview Avenue Improvements'}, 'var_functions.execute_python:22': {'projects_with_funding': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:24': {'funding_projects': 276, 'message': 'Loaded funding data'}, 'var_functions.execute_python:26': {'total_funding_projects': 276, 'funding_dict_size': 276}}

exec(code, env_args)
