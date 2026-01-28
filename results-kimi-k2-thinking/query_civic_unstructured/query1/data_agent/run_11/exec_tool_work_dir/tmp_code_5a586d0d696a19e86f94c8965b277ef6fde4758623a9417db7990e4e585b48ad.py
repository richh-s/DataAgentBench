code = """import json

# Load the civic documents
civic_docs_file = open('file_storage/functions.query_db:30.json')
civic_docs = json.load(civic_docs_file)
civic_docs_file.close()

# Load the funding data
funding_file = open('file_storage/functions.query_db:22.json')
funding_data = json.load(funding_file)
funding_file.close()

# Collect all design project names from civic documents
design_names = set()
keywords = ['road', 'street', 'park', 'drainage', 'drain', 'storm', 'bridge', 'walkway', 'median', 'signal', 'canyon', 'beach', 'water', 'facility', 'skate']

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section start
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where the design section ends
    design_end = text.find('Capital Improvement Projects (', design_start + 40)
    if design_end == -1:
        design_end = len(text)
    
    design_section = text[design_start:design_end]
    lines = design_section.split('\n')
    
    for line in lines:
        line = line.strip()
        # Skip short lines and metadata
        if len(line) < 10 or 'Page' in line or 'Agenda Item' in line or 'cid:' in line:
            continue
        if line.startswith(('Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:')):
            continue
        
        # Check if line looks like a project name
        if any(kw in line.lower() for kw in keywords):
            if line.istitle() or line[0].isupper() or 'Project' in line:
                if not line.startswith('(') and ' ' in line:
                    design_names.add(line)

# Create set of funded project names (amount > $50,000)
funded_names = set()
for record in funding_data:
    amount = int(record.get('Amount', 0))
    if amount > 50000:
        name = record.get('Project_Name', '').strip()
        if name:
            funded_names.add(name)

# Count matches between design projects and funded projects
matched_count = 0

for design_name in design_names:
    # Direct matching
    if design_name in funded_names:
        matched_count += 1
        continue
    
    # Partial/approximate matching
    design_lower = design_name.lower()
    for funded_name in funded_names:
        funded_lower = funded_name.lower()
        if design_lower in funded_lower or funded_lower in design_lower:
            matched_count += 1
            break

# Output the result
print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}, 'var_functions.execute_python:12': {'json_files': [], 'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.query_db:8', 'var_functions.execute_python:10'], 'current_dir_files': ['tmp_code_b262fd095b36b5236393345bb8d1ca0a3d195790acfd855432118fb96265da25.py', 'tmp_code_ec12d0aa8e6ef28366e7553f1de624160a0ec8fe0b8dcd1d857bdc21d2ac6101.py', 'tmp_code_571c1044f3b97a69aa8a7d818bee03068db011ff8bc05dfe8973c1b9d8bffe19.py', 'tmp_code_e5ff25f71b3e4ce5f3ce1c812f4ebf25f913fb64b2bed77fbaa660f1d36156fc.py', 'file_storage']}, 'var_functions.execute_python:14': {'civic_docs_loaded': 38, 'funding_data_loaded': 38, 'civic_docs_type': 'str'}, 'var_functions.execute_python:16': {'civic_docs_path': 'file_storage/functions.query_db:8.json', 'funding_data_path': 'file_storage/functions.query_db:2.json', 'civic_docs_loaded': 5, 'funding_data_loaded': 276}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_doc_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'funding_data_count': 276, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
