code = """import json
import re

# Load data
funding_file = var_functions.query_db:1
civic_file = var_functions.query_db:2

with open(funding_file) as f:
    funding_data = json.load(f)
with open(civic_file) as f:
    civic_docs = json.load(f)

print('Funding records count:', len(funding_data))
print('Civic documents count:', len(civic_docs))

# Extract design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Find the design section
        design_start = text.find('Capital Improvement Projects (Design)')
        remaining = text[design_start:]
        
        # Find where design section ends
        construction_idx = remaining.find('Capital Improvement Projects (Construction)')
        not_started_idx = remaining.find('Capital Improvement Projects (Not Started)')
        
        if construction_idx > 0:
            design_section = remaining[:construction_idx]
        elif not_started_idx > 0:
            design_section = remaining[:not_started_idx]
        else:
            design_section = remaining
        
        # Extract project names - lines that look like titles
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip if too short or contains certain patterns
            if len(line) < 10:
                continue
            if line.startswith('(') or 'cid:' in line or 'Updates' in line:
                continue
            if 'Schedule:' in line or 'Complete Design:' in line:
                continue
                
            # Look for project-like names
            if any(key in line for key in ['Project', 'Improvements', 'Repairs', 'Master Plan', 'Study']):
                # Clean the line
                clean_line = line.replace('\u2022', '').replace('-', '').strip()
                if clean_line:
                    design_projects.append(clean_line)

# Remove duplicates
unique_projects = list(set(design_projects))
print('Unique design projects extracted:', len(unique_projects))

# Get funding project names
funding_names = [f['Project_Name'] for f in funding_data]

# Match projects
matched_projects = []
matched_count = 0

for proj in unique_projects:
    proj_words = set(proj.lower().split())
    if len(proj_words) < 2:
        continue
        
    for fund_name in funding_names:
        # Direct string match
        if proj in fund_name or fund_name in proj:
            if proj not in matched_projects:
                matched_projects.append(proj)
                matched_count += 1
            break
            
        # Word overlap
        fund_words = set(fund_name.lower().split())
        if len(proj_words & fund_words) >= 3:
            if proj not in matched_projects:
                matched_projects.append(proj)
                matched_count += 1
            break

print('Final matched count:', matched_count)
print('Sample matched projects:', matched_projects[:5])

result = {'count': matched_count, 'sample_projects': matched_projects[:5]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
