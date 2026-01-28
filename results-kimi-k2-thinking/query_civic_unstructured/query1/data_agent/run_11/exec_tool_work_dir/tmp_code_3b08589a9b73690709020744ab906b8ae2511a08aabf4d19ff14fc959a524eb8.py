code = """import json
import re
import os

# Load the data from files
civic_docs_path = 'file_storage/functions.query_db:8.json'
funding_data_path = 'file_storage/functions.query_db:22.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

# Extract capital projects with 'design' status from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section
    design_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects|Disaster Recovery Projects|$)'
    design_match = re.search(design_pattern, text, re.DOTALL)
    
    if design_match:
        design_section = design_match.group(1)
        
        # Split into lines and look for project names
        lines = design_section.split('\n')
        in_project_section = False
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Skip markers that aren't project names
            if any(marker in line for marker in ['Updates:', 'Project Schedule:', 'cid:', 'Complete Design:', 
                                               'Advertise:', 'Begin Construction:', '•', 'Page', 'Agenda Item']):
                continue
            
            # Look for project names (usually title case, contain infrastructure keywords, or end with "Project")
            if (len(line) > 10 and  # Reasonable length for a project name
                (line.istitle() or 'Project' in line or '&' in line or
                 any(keyword in line.lower() for keyword in ['road', 'street', 'park', 'drain', 'bridge', 
                                                           'walkway', 'median', 'signal', 'skate', 'canyon', 
                                                           'beach', 'storm', 'water', 'treatment', 'facility']))):
                
                # Clean and validate
                project_name = line.strip()
                if len(project_name) > 8:  # Filter out very short lines
                    projects.append({
                        'Project_Name': project_name,
                        'type': 'capital',
                        'status': 'design'
                    })

# Filter funding data for amounts > 50000
funding_over_50k = [f for f in funding_data if int(f.get('Amount', 0)) > 50000]

# Create lookup for funded project names
funded_names = set()
for f in funding_over_50k:
    name = f.get('Project_Name', '').strip()
    if name:
        funded_names.add(name)

# Find capital design projects with funding > 50k
capital_design_funded = []
for project in projects:
    proj_name = project['Project_Name']
    
    # Check for exact match or partial match
    match_found = False
    
    # Exact match
    if proj_name in funded_names:
        match_found = True
    else:
        # Check if any funded name contains this project name
        for funded_name in funded_names:
            if proj_name.lower() in funded_name.lower():
                match_found = True
                break
            # Also check reverse - if funded name is contained in project name
            elif funded_name.lower() in proj_name.lower() and len(funded_name) > 10:
                match_found = True
                break
    
    if match_found:
        capital_design_funded.append(project['Project_Name'])

# Count unique projects
unique_projects = list(set(capital_design_funded))

result = {
    'total_design_projects_found': len(projects),
    'unique_capital_design_funded_over_50k': len(unique_projects),
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}, 'var_functions.execute_python:12': {'json_files': [], 'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.query_db:8', 'var_functions.execute_python:10'], 'current_dir_files': ['tmp_code_b262fd095b36b5236393345bb8d1ca0a3d195790acfd855432118fb96265da25.py', 'tmp_code_ec12d0aa8e6ef28366e7553f1de624160a0ec8fe0b8dcd1d857bdc21d2ac6101.py', 'tmp_code_571c1044f3b97a69aa8a7d818bee03068db011ff8bc05dfe8973c1b9d8bffe19.py', 'tmp_code_e5ff25f71b3e4ce5f3ce1c812f4ebf25f913fb64b2bed77fbaa660f1d36156fc.py', 'file_storage']}, 'var_functions.execute_python:14': {'civic_docs_loaded': 38, 'funding_data_loaded': 38, 'civic_docs_type': 'str'}, 'var_functions.execute_python:16': {'civic_docs_path': 'file_storage/functions.query_db:8.json', 'funding_data_path': 'file_storage/functions.query_db:2.json', 'civic_docs_loaded': 5, 'funding_data_loaded': 276}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_doc_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'funding_data_count': 276, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
