code = """import json
import pandas as pd

# Load funding data
funding_file = 'file_storage/functions.query_db:5.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Load civic documents
civic_file = 'file_storage/functions.query_db:9.json'
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Extract projects from civic documents
projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find Design section start
    design_marker = 'Capital Improvement Projects (Design)'
    design_start = text.find(design_marker)
    
    if design_start == -1:
        design_marker = 'Capital Improvement Projects (Design)'.replace('(', '\\(').replace(')', '\\)')
        design_start = text.find(design_marker)
    
    if design_start != -1:
        # Find where design section ends (next major heading)
        construction_marker = 'Capital Improvement Projects (Construction)'
        not_started_marker = 'Capital Improvement Projects (Not Started)'
        
        construction_start = text.find(construction_marker, design_start)
        not_started_start = text.find(not_started_marker, design_start)
        
        end_pos = min([pos for pos in [construction_start, not_started_start] if pos > 0], default=len(text))
        
        design_section = text[design_start:end_pos]
        
        lines = design_section.split('\n')
        current_project = None
        
        for line in lines:
            line = line.strip()
            if line and len(line) > 5:
                skip_words = ['Updates', 'Project Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital', 'RECOMMENDED', 'DISCUSSION', 'Page', '----', 'cid:']
                if not any(skip in line for skip in skip_words):
                    if not line.startswith('(') and not line.startswith('•'):
                        if line[0].isalnum():
                            projects.append({
                                'Project_Name': line,
                                'Status': 'design',
                                'Type': 'capital'
                            })

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in projects:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

# Basic cleanup
final_projects = []
for proj in unique_projects:
    name = proj['Project_Name']
    if len(name) > 10 and len(name) < 100:
        if not name.isupper():
            final_projects.append(proj)

print('__RESULT__:')
print(json.dumps({
    'projects': final_projects,
    'count': len(final_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
