code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:30
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:31
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding dictionary for projects > $50K
funding_lookup = {}
for rec in funding_records:
    amt = int(rec.get('Amount', 0))
    if amt > 50000:
        name = rec.get('Project_Name', '').strip()
        if name:
            funding_lookup[name.lower()] = name

print('Funded projects > $50K: ' + str(len(funding_lookup)))

# Extract design projects from civic docs
all_design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find section end
    section_end = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        pos = text.find(marker, design_start + 50)
        if design_start < pos < section_end:
            section_end = pos
    
    design_section = text[design_start:section_end]
    lines = design_section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty/invalid lines
        if not line or len(line) < 10:
            continue
        
        # Skip header lines and markers
        if any(x in line for x in ['cid:', 'Updates:', 'Project Schedule:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Page']):
            continue
        
        # Skip all caps short lines
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Look for potential project names (title case, multiple words)
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify by checking context in following lines
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'updates:' in next_line or 'project schedule:' in next_line:
                    is_project = True
                    break
            
            if not is_project:
                # Also accept lines containing clear project keywords
                if any(k in line for k in ['Project', 'Improvements', 'Drainage', 'Repairs', 'Road', 'Park', 'Study']):
                    is_project = True
            
            if is_project and line not in all_design_projects:
                all_design_projects.append(line)

print('Design projects extracted: ' + str(len(all_design_projects)))

# Match projects with funding
matched_projects = []
for project_name in all_design_projects:
    proj_key = project_name.lower()
    
    # Direct match
    if proj_key in funding_lookup:
        matched_projects.append(project_name)
    else:
        # Fuzzy matching
        for fund_key in funding_lookup:
            # Check containment/suffix matches
            if proj_key in fund_key or fund_key in proj_key:
                # Ensure reasonable word overlap
                proj_words = set(proj_key.split())
                fund_words = set(fund_key.split())
                shared_words = proj_words.intersection(fund_words)
                
                if len(shared_words) >= 2 or len(shared_words) == len(proj_words):
                    matched_projects.append(project_name)
                    break

# Remove duplicates and count
unique_matches = list(set(matched_projects))
print('Final matches found: ' + str(len(unique_matches)))

# Show sample matches
if unique_matches:
    print('\nSample matching projects:')
    for i, proj in enumerate(unique_matches[:min(5, len(unique_matches))]):
        print(str(i+1) + '. ' + proj)

result = len(unique_matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
