code = """import json
import pandas as pd

# Load funding data (projects > $50k)
with open('file_storage/functions.query_db:32.json', 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Load civic documents
with open('file_storage/functions.query_db:9.json', 'r') as f:
    civic_data = json.load(f)

# Extract potential design projects
all_text = ''
for doc in civic_data:
    all_text += doc.get('text', '') + '\n'

# Find design project names by looking for section markers
design_projects = []
start_marker = 'Capital Improvement Projects (Design)'
end_marker = 'Capital Improvement Projects (Construction)'

design_start = all_text.find(start_marker)
if design_start > 0:
    design_end = all_text.find(end_marker, design_start)
    if design_end < 0:
        design_end = len(all_text)
    
    design_section = all_text[design_start:design_end]
    lines = design_section.split('\n')
    
    for line in lines:
        line = line.strip()
        if line and 8 < len(line) < 200 and not line.isupper():
            if 'Updates' not in line and 'Schedule' not in line:
                if not line.startswith('('):
                    design_projects.append(line)

# Filter out non-project lines
clean_projects = []
for proj in design_projects:
    if all(x not in proj for x in ['Page ', 'cid:', 'Agenda', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement']):
        if not any(proj.startswith(x) for x in ['\u2022', '-']):
            clean_projects.append(proj)

# Remove duplicates
unique_projects = list(dict.fromkeys(clean_projects))

# Match with funding
funding_names = df_funding['Project_Name'].tolist()
matched = []

for design_proj in unique_projects:
    for fund_name in funding_names:
        if design_proj in fund_name or fund_name in design_proj:
            amount = df_funding[df_funding['Project_Name'] == fund_name]['Amount'].iloc[0]
            if amount > 50000:
                matched.append(design_proj)
                break

print('__RESULT__:')
print(json.dumps({'count': len(matched)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_documents': 5, 'first_doc_keys': ['_id', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
