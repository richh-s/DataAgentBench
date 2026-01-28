code = """import json
import pandas as pd
import re

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

# Extract design projects from civic documents
all_design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find Capital Improvement Projects (Design) section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    
    if design_section_start != -1:
        # Find where this section ends (next major section)
        construction_section_start = text.find('Capital Improvement Projects (Construction)', design_section_start)
        not_started_section_start = text.find('Capital Improvement Projects (Not Started)', design_section_start)
        
        # Determine end position
        end_pos = construction_section_start
        if end_pos == -1 or (not_started_section_start > 0 and not_started_section_start < end_pos):
            end_pos = not_started_section_start
        if end_pos == -1:
            end_pos = len(text)
        
        # Extract the design section
        design_section = text[design_section_start:end_pos]
        
        # Split into lines and find project names
        lines = design_section.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip empty lines and headers
            if len(line) < 5 or line.isupper() or line.startswith('-----'):
                continue
                
            # Skip known non-project lines
            skip_patterns = ['Updates:', 'Project Schedule', 'Complete Design', 'Advertise:', 'Begin Construction', 
                           'Page ', 'Agenda Item', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement', 'cid:']
            if any(pattern in line for pattern in skip_patterns):
                continue
            
            # Skip bullet points and dates
            if line.startswith('(') or line.startswith('•') or re.match(r'\d{1,2}/\d{1,2}/\d{4}', line):
                continue
            
            # This looks like it could be a project name
            # Check if next line contains project indicators
            if i < len(lines) - 2:
                next_lines = '\n'.join(lines[i+1:i+4])
                if 'Updates:' in next_lines or 'Project Schedule' in next_lines:
                    all_design_projects.append({
                        'Project_Name': line,
                        'Status': 'design',
                        'Type': 'capital'
                    })

# Remove duplicates
unique_design_projects = []
seen_names = set()
for proj in all_design_projects:
    if proj['Project_Name'] not in seen_names:
        unique_design_projects.append(proj)
        seen_names.add(proj['Project_Name']

# Now match with funding data
funding_names = set(df_funding['Project_Name'].tolist())

matched_projects = []
for proj in unique_design_projects:
    proj_name = proj['Project_Name']
    
    # Check for direct match
    if proj_name in funding_names:
        amount = df_funding[df_funding['Project_Name'] == proj_name]['Amount'].iloc[0]
        matched_projects.append(proj_name)
    else:
        # Check for fuzzy matches (project name appears in funded name or vice versa)
        for fund_name in funding_names:
            if proj_name in fund_name or fund_name in proj_name:
                matched_projects.append(proj_name)
                break

count_with_funding_over_50k = len(matched_projects)

print('__RESULT__:')
print(json.dumps({
    'total_design_projects': len(unique_design_projects),
    'matched_with_funding': count_with_funding_over_50k,
    'sample_matched': matched_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_documents': 5, 'first_doc_keys': ['_id', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
