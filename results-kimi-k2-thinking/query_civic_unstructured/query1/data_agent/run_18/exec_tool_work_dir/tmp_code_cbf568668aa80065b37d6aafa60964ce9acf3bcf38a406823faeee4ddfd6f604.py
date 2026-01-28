code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:1
civic_file = var_functions.query_db:2

with open(funding_file) as f:
    funding_data = json.load(f)
with open(civic_file) as f:
    civic_docs = json.load(f)

# Extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section boundaries
    start_marker = 'Capital Improvement Projects (Design)'
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    
    start_pos = text.find(start_marker)
    if start_pos < 0:
        continue
    
    # Find section end
    section_text = text[start_pos:]
    end_pos = len(section_text)
    for marker in end_markers:
        marker_pos = section_text.find(marker)
        if marker_pos > 0 and marker_pos < end_pos:
            end_pos = marker_pos
    
    design_section = section_text[:end_pos]
    
    # Extract project names
    for line in design_section.splitlines():
        line = line.strip()
        if len(line) < 10 or line.startswith('(') or 'cid:' in line:
            continue
        if 'Updates' in line or 'Schedule' in line or 'Complete Design' in line:
            continue
        
        # Check if line contains project indicators
        indicators = ['Project', 'Improvements', 'Repairs', 'Master Plan', 'Study']
        if any(indicator in line for indicator in indicators):
            clean = re.sub(r'[^A-Za-z0-9\s]', '', line)
            clean = clean.strip()
            if clean:
                design_projects.append(clean)

# Remove duplicates  
design_projects = list(set(design_projects))

# Get funding project names
funded_names = [f['Project_Name'] for f in funding_data]

# Match projects
matched = []
for proj in design_projects:
    for fund in funded_names:
        # Case-insensitive match
        proj_lower = proj.lower()
        fund_lower = fund.lower()
        
        # Direct substring match
        if proj in fund or fund in proj:
            matched.append(proj)
            break
        
        # Word overlap (3+ words)
        proj_words = set(proj_lower.split())
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            matched.append(proj)
            break

# Result
count = len(matched)

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
