code = """import json
import re
import os

# Load civic documents
civic_file = open('file_storage/functions.query_db:30.json', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Load funding data  
funding_file = open('file_storage/functions.query_db:22.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Extract capital design project names
design_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    start_marker = 'Capital Improvement Projects (Design)'
    end_marker1 = 'Capital Improvement Projects ('
    end_marker2 = 'Disaster Recovery Projects'
    
    start = text.find(start_marker)
    if start == -1:
        continue
    
    # Find end of section
    end = text.find(end_marker1, start + len(start_marker))
    if end == -1:
        end = text.find(end_marker2, start + len(start_marker))
    if end == -1:
        end = len(text)
    
    section = text[start:end]
    
    # Extract project names from this section
    for line in section.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        
        # Skip metadata lines
        if 'Updates:' in line or 'Project Schedule:' in line or 'Complete Design:' in line:
            continue
        if 'Advertise:' in line or 'Begin Construction:' in line:
            continue
        if 'Page' in line or 'Agenda Item' in line or 'cid:' in line:
            continue
        
        # Check if this looks like a project name
        keywords = ['road', 'street', 'park', 'drainage', 'drain', 'bridge', 'walkway', 'median', 'signal', 'canyon', 'beach', 'storm']
        has_keyword = False
        for kw in keywords:
            if kw in line.lower():
                has_keyword = True
                break
        
        if has_keyword and (line.istitle() or line[0].isupper()) and not line.startswith('('):
            design_names.add(line)

# Get projects with funding > $50,000
funded_names = set()
for item in funding_data:
    amount = int(item.get('Amount', 0))
    if amount > 50000:
        funded_names.add(item.get('Project_Name', '').strip())

# Count matches (allowing for partial name matching)
matched_count = 0
matched_names = []

for design_name in design_names:
    # Direct match
    if design_name in funded_names:
        matched_count += 1
        matched_names.append(design_name)
        continue
    
    # Partial match - check if design name appears in any funded name
    design_lower = design_name.lower()
    match_found = False
    for funded_name in funded_names:
        funded_lower = funded_name.lower()
        if design_lower in funded_lower or funded_lower in design_lower:
            match_found = True
            break
    
    if match_found:
        matched_count += 1
        matched_names.append(design_name)

# Create result
result = {
    'count': matched_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}, 'var_functions.execute_python:12': {'json_files': [], 'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.query_db:8', 'var_functions.execute_python:10'], 'current_dir_files': ['tmp_code_b262fd095b36b5236393345bb8d1ca0a3d195790acfd855432118fb96265da25.py', 'tmp_code_ec12d0aa8e6ef28366e7553f1de624160a0ec8fe0b8dcd1d857bdc21d2ac6101.py', 'tmp_code_571c1044f3b97a69aa8a7d818bee03068db011ff8bc05dfe8973c1b9d8bffe19.py', 'tmp_code_e5ff25f71b3e4ce5f3ce1c812f4ebf25f913fb64b2bed77fbaa660f1d36156fc.py', 'file_storage']}, 'var_functions.execute_python:14': {'civic_docs_loaded': 38, 'funding_data_loaded': 38, 'civic_docs_type': 'str'}, 'var_functions.execute_python:16': {'civic_docs_path': 'file_storage/functions.query_db:8.json', 'funding_data_path': 'file_storage/functions.query_db:2.json', 'civic_docs_loaded': 5, 'funding_data_loaded': 276}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_doc_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'funding_data_count': 276, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
