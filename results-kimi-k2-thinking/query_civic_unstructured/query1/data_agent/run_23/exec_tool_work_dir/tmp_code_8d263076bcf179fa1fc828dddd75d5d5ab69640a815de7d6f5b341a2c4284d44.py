code = """import json
import re

# Load funding data
with open('var_functions.query_db:45', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('var_functions.query_db:44', 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for projects > $50K
funding_lookup = {}
for rec in funding_data:
    name = rec.get('Project_Name', '').strip()
    amount = int(rec.get('Amount', 0))
    if name and amount > 50000:
        funding_lookup[name.lower()] = {'original_name': name, 'amount': amount}

print('Total funded projects > $50K:', len(funding_lookup))

# Extract capital design projects from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where the Design section ends
    section_end = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        pos = text.find(marker, design_start + 50)
        if design_start < pos < section_end:
            section_end = pos
    
    design_section = text[design_start:section_end]
    lines = design_section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers and markers
        if any(skip in line for skip in ['cid:', 'Updates:', 'Project Schedule:', 'Page', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
            continue
        
        # Skip short uppercase lines
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Look for project names (title case, multiple words)
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify by checking following lines
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'updates:' in next_line or 'project schedule:' in next_line:
                    is_project = True
                    break
            
            # Also accept lines with project keywords
            if not is_project:
                project_keywords = ['Project', 'Improvements', 'Drainage', 'Repairs', 'Study', 'Replacement', 'System', 'Road', 'Park']
                if any(kw in line for kw in project_keywords):
                    is_project = True
            
            if is_project and line not in capital_design_projects:
                capital_design_projects.append(line)

print('Capital design projects found:', len(capital_design_projects))

# Match projects with funding
matched_projects = []
for project in capital_design_projects:
    proj_key = project.lower()
    
    # Direct match
    if proj_key in funding_lookup:
        matched_projects.append({
            'project': project,
            'funding_name': funding_lookup[proj_key]['original_name'],
            'amount': funding_lookup[proj_key]['amount']
        })
    else:
        # Fuzzy matching
        for fund_key, fund_info in funding_lookup.items():
            # Check if project names overlap
            if proj_key in fund_key or fund_key in proj_key:
                # Check word overlap
                proj_words = set(proj_key.split())
                fund_words = set(fund_key.split())
                shared = proj_words.intersection(fund_words)
                
                if len(shared) >= 2 or len(shared) == len(proj_words):
                    matched_projects.append({
                        'project': project,
                        'funding_name': fund_info['original_name'],
                        'amount': fund_info['amount']
                    })
                    break

# Remove duplicates
unique_projects = {}
for match in matched_projects:
    proj_name = match['project']
    if proj_name not in unique_projects:
        unique_projects[proj_name] = match

final_count = len(unique_projects)
print('\nFinal count:', final_count)

# Show some examples
print('\nSample matched projects:')
for i, (name, info) in enumerate(list(unique_projects.items())[:5]):
    print(f"{i+1}. {name}")

print('__RESULT__:')
print(json.dumps(final_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:45': 'file_storage/functions.query_db:45.json'}

exec(code, env_args)
