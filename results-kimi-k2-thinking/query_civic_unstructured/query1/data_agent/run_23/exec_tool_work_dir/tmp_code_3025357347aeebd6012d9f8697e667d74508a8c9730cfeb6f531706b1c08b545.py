code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:18
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
civic_file = var_functions.query_db:19
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding dictionary (amount > 50000)
funding_dict = {}
for rec in funding_data:
    try:
        amount = int(rec.get('Amount', 0))
        if amount > 50000:
            name = rec.get('Project_Name', '').strip()
            if name:
                funding_dict[name.lower()] = {'original': name, 'amount': amount}
    except:
        continue

print('Funding projects > $50K: ' + str(len(funding_dict)))

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_idx = text.find('Capital Improvement Projects (Design)')
    if design_idx == -1:
        continue
    
    # Find where design section ends
    constr_idx = text.find('Capital Improvement Projects (Construction)', design_idx)
    notstart_idx = text.find('Capital Improvement Projects (Not Started)', design_idx)
    
    end_idx = len(text)
    if constr_idx > design_idx:
        end_idx = min(end_idx, constr_idx)
    if notstart_idx > design_idx:
        end_idx = min(end_idx, notstart_idx)
    
    design_section = text[design_idx:end_idx]
    lines = design_section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers and markers
        skip_markers = ['cid:', 'Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Page']
        if any(marker in line for marker in skip_markers):
            continue
        
        # Skip short uppercase lines
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Look for project names (title case, multiple words)
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify by checking following lines
            is_valid = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line_lower = lines[j].lower()
                if 'updates:' in next_line_lower or 'project schedule:' in next_line_lower:
                    is_valid = True
                    break
            
            # Also accept common project naming patterns
            if not is_valid:
                proj_indicators = ['Project', 'Improvements', 'Repairs', 'Drainage', 'Study', 'Replacement', 'System']
                is_valid = any(indicator in line for indicator in proj_indicators)
            
            if is_valid and line not in design_projects:
                design_projects.append(line)

print('Capital design projects found: ' + str(len(design_projects)))

# Match projects with funding
matched_projects = []
for project in design_projects:
    project_key = project.lower()
    
    # Direct match
    if project_key in funding_dict:
        matched_projects.append(project)
    else:
        # Fuzzy matching - check for name overlap
        for fund_key, fund_info in funding_dict.items():
            # Check if one name contains the other
            if project_key in fund_key or fund_key in project_key:
                # Ensure at least 2 words match
                proj_words = set(project_key.split())
                fund_words = set(fund_key.split())
                if len(proj_words.intersection(fund_words)) >= 2:
                    matched_projects.append(project)
                    break

# Remove duplicates
unique_matches = list(set(matched_projects))
print('Matched projects: ' + str(len(unique_matches)))

# Print sample matches
if unique_matches:
    print('\nSample matches:')
    for i in range(min(5, len(unique_matches))):
        print(str(i+1) + '. ' + unique_matches[i])

result = len(unique_matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json'}

exec(code, env_args)
