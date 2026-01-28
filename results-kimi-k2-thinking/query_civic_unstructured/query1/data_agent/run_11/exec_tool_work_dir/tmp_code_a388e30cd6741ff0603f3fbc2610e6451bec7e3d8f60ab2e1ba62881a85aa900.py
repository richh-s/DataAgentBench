code = """import json
import re
import os

# Load data
civic_docs_path = 'file_storage/functions.query_db:8.json'
funding_data_path = 'file_storage/functions.query_db:22.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

# Extract all capital projects with design status from civic documents
all_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find sections for Capital Improvement Projects (Design)
    lines = text.split('\n')
    in_design_section = False
    project_count_in_section = 0
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            project_count_in_section = 0
            continue
            
        if in_design_section:
            if 'Capital Improvement Projects' in line and '(Design)' not in line:
                in_design_section = False
                continue
                
            if 'Disaster Recovery Projects' in line:
                in_design_section = False
                continue
            
            # Skip empty lines and metadata
            if not line or len(line) < 8:
                continue
                
            # Skip update/schedule lines
            if any(skip in line for skip in ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'cid:']):
                continue
                
            # Skip page numbers and agenda items
            if line.startswith('Page') or line.startswith('Agenda Item'):
                continue
                
            # This is likely a project name
            if (line.istitle() or 'Project' in line or 
                any(keyword in line.lower() for keyword in ['road', 'street', 'park', 'drainage', 'drain', 'bridge', 'walkway', 'median', 'signal', 'canyon', 'beach', 'storm', 'water', 'treatment', 'facility', 'skate'])):
                
                # Additional validation - should not be a continuation line
                if not line.startswith(('(', '•', '-')):
                    all_design_projects.append(line)

# Get funded projects > $50k
funded_projects = set()
for f in funding_data:
    if int(f.get('Amount', 0)) > 50000:
        funded_projects.add(f.get('Project_Name', '').strip())

# Match design projects with funding
capital_design_with_funding = []

for design_project in all_design_projects:
    # Direct match
    if design_project in funded_projects:
        capital_design_with_funding.append(design_project)
        continue
    
    # Partial matching
    for funded_name in funded_projects:
        if (design_project.lower() in funded_name.lower() or 
            funded_name.lower() in design_project.lower()):
            capital_design_with_funding.append(design_project)
            break

# Get unique count
unique_matches = list(set(capital_design_with_funding))

result = {
    'count': len(unique_matches),
    'projects': unique_matches[:20]  # First 20 for preview
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}, 'var_functions.execute_python:12': {'json_files': [], 'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.query_db:8', 'var_functions.execute_python:10'], 'current_dir_files': ['tmp_code_b262fd095b36b5236393345bb8d1ca0a3d195790acfd855432118fb96265da25.py', 'tmp_code_ec12d0aa8e6ef28366e7553f1de624160a0ec8fe0b8dcd1d857bdc21d2ac6101.py', 'tmp_code_571c1044f3b97a69aa8a7d818bee03068db011ff8bc05dfe8973c1b9d8bffe19.py', 'tmp_code_e5ff25f71b3e4ce5f3ce1c812f4ebf25f913fb64b2bed77fbaa660f1d36156fc.py', 'file_storage']}, 'var_functions.execute_python:14': {'civic_docs_loaded': 38, 'funding_data_loaded': 38, 'civic_docs_type': 'str'}, 'var_functions.execute_python:16': {'civic_docs_path': 'file_storage/functions.query_db:8.json', 'funding_data_path': 'file_storage/functions.query_db:2.json', 'civic_docs_loaded': 5, 'funding_data_loaded': 276}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_doc_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'funding_data_count': 276, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
