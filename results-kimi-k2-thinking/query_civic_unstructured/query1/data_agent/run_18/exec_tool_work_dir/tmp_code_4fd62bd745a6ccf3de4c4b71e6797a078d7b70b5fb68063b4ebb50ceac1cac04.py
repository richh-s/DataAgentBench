code = """import json
import re

# Load data from files
f_result = var_functions.query_db:1
c_result = var_functions.query_db:2

with open(f_result) as f:
    funding_data = json.load(f)
with open(c_result) as f:
    civic_docs = json.load(f)

# Extract capital design projects
design_list = []

for document in civic_docs:
    text = document.get('text', '')
    
    design_marker = 'Capital Improvement Projects (Design)'
    start = text.find(design_marker)
    if start < 0:
        continue
    
    after = text[start:]
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    
    end = len(after)
    for marker in end_markers:
        pos = after.find(marker)
        if pos > 0 and pos < end:
            end = pos
    
    design_section = after[:end]
    
    for line in design_section.splitlines():
        line = line.strip()
        if len(line) < 10 or line.startswith('(') or line == '-':
            continue
        if 'cid:' in line or 'Updates' in line or 'Schedule' in line:
            continue
        
        indicators = ['Project', 'Improvements', 'Repairs', 'Master Plan', 'Study']
        if any(indicator in line for indicator in indicators):
            clean = re.sub(r'[^A-Za-z0-9\s]', '', line)
            clean = clean.strip()
            if clean and len(clean) > 5:
                design_list.append(clean)

# Remove duplicates
design_list = list(set(design_list))

# Get funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Count matches
count = 0
matched_names = []

for design in design_list:
    design_lower = design.lower()
    
    for funded in funded_names:
        funded_lower = funded.lower()
        
        if design in funded or funded in design:
            count += 1
            matched_names.append(design)
            break
        
        proj_words = set(design_lower.split())
        fund_words = set(funded_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            matched_names.append(design)
            break

# Output
result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
