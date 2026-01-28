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

# Parse civic documents to extract project information
project_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections in the text
    # Pattern to find project names and their details
    project_patterns = [
        r'([A-Z][^\n]+?)\n\s*\(cid:\d+\)\s+Updates:',  # Capital Improvement Projects
        r'([A-Z][^\n]+?)\n\s*\(cid:\d+\)\s+Project Description:',  # Other projects
        r'([A-Z][^\n]+?)\n\(cid:\d+\)',  # General pattern
    ]
    
    # Also look for lines that look like project names (starting with capital letters)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 5 and line[0].isupper() and not line.startswith('(') and not line.startswith('Page'):
            # Check if this might be a project name
            if 'Project' not in line and line.endswith('Project'):
                project_name = line.strip()
                # Look for status indicators nearby
                status = None
                project_type = None
                
                # Look ahead for status
                for j in range(i, min(i+10, len(lines))):
                    next_line = lines[j].strip().lower()
                    if 'design' in next_line or 'complete design' in next_line:
                        status = 'design'
                        break
                    elif 'construction' in next_line and ('complete' in next_line or 'completed' in next_line):
                        status = 'completed'
                        break
                    elif 'not started' in next_line:
                        status = 'not started'
                        break
                
                # Look for project type
                if 'capital improvement' in text.lower():
                    project_type = 'capital'
                elif 'disaster' in text.lower() or 'fema' in text.lower():
                    project_type = 'disaster'
                
                # Store project info
                if project_name:
                    project_info[project_name] = {
                        'status': status,
                        'type': project_type,
                        'amount': funding_dict.get(project_name, 0)
                    }

print("__RESULT__:")
print(json.dumps({
    "projects_parsed": len(project_info),
    "sample_projects": list(project_info.items())[:5]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5'], 'var_functions.execute_python:20': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding_name': 'Birdview Avenue Improvements'}, 'var_functions.execute_python:22': {'projects_with_funding': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:24': {'funding_projects': 276, 'message': 'Loaded funding data'}, 'var_functions.execute_python:26': {'total_funding_projects': 276, 'funding_dict_size': 276}}

exec(code, env_args)
