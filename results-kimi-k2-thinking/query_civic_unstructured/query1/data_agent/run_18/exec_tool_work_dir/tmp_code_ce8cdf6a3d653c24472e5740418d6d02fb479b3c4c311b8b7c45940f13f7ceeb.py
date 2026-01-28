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

# Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Get section end
    remaining = text[design_start:]
    construction_idx = remaining.find('Capital Improvement Projects (Construction)')
    not_started_idx = remaining.find('Capital Improvement Projects (Not Started)')
    
    end_idx = len(remaining)
    if construction_idx > 0:
        end_idx = construction_idx
    elif not_started_idx > 0:
        end_idx = not_started_idx
    
    # Extract design section
    design_section = remaining[:end_idx]
    
    # Get project names - look for lines that are likely project titles
    lines = [line.strip() for line in design_section.split('\n')]
    
    for line in lines:
        # Skip short lines or metadata
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('-') or 'cid:' in line:
            continue
        if 'Updates' in line or 'Schedule' in line or 'Complete Design' in line:
            continue
        
        # Check if line looks like a project name
        project_indicators = ['Project', 'Improvements', 'Repairs', 'Infrastructure', 'Master Plan', 'Study', 'Replacement']
        if any(indicator in line for indicator in project_indicators):
            clean_name = line.replace('\u2022', '').strip()
            if clean_name:
                design_projects.append(clean_name)

# Remove duplicates
design_projects = list(set(design_projects))

# Match with funding data
funding_names = [f['Project_Name'] for f in funding_data]
matching_projects = []

for proj_name in design_projects:
    proj_lower = proj_name.lower()
    
    for fund_name in funding_names:
        fund_lower = fund_name.lower()
        
        # Simple substring matching
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matching_projects.append(proj_name)
            break
        
        # Check word overlap (at least 3 words in common)
        proj_words = set(proj_lower.split())
        fund_words = set(fund_lower.split())
        common = proj_words & fund_words
        
        if len(common) >= 3:
            matching_projects.append(proj_name)
            break

# Result
count = len(matching_projects)
result = {'count': count, 'matching_projects': matching_projects[:10]}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
