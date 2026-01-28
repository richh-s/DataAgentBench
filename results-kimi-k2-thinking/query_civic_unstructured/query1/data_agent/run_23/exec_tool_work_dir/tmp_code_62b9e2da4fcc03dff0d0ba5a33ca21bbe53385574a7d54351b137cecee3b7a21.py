code = """import json

# Load the funding data
with open('var_functions.query_db:30', 'r') as f:
    funding_data = json.load(f)

# Load the civic documents
with open('var_functions.query_db:31', 'r') as f:
    civic_docs = json.load(f)

# Create a set of funded project names (lowercase for matching)
funded_projects = {}
for rec in funding_data:
    name = rec.get('Project_Name', '').strip()
    if name:
        funded_projects[name.lower()] = name

print('Total funded projects > $50K: ' + str(len(funded_projects)))

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where it ends
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    not_started_start = text.find('Capital Improvement Projects (Not Started)', design_start)
    
    end_pos = len(text)
    if construction_start > design_start:
        end_pos = min(end_pos, construction_start)
    if not_started_start > design_start:
        end_pos = min(end_pos, not_started_start)
    
    design_section = text[design_start:end_pos]
    
    # Find projects by pattern matching
    import re
    # Look for lines that are likely project names
    lines = design_section.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        if any(x in line for x in ['cid:', 'Updates:', 'Project Schedule:', 'Page']):
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Check if this is a project name
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify by looking ahead
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'updates:' in next_line or 'project schedule:' in next_line:
                    is_project = True
                    break
            
            if not is_project:
                # Check if line contains project keywords
                if any(kw in line for kw in ['Project', 'Improvements', 'Repairs', 'Drainage', 'System']):
                    is_project = True
            
            if is_project and line not in design_projects:
                design_projects.append(line)

print('Capital design projects found in documents: ' + str(len(design_projects)))

# Match with funding
matched = []
for proj in design_projects:
    proj_key = proj.lower()
    if proj_key in funded_projects:
        matched.append(proj)
    else:
        # Try partial matching
        for funded_key in funded_projects:
            if proj_key in funded_key or funded_key in proj_key:
                # Share words
                proj_words = set(proj_key.split())
                funded_words = set(funded_key.split())
                if len(proj_words.intersection(funded_words)) >= 2:
                    matched.append(proj)
                    break

unique_matched = list(set(matched))
print('Matched projects with funding: ' + str(len(unique_matched)))

# Show sample matches
if unique_matched:
    print('\nSample matches:')
    for i, p in enumerate(unique_matched[:8]):
        print(str(i+1) + '. ' + p)

result = len(unique_matched)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
