code = """import json
import re

# Load data
with open('file_storage/functions.query_db:32.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:9.json', 'r') as f:
    civic_data = json.load(f)

# Get all funding project names for projects > $50k
funding_projects = set(item['Project_Name'] for item in funding_data)

# Extract design projects from civic documents
all_design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find end of design section
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    if construction_start == -1:
        construction_start = len(text)
    
    design_section = text[design_start:construction_start]
    
    # Split into lines and process
    lines = design_section.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty lines and obvious non-project lines
        if not line or len(line) < 5:
            continue
        
        # Skip headers and noise
        if line.isupper() or 'cid:' in line or 'Page ' in line or 'Updates:' in line or 'Schedule:' in line:
            continue
        
        # Check if followed by project markers
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if 'Updates:' in next_line:
                all_design_projects.append(line)

# Remove duplicates
design_projects = []
seen = set()
for proj in all_design_projects:
    if proj not in seen:
        design_projects.append(proj)
        seen.add(proj)

# Match with funding data
matched_design_projects = []

for design_proj in design_projects:
    # Check direct match
    if design_proj in funding_projects:
        matched_design_projects.append(design_proj)
    else:
        # Check partial matches
        for funded_proj in funding_projects:
            if design_proj in funded_proj or funded_proj in design_proj:
                matched_design_projects.append(design_proj)
                break

# Count and return result
count_result = len(matched_design_projects)
matched_sample = matched_design_projects[:15]

print('__RESULT__:')
print(json.dumps({
    'count': count_result,
    'sample_projects': matched_sample
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_documents': 5, 'first_doc_keys': ['_id', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:46': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
