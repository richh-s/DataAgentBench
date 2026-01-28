code = """import json

# Load funding data
fid = open('file_storage/functions.query_db:32.json', 'r')
funding_data = json.load(fid)
fid.close()

# Load civic data
cid = open('file_storage/functions.query_db:9.json', 'r')
civic_data = json.load(cid)
cid.close()

# Extract design projects from civic documents
design_project_names = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Locate the design section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    
    if design_section_start >= 0:
        # Find where design section ends
        construction_section_start = text.find('Capital Improvement Projects (Construction)', design_section_start)
        
        if construction_section_start < 0:
            construction_section_start = len(text)
        
        design_section = text[design_section_start:construction_section_start]
        
        # Split and process lines
        lines = design_section.split('\n')
        
        for i in range(len(lines)):
            line = lines[i].strip()
            
            # Filter potential project names
            if len(line) > 5 and not line.isupper():
                # Skip headers and metadata
                header_terms = ['Updates', 'Schedule:', 'Advertise:', 'Construction', 'Page', 'Agenda', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement Projects']
                if not any(term in line for term in header_terms):
                    if not line.startswith('(') and not line.startswith('•'):
                        # Check if followed by project metadata
                        if i + 1 < len(lines):
                            next_line = lines[i + 1].strip()
                            if next_line.startswith('Updates:') or 'Complete Design:' in lines[i+1]:
                                design_project_names.append(line)

# Remove duplicates
unique_design_projects = []
seen = set()
for proj in design_project_names:
    if proj not in seen:
        unique_design_projects.append(proj)
        seen.add(proj)

# Get funding project names
funding_names = set()
for item in funding_data:
    funding_names.add(item['Project_Name'])

# Count matches with funding > $50k
matched_count = 0
matched_list = []

for design_proj in unique_design_projects:
    # Check for direct match
    if design_proj in funding_names:
        matched_count += 1
        matched_list.append(design_proj)
    else:
        # Check for partial match (design name contained in funded name or vice versa)
        for funded_proj in funding_names:
            if design_proj in funded_proj or funded_proj in design_proj:
                matched_count += 1
                matched_list.append(design_proj)
                break

# Prepare result
result_dict = {
    'count': matched_count,
    'sample_projects': matched_list[:5]
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_documents': 5, 'first_doc_keys': ['_id', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:46': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
