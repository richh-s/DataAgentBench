code = """import json

# Load datasets
with open('file_storage/functions.query_db:32.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:9.json', 'r') as f:
    civic_data = json.load(f)

# Get funding project names  
funding_names = set(item['Project_Name'] for item in funding_data)

# Extract design projects from civic documents
design_projects = []
for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    design_marker = 'Capital Improvement Projects (Design)'
    start = text.find(design_marker)
    if start == -1:
        continue
    
    # Find end of design section
    construction_marker = 'Capital Improvement Projects (Construction)'
    end = text.find(construction_marker, start)
    if end == -1:
        end = len(text)
    
    section = text[start:end]
    lines = section.split('\n')
    
    # Extract project names (lines followed by Updates:)
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 5 and not line.isupper():
            has_bad = any(word in line for word in ['Updates', 'Schedule', 'Advertise'])
            if not has_bad and not line.startswith('('):
                if i+1 < len(lines) and 'Updates:' in lines[i+1]:
                    design_projects.append(line)

# Remove duplicates
unique_projects = []
seen = set()
for proj in design_projects:
    if proj not in seen:
        unique_projects.append(proj)
        seen.add(proj)

# Match with funding
matched = []
for design in unique_projects:
    for funded in funding_names:
        if design in funded or funded in design:
            matched.append(design)
            break

result = {'count': len(matched), 'projects': matched[:5]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_documents': 5, 'first_doc_keys': ['_id', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:46': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
