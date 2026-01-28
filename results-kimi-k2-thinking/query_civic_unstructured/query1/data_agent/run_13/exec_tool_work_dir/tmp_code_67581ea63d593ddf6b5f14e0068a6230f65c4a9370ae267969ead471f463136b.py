code = """import json
import re

# Load the data files
funding_path = var_functions.query_db:46
civic_path = var_functions.query_db:54

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project names
funding_names = []
for record in funding_records:
    funding_names.append(record['Project_Name'])

# Find design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find design section
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    end = len(text)
    markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']
    for marker in markers:
        pos = text.find(marker, start)
        if pos > 0 and pos < end:
            end = pos
    
    section = text[start:end]
    
    # Extract project names from section
    for line in section.split('\n'):
        line_clean = line.strip()
        if not line_clean or len(line_clean) < 10:
            continue
        
        lower_line = line_clean.lower()
        
        # Skip lines with status keywords
        pattern1 = 'updates:'
        pattern2 = 'schedule:'
        pattern3 = 'advertise:'
        pattern4 = 'staff'
        pattern5 = 'city'
        pattern6 = 'project is'
        pattern7 = 'to:'
        pattern8 = 'prepared'
        pattern9 = 'approved'
        pattern10 = 'date'
        pattern11 = 'meeting'
        pattern12 = 'subject:'
        pattern13 = 'agenda'
        pattern14 = 'item'
        pattern15 = 'page'
        pattern16 = 'public works'
        pattern17 = 'commission'
        
        skip = False
        for pat in [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7, pattern8, pattern9, pattern10, pattern11, pattern12, pattern13, pattern14, pattern15, pattern16, pattern17]:
            if pat in lower_line:
                skip = True
                break
        
        if skip or '(cid' in lower_line or line_clean[0:1] == '(':
            continue
        
        # Check for year patterns
        m = re.search(r'\d{4}', lower_line)
        if m is not None:
            continue
        
        # Add project
        proj = line_clean.strip().title()
        if proj and proj not in design_projects:
            design_projects.append(proj)

# Match projects
matched = []

for design_proj in design_projects:
    d_core = design_proj.split('(')[0].strip().lower()
    
    for fund_proj in funding_names:
        f_core = fund_proj.split('(')[0].strip().lower()
        
        if d_core == f_core:
            if design_proj not in matched:
                matched.append(design_proj)

# Result
count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
