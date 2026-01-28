code = """import json
import re

# Load the data
civic_docs_path = 'var_functions.query_db:30'
funding_data_path = 'var_functions.query_db:22'

civic_docs = json.load(open(civic_docs_path))
funding_data = json.load(open(funding_data_path))

# Extract capital projects with design status
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects|Disaster Recovery Projects|$)', text, re.DOTALL)
    
    if design_section:
        section_text = design_section.group(1)
        lines = section_text.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines and metadata
            if not line or len(line) < 8:
                continue
            
            # Skip update/schedule markers
            skip_patterns = ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:']
            if any(pattern in line for pattern in skip_patterns):
                continue
            
            # Skip page/section markers
            if 'Page' in line or 'Agenda Item' in line or 'cid:' in line:
                continue
            
            # Look for project names (title case, contains keywords, or ends with Project)
            keywords = ['road', 'street', 'park', 'drainage', 'drain', 'bridge', 'walkway', 'median', 'signal', 'canyon', 'beach', 'storm', 'water', 'treatment', 'facility', 'skate', 'slope', 'warning', 'traffic']
            
            if (line.istitle() and any(kw in line.lower() for kw in keywords)) or \
               (line[0].isupper() and 'Project' in line) or \
               ('&' in line and line[0].isupper()):
                design_projects.add(line)

# Get funded projects > $50k
funded_projects = set()
for f in funding_data:
    amount = int(f.get('Amount', 0))
    if amount > 50000:
        funded_projects.add(f.get('Project_Name', '').strip())

# Match projects (handle variations like suffixes)
matched_projects = set()

for design_project in design_projects:
    # Direct match
    if design_project in funded_projects:
        matched_projects.add(design_project)
        continue
    
    # Partial matching (ignore common suffixes)
    design_base = re.sub(r'\s+(Project|Phase\s+\d+|Improvements|Repairs)$', '', design_project, flags=re.IGNORECASE)
    
    for funded_name in funded_projects:
        funded_base = re.sub(r'\s+\(.*\)$', '', funded_name)  # Remove (FEMA Project) etc.
        funded_base = re.sub(r'\s+(Project|Phase\s+\d+|Improvements|Repairs)$', '', funded_base, flags=re.IGNORECASE)
        
        if design_base.lower() in funded_base.lower() or funded_base.lower() in design_base.lower():
            matched_projects.add(design_project)
            break

result = {
    'count': len(matched_projects),
    'projects': list(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}, 'var_functions.execute_python:12': {'json_files': [], 'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.query_db:8', 'var_functions.execute_python:10'], 'current_dir_files': ['tmp_code_b262fd095b36b5236393345bb8d1ca0a3d195790acfd855432118fb96265da25.py', 'tmp_code_ec12d0aa8e6ef28366e7553f1de624160a0ec8fe0b8dcd1d857bdc21d2ac6101.py', 'tmp_code_571c1044f3b97a69aa8a7d818bee03068db011ff8bc05dfe8973c1b9d8bffe19.py', 'tmp_code_e5ff25f71b3e4ce5f3ce1c812f4ebf25f913fb64b2bed77fbaa660f1d36156fc.py', 'file_storage']}, 'var_functions.execute_python:14': {'civic_docs_loaded': 38, 'funding_data_loaded': 38, 'civic_docs_type': 'str'}, 'var_functions.execute_python:16': {'civic_docs_path': 'file_storage/functions.query_db:8.json', 'funding_data_path': 'file_storage/functions.query_db:2.json', 'civic_docs_loaded': 5, 'funding_data_loaded': 276}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_doc_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'funding_data_count': 276, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
