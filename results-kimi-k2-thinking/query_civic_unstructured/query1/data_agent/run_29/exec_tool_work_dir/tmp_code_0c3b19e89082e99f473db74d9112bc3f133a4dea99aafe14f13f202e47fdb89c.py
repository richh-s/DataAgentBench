code = """import json

# Load funding data (projects > $50k)
with open('file_storage/functions.query_db:32.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('file_storage/functions.query_db:9.json', 'r') as f:
    civic_data = json.load(f)

# Extract design project names from civic documents
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where design section ends
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    if construction_start == -1:
        construction_start = len(text)
    
    design_section = text[design_start:construction_start]
    lines = design_section.split('\n')
    
    # Look for project names (non-header lines followed by Updates:)
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 5 or line.isupper():
            continue
        
        # Skip if contains common non-project words
        if 'Updates:' in line or 'Schedule:' in line or 'Page' in line or 'cid:' in line:
            continue
        
        # Check if next line indicates this is a project
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith('Updates:'):
                design_projects.append(line)

# Remove duplicates
design_projects_unique = []
seen = set()
for proj in design_projects:
    if proj not in seen:
        design_projects_unique.append(proj)
        seen.add(proj)

# Match with funding data
funding_project_names = set(item['Project_Name'] for item in funding_data)

matched_projects = []
for design_proj in design_projects_unique:
    # Check direct match
    if design_proj in funding_project_names:
        matched_projects.append(design_proj)
    else:
        # Check partial matches
        for funded_name in funding_project_names:
            if design_proj in funded_name or funded_name in design_proj:
                matched_projects.append(design_proj)
                break

# Return results without problematic characters
result = {
    'count': len(matched_projects),
    'sample': matched_projects[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_documents': 5, 'first_doc_keys': ['_id', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:46': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
