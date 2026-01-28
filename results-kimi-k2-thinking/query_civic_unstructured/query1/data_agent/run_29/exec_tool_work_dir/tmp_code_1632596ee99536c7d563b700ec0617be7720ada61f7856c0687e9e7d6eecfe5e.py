code = """import json
import pandas as pd

# Load funding data with projects > $50k
funding_file = 'file_storage/functions.query_db:32.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Load civic documents
civic_file = 'file_storage/functions.query_db:9.json'
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Extract design projects more carefully
all_text = ''
for doc in civic_data:
    all_text += doc.get('text', '') + '\n'

# Find the design section
design_marker = 'Capital Improvement Projects (Design)'
design_start = all_text.find(design_marker)

if design_start != -1:
    # Find where design section ends
    next_section_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    end_pos = len(all_text)
    
    for marker in next_section_markers:
        marker_pos = all_text.find(marker, design_start + len(design_marker))
        if marker_pos != -1 and marker_pos < end_pos:
            end_pos = marker_pos
    
    design_section = all_text[design_start:end_pos]
    
    # Split into lines and filter
    lines = design_section.split('\n')
    candidate_projects = []
    
    for line in lines:
        line = line.strip()
        # Filter for potential project names
        if 10 < len(line) < 200 and not line.isupper():
            skip_words = ['Updates', 'Schedule', 'Advertise', 'Construction', 'Page', 'Agenda', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement', 'cid', 'Project']
            if not any(word in line for word in skip_words):
                if not line.startswith('(') and not line.startswith('•'):
                    # Check if followed by typical project content
                    line_index = lines.index(line)
                    if line_index < len(lines) - 2:
                        next_content = ' '.join(lines[line_index+1:line_index+4])
                        if 'Updates' in next_content or 'Complete Design' in next_content:
                            candidate_projects.append(line)
    
    # Remove duplicates
    design_projects = list(dict.fromkeys(candidate_projects))
else:
    design_projects = []

# Match with funding
funding_names = df_funding['Project_Name'].tolist()
matched_count = 0
matched_names = []

for design_proj in design_projects:
    # Check if this design project has funding
    for fund_name in funding_names:
        if design_proj in fund_name or fund_name in design_proj:
            amount = df_funding[df_funding['Project_Name'] == fund_name]['Amount'].iloc[0]
            if amount > 50000:
                matched_count += 1
                matched_names.append(design_proj)
                break

print('__RESULT__:')
print(json.dumps({
    'design_projects': design_projects,
    'count_design_projects': len(design_projects),
    'count_with_funding_over_50k': matched_count,
    'matched_projects': matched_names
}, default=str))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_documents': 5, 'first_doc_keys': ['_id', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
