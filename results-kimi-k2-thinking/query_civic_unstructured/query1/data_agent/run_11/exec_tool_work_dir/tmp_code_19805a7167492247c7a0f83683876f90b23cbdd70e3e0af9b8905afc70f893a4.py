code = """import json
import re
import os

# Load civic documents
civic_docs_path = 'file_storage/functions.query_db:74.json'
civic_docs = json.load(open(civic_docs_path))

# Load funding data
funding_data_path = 'file_storage/functions.query_db:22.json'
funding_data = json.load(open(funding_data_path))

# Extract capital design projects from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where design section ends (next major heading)
    design_end = text.find('Capital Improvement Projects (', design_start + 40)
    disaster_start = text.find('Disaster Recovery Projects', design_start)
    
    if design_end == -1 and disaster_start == -1:
        section = text[design_start:]
    elif design_end != -1 and (disaster_start == -1 or design_end < disaster_start):
        section = text[design_start:design_end]
    else:
        section = text[design_start:disaster_start]
    
    # Extract project names from this section
    for line in section.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        
        # Skip metadata and update lines
        skip_patterns = ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Page', 'Agenda Item', 'cid:', '•']
        should_skip = False
        for pattern in skip_patterns:
            if pattern in line:
                should_skip = True
                break
        if should_skip:
            continue
        
        # Look for project names (contain infrastructure keywords and proper capitalization)
        infra_keywords = ['road', 'street', 'park', 'drainage', 'storm', 'bridge', 'walkway', 'median', 'signal', 'canyon', 'beach', 'water', 'facility', 'skate', 'slope', 'treatment', 'facility', 'traffic', 'warning', 'resurfacing', 'improvements', 'repair', 'project', 'phase']
        
        line_lower = line.lower()
        has_infra_term = any(kw in line_lower for kw in infra_keywords)
        
        # Check if it looks like a project name (properly capitalized or contains "Project")
        looks_like_name = line.istitle() or (line[0].isupper() and len(line.split()) >= 2) or 'Project' in line
        
        # Filter out obvious non-project lines
        if (has_infra_term and looks_like_name and not line.startswith('(') and 
            len(line) > 15 and not line.isupper() and not line.endswith(':')):
            design_projects.add(line)

# Get funded projects with amount > $50,000
funded_projects = {}
for item in funding_data:
    amount = int(item.get('Amount', 0))
    if amount > 50000:
        project_name = item.get('Project_Name', '').strip()
        funded_projects[project_name] = amount

# Match design projects with funding (allowing for partial name matching)
matched_projects = []
funded_names = list(funded_projects.keys())

for design_name in design_projects:
    # Direct match
    if design_name in funded_projects:
        matched_projects.append((design_name, funded_projects[design_name]))
        continue
    
    # Partial matching (remove common suffixes/prefixes and compare)
    design_clean = re.sub(r'\s+(Project|Phase\s+\d+|Improvements|Repairs|Design)$', '', design_name, flags=re.IGNORECASE)
    
    for funded_name in funded_names:
        # Check for containment in either direction
        if (design_name.lower() in funded_name.lower() or 
            funded_name.lower() in design_name.lower() or
            design_clean.lower() in funded_name.lower() or
            funded_name.lower() in design_clean.lower()):
            matched_projects.append((design_name, funded_projects[funded_name]))
            break

# Remove duplicates and count
unique_matched = list(set(matched_projects))
count = len(unique_matched)

# Prepare result
result = {
    'count': count,
    'projects': unique_matched[:10]  # Sample of matched projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}, 'var_functions.execute_python:12': {'json_files': [], 'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.query_db:8', 'var_functions.execute_python:10'], 'current_dir_files': ['tmp_code_b262fd095b36b5236393345bb8d1ca0a3d195790acfd855432118fb96265da25.py', 'tmp_code_ec12d0aa8e6ef28366e7553f1de624160a0ec8fe0b8dcd1d857bdc21d2ac6101.py', 'tmp_code_571c1044f3b97a69aa8a7d818bee03068db011ff8bc05dfe8973c1b9d8bffe19.py', 'tmp_code_e5ff25f71b3e4ce5f3ce1c812f4ebf25f913fb64b2bed77fbaa660f1d36156fc.py', 'file_storage']}, 'var_functions.execute_python:14': {'civic_docs_loaded': 38, 'funding_data_loaded': 38, 'civic_docs_type': 'str'}, 'var_functions.execute_python:16': {'civic_docs_path': 'file_storage/functions.query_db:8.json', 'funding_data_path': 'file_storage/functions.query_db:2.json', 'civic_docs_loaded': 5, 'funding_data_loaded': 276}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_doc_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'funding_data_count': 276, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
