code = """import json
import re

# Load funding data
funding_result = var_functions.query_db:1
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Load civic documents
civic_result = var_functions.query_db:2
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

# Extract design projects by looking for project names in the design section
all_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Get the design section with a simpler approach
    sections = text.split('Capital Improvement Projects')
    design_part = ''
    
    for section in sections:
        if '(Design)' in section and not design_part:
            design_part = section
            # Stop at the next major section
            if 'Capital Improvement Projects' in section[20:]:
                break_point = section.find('Capital Improvement Projects', 20)
                if break_point > 0:
                    design_part = section[:break_point]
            break
    
    if not design_part:
        continue
    
    # Extract project names from the design section
    lines = [line.strip() for line in design_part.split('\n')]
    for line in lines:
        if len(line) < 10 or 'cid:' in line or ':' in line:
            continue
        if line.startswith('(') or line.startswith('-'):
            continue
        if 'Schedule' in line or 'Updates' in line:
            continue
        
        # Check for project indicators
        indicators = ['Project', 'Improvements', 'Repairs', 'Master Plan', 'Study', 'Infrastructure', 'Replacement']
        if any(indicator in line for indicator in indicators):
            clean_line = re.sub(r'^\W+', '', line)
            if clean_line:
                all_design_projects.append(clean_line)

# Remove duplicates
design_projects = list(set(all_design_projects))

# Get funding project names
funding_names = [f['Project_Name'] for f in funding_data]

# Find matches
matches = []
for proj in design_projects:
    proj_words = set(proj.lower().split())
    for fund in funding_names:
        fund_words = set(fund.lower().split())
        
        if proj in fund or fund in proj:
            matches.append(proj)
            break
            
        common = proj_words & fund_words
        if len(common) >= 3:
            matches.append(proj)
            break

result_count = len(matches)

# Print result
output = json.dumps(result_count)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
