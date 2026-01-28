code = """import json
import pandas as pd
import re

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
    
    # Look for Capital Improvement Projects sections
    # Pattern for Design section
    design_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY PROJECTS|$)'
    design_match = re.search(design_pattern, text, re.DOTALL)
    
    if design_match:
        design_section = design_match.group(1)
        # Extract project names - they're typically on separate lines before updates
        lines = design_section.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip empty lines and known headers
            if line and not any(skip in line for skip in ['Updates', 'Project Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'RECOMMENDED ACTION', 'DISCUSSION']):
                # Check if this looks like a project name (not a bullet point, not a date)
                if not line.startswith('(') and not line.startswith('•') and not re.match(r'\d{1,2}/\d{1,2}/\d{4}', line):
                    # Check if next few lines contain project indicators
                    next_lines = ' '.join(lines[i+1:i+4])
                    if 'Complete Design' in next_lines or 'Project Schedule' in next_lines:
                        projects.append({
                            'Project_Name': line,
                            'type': 'capital',
                            'status': 'design'
                        })

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in projects:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

print('__RESULT__:')
print(json.dumps({
    'extracted_projects': unique_projects,
    'extracted_count': len(unique_projects),
    'sample_extracted': unique_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
