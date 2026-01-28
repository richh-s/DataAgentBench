code = """import json
import re

# Load funding data
funding_path = '/tmp/tmpf6o4o9x2.json'
civic_path = '/tmp/tmpp3s6x5y4.json'

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract funding project names
funding_names = []
for record in funding_records:
    funding_names.append(record['Project_Name'].lower())

# Extract design projects from civic documents
# Looking at the first document which contains the design section
text = civic_docs[0]['text'].lower()

# Find the design section
start_index = text.find('capital improvement projects (design)')
if start_index != -1:
    # Find the end of the design section
    end_index = text.find('capital improvement projects (construction)', start_index)
    if end_index == -1:
        end_index = text.find('capital improvement projects (not started)', start_index)
    if end_index == -1:
        end_index = len(text)
    
    design_section = text[start_index:end_index]
    lines = design_section.split('\n')
    
    design_projects = []
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue
        
        lower_line = clean_line.lower()
        
        # Skip metadata and status update lines
        if lower_line.startswith('capital improvement'):
            continue
        if lower_line.startswith('('):
            continue
        if '(cid' in lower_line:
            continue
        if 'updates:' in lower_line or 'schedule:' in lower_line:
            continue
        if any(word in lower_line for word in ['staff', 'city will', 'project is', 'to:', 'prepared', 'approved', 'date', 'meeting']):
            continue
        
        # Skip short date-like lines
        if re.search(r'\d{4}', lower_line) and len(clean_line.split()) <= 4:
            continue
        
        # Skip page numbers
        if clean_line.isdigit():
            continue
        
        # Skip very short lines
        if len(clean_line) < 10:
            continue
        
        # This appears to be a project name
        project_name = clean_line.title().strip()
        if project_name not in design_projects:
            design_projects.append(project_name)

# Match design projects with funding data
matched_projects = []
for design_project in design_projects:
    design_core = design_project.lower().split('(')[0].strip()
    for funding_project in funding_names:
        funding_core = funding_project.split('(')[0].strip()
        if design_core == funding_core:
            if design_project not in matched_projects:
                matched_projects.append(design_project)
                break

# Count the result
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
