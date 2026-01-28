code = """import json
import re

# Load data from the variable keys
with open(var_functions.query_db:30, 'r') as f:
    funding_data = json.load(f)

with open(var_functions.query_db:31, 'r') as f:
    civic_docs = json.load(f)

# Create funding dictionary for projects > $50K
funding_dict = {}
for rec in funding_data:
    try:
        amount = int(rec.get('Amount', 0))
        if amount > 50000:
            name = rec.get('Project_Name', '').strip()
            if name:
                funding_dict[name.lower()] = {
                    'original_name': name,
                    'amount': amount
                }
    except:
        pass

print('Funding projects > $50K: ' + str(len(funding_dict)))

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section and extract project names
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find section end
    end_pos = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'DISASTER RECOVERY PROJECTS']:
        marker_pos = text.find(marker, design_start + 50)
        if marker_pos > design_start and marker_pos < end_pos:
            end_pos = marker_pos
    
    design_section = text[design_start:end_pos]
    lines = design_section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers and markers
        skip_terms = ['cid:', 'Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Page', 'RECOMMENDED ACTION:', 'DISCUSSION:']
        if any(term in line for term in skip_terms):
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Check if this is a project name
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify it's a project by checking following lines for project context
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'updates:' in next_line or 'project schedule:' in next_line or 'staff' in next_line or 'city' in next_line:
                    is_project = True
                    break
            
            # Also accept lines with project naming patterns
            if not is_valid:
                proj_indicators = ['Project', 'Improvements', 'Repairs', 'Drainage', 'System', 'Replacement', 'Road', 'Park', 'Study']
                is_project = any(indicator in line for indicator in proj_indicators)
            
            if is_project and line not in design_projects:
                design_projects.append(line)

print('Capital design projects found: ' + str(len(design_projects)))

# Match with funding
matched = []
for project in design_projects:
    project_key = project.lower()
    
    if project_key in funding_dict:
        matched.append(project)
    else:
        # Fuzzy matching - check for overlap
        for fund_key, fund_info in funding_dict.items():
            # Check containment with reasonable word overlap
            if project_key in fund_key or fund_key in project_key:
                proj_words = set(project_key.split())
                fund_words = set(fund_key.split())
                shared = proj_words.intersection(fund_words)
                if len(shared) >= 2 or len(shared) == len(proj_words):
                    matched.append(project)
                    break

# Remove duplicates
unique_matches = list(set(matched))
print('Final matches: ' + str(len(unique_matches)))

# Print sample matches
if unique_matches:
    print('\nSample matches:')
    for i, proj in enumerate(unique_matches[:8]):
        print(str(i+1) + '. ' + proj)

result = len(unique_matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
