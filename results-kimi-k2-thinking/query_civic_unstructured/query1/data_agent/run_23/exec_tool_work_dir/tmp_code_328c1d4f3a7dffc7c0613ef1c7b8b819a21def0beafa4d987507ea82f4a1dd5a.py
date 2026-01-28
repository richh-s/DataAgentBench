code = """import json
import re

# Load funding data
funding_file = 'var_functions.query_db:74'
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = 'var_functions.query_db:78'
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name', '').strip()
    amount = int(rec.get('Amount', 0))
    if name and amount > 50000:
        funding_lookup[name.lower()] = {'name': name, 'amount': amount}

print(f'Funding projects > $50K: {len(funding_lookup)}')

# Extract design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find section end
    design_end = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        marker_pos = text.find(marker, design_start + 50)
        if design_start < marker_pos < design_end:
            design_end = marker_pos
    
    design_section = text[design_start:design_end]
    lines = design_section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        if any(skip in line for skip in ['cid:', 'Updates:', 'Project Schedule:', 'Page']):
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Check if project name
        if line[0].isupper() and len(line.split()) >= 2:
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'updates:' in next_line or 'project schedule:' in next_line:
                    is_project = True
                    break
            
            if not is_project:
                if any(kw in line for kw in ['Project', 'Improvements', 'Drainage', 'Repairs', 'Study']):
                    is_project = True
            
            if is_project and line not in design_projects:
                design_projects.append(line)

print(f'Design projects: {len(design_projects)}')

# Match projects
matches = []
for project in design_projects:
    proj_key = project.lower()
    if proj_key in funding_lookup:
        matches.append(project)
    else:
        for fund_key in funding_lookup:
            if proj_key in fund_key or fund_key in proj_key:
                proj_words = set(proj_key.split())
                fund_words = set(fund_key.split())
                if len(proj_words.intersection(fund_words)) >= 2:
                    matches.append(project)
                    break

unique_matches = list(set(matches))
print(f'Final matches: {len(unique_matches)}')

# Show sample
for i, proj in enumerate(unique_matches[:5]):
    print(f'{i+1}. {proj}')

result = len(unique_matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)
