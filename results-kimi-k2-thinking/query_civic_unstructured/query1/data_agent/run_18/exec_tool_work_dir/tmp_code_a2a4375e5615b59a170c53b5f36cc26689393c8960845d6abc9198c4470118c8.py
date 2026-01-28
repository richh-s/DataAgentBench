code = """import json
import re

# Load funding data  
funding_path = str(var_functions.query_db:70)
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_path = str(var_functions.query_db:71)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Get funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Extract capital design projects from documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    design_marker = 'Capital Improvement Projects (Design)'
    dpos = text.find(design_marker)
    if dpos < 0:
        continue
    
    # Find design section end  
    after_design = text[dpos:]
    end_pos = len(after_design)
    
    end_markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Disaster Recovery Projects'
    ]
    
    for marker in end_markers:
        pos = after_design.find(marker)
        if pos > 0 and pos < end_pos:
            end_pos = pos
    
    design_section = after_design[:end_pos]
    
    # Extract project names
    for line in design_section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•') or line.startswith('●'):
            continue
        if 'cid:' in line or ':' in line:
            continue
        
        skip_words = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction',
                     'Project Description', 'Project Schedule', 'Estimated Schedule']
        if any(word in line for word in skip_words):
            continue
        
        indicators = ['Project', 'Improvements', 'Repairs', 'Infrastructure', 'Master Plan',
                     'Study', 'Replacement', 'Facility']
        if any(indicator in line for indicator in indicators):
            clean = re.sub(r'[^A-Za-z0-9\s&]', '', line).strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
unique_design = list(set(design_projects))

# Match with funded projects
count = 0
matched = []

for proj in unique_design:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    if len(proj_words) < 2:
        continue
    
    for fund in funded_names:
        fund_lower = fund.lower()
        
        # Direct match
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count += 1
            matched.append(proj)
            break
        
        # Word overlap
        fund_words = set(fund_lower.split())
        common = proj_words & fund_words
        
        if len(common) >= 3:
            count += 1
            matched.append(proj)
            break

# Return final count
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
