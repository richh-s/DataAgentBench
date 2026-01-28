code = """import json
import re

# Load data
funding_result = var_functions.query_db:1
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Load civic docs
civic_result = var_functions.query_db:2
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

# Extract capital projects with design status
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for design section
    design_text = ''
    
    # Method 1: Find design section
    start_marker = 'Capital Improvement Projects (Design)'
    start = text.find(start_marker)
    
    if start >= 0:
        section_after = text[start:]
        end_markers = [
            'Capital Improvement Projects (Construction)',
            'Capital Improvement Projects (Not Started)',
            'Disaster Recovery Projects',
            '\\n\\n\\n'  # Triple newline
        ]
        
        end_pos = len(section_after)
        for marker in end_markers:
            pos = section_after.find(marker)
            if pos > 0 and pos < end_pos:
                end_pos = pos
        
        design_text = section_after[:end_pos]
    
    # Extract potential project names
    lines = [l.strip() for l in design_text.split('\n')]
    for line in lines:
        # Skip metadata
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('-') or 'cid:' in line:
            continue
        skip_words = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Project Description']
        if any(word in line for word in skip_words):
            continue
        
        # Project name indicators
        indicators = ['Project', 'Improvements', 'Repairs', 'Master Plan', 'Study', 'Infrastructure', 'Replacement']
        if any(indicator in line for indicator in indicators):
            # Clean line
            clean = re.sub(r'[^\w\s]', '', line)
            clean = clean.strip()
            if clean:
                all_projects.append(clean)

# Remove duplicates
unique_design = list(set(all_projects))

# Get funding project names
funding_projects = [f['Project_Name'] for f in funding_data]

# Match projects
matched = []
for proj_name in unique_design:
    proj_lower = proj_name.lower()
    proj_parts = set(proj_lower.split())
    
    for fund_name in funding_projects:
        fund_lower = fund_name.lower()
        fund_parts = set(fund_lower.split())
        
        # Direct match
        if proj_name in fund_name or fund_name in proj_name:
            matched.append(proj_name)
            break
        
        # Word overlap
        common = proj_parts & fund_parts
        if len(common) >= 3:
            matched.append(proj_name)
            break

# Get final count
count = len(matched)

# Return result
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
