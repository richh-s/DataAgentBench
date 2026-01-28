code = """import json
import re

civic_docs = json.load(open('file_storage/functions.query_db:82.json'))
funding_records = json.load(open('file_storage/functions.query_db:80.json'))

design_projects = set()

# Extract capital projects with design status
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section (between "Capital Improvement Projects (Design)" and next major heading)
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find end of section (next "Capital Improvement Projects" or "Disaster Recovery Projects")
    next_capital = text.find('Capital Improvement Projects (', design_start + 40)
    next_disaster = text.find('Disaster Recovery Projects', design_start)
    
    if next_capital > 0 and (next_disaster == -1 or next_capital < next_disaster):
        design_section = text[design_start:next_capital]
    elif next_disaster > 0:
        design_section = text[design_start:next_disaster]
    else:
        design_section = text[design_start:]
    
    # Extract project names from the design section
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        
        # Skip metadata and update lines
        if any(marker in line for marker in ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Page', 'Agenda Item', 'cid:', '•']):
            continue
        
        # Look for infrastructure-related project names (title case, proper nouns, etc.)
        infra_terms = ['road', 'street', 'park', 'drainage', 'storm', 'bridge', 'walkway', 'median', 'signal', 'canyon', 'beach', 'water', 'facility', 'treatment', 'slope', 'wall', 'improvements', 'repairs', 'project', 'skate']
        line_lower = line.lower()
        
        has_infra = any(term in line_lower for term in infra_terms)
        proper_format = line.istitle() or (line[0].isupper() and len(line.split()) >= 2)
        not_metadata = not line.startswith('(') and not line.isupper() and len(line) > 15
        
        if has_infra and proper_format and not_metadata:
            design_projects.add(line)

# Get funded project names over $50,000
funded_projects = {}
for rec in funding_records:
    project_name = rec.get('Project_Name', '').strip()
    amount = int(rec.get('Amount', 0))
    if amount > 50000:
        funded_projects[project_name] = amount

# Match design projects with funding (allowing for partial name matching and suffix variations)
matched = set()
funded_names = list(funded_projects.keys())

for design_name in design_projects:
    # Direct match
    if design_name in funded_projects:
        matched.add(design_name)
        continue
    
    # Clean up design name (remove common suffixes)
    import re
    design_clean = re.sub(r'\s+(Project|Phase\s+\d+|Improvements|Repairs|Design)$', '', design_name, flags=re.IGNORECASE)
    
    # Partial matching
    design_clean_lower = design_clean.lower()
    for funded_name in funded_names:
        funded_lower = funded_name.lower()
        if (design_clean_lower in funded_lower or funded_lower in design_clean_lower or
            any(design_clean_lower in funded_name_part.lower() for funded_name_part in funded_lower.split('('))):
            matched.add(design_name)
            break

print('__RESULT__:')
print(json.dumps({'count': len(matched), 'sample_projects': list(matched)[:8]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}, 'var_functions.execute_python:12': {'json_files': [], 'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.query_db:8', 'var_functions.execute_python:10'], 'current_dir_files': ['tmp_code_b262fd095b36b5236393345bb8d1ca0a3d195790acfd855432118fb96265da25.py', 'tmp_code_ec12d0aa8e6ef28366e7553f1de624160a0ec8fe0b8dcd1d857bdc21d2ac6101.py', 'tmp_code_571c1044f3b97a69aa8a7d818bee03068db011ff8bc05dfe8973c1b9d8bffe19.py', 'tmp_code_e5ff25f71b3e4ce5f3ce1c812f4ebf25f913fb64b2bed77fbaa660f1d36156fc.py', 'file_storage']}, 'var_functions.execute_python:14': {'civic_docs_loaded': 38, 'funding_data_loaded': 38, 'civic_docs_type': 'str'}, 'var_functions.execute_python:16': {'civic_docs_path': 'file_storage/functions.query_db:8.json', 'funding_data_path': 'file_storage/functions.query_db:2.json', 'civic_docs_loaded': 5, 'funding_data_loaded': 276}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_doc_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'funding_data_count': 276, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json'}

exec(code, env_args)
