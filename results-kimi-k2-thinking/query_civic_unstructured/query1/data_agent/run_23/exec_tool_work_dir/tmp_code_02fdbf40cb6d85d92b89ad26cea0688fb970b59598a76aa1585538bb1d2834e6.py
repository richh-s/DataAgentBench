code = """import json
import re

# Load funding data (projects > $50,000)
funding_file = var_functions.query_db:74
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(var_functions.query_db:78, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup - map lowercase to original name and amount
funding_lookup = {}
for rec in funding_records:
    try:
        name = rec.get('Project_Name', '').strip()
        amount = int(rec.get('Amount', 0))
        if name and amount > 50000:
            funding_lookup[name.lower()] = {
                'name': name,
                'amount': amount
            }
    except:
        pass

print('Total funded projects > $50K: ' + str(len(funding_lookup)))

# Extract design projects from civic documents
all_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find Design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where Design section ends
    design_end = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)']:
        marker_pos = text.find(marker, design_start + 50)
        if design_start < marker_pos < design_end:
            design_end = marker_pos
    
    design_text = text[design_start:design_end]
    lines = design_text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers and markers
        if any(skip in line for skip in ['cid:', 'Updates:', 'Project Schedule:', 'Page', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Identify project name lines
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify by checking following lines for project context
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'updates:' in next_line or 'project schedule:' in next_line:
                    is_project = True
                    break
            
            if not is_project:
                # Check if line itself is a clear project name
                if any(kw in line for kw in ['Project', 'Improvements', 'Drainage', 'Repairs', 'Study', 'Replacement']):
                    is_project = True
            
            if is_project and line not in all_design_projects:
                all_design_projects.append(line)

print('Design projects extracted: ' + str(len(all_design_projects)))

# Find matches with funding data
matches = []
for project in all_design_projects:
    proj_key = project.lower()
    
    # Direct match
    if proj_key in funding_lookup:
        matches.append({
            'project': project,
            'funding_name': funding_lookup[proj_key]['name'],
            'amount': funding_lookup[proj_key]['amount']
        })
    else:
        # Fuzzy matching - check if project name is similar to funded name
        for fund_key, fund_info in funding_lookup.items():
            # Check if one contains the other
            if (proj_key in fund_key or fund_key in proj_key):
                # Ensure word overlap
                proj_words = set(proj_key.split())
                fund_words = set(fund_key.split())
                shared = proj_words.intersection(fund_words)
                
                if len(shared) >= 2 or len(shared) == len(proj_words):
                    matches.append({
                        'project': project,
                        'funding_name': fund_info['name'],
                        'amount': fund_info['amount']
                    })
                    break

# Remove duplicates based on project name
unique_matches = {}
for match in matches:
    project_name = match['project']
    if project_name not in unique_matches:
        unique_matches[project_name] = match

final_results = list(unique_matches.values())
print('\nMatched projects with funding > $50,000:')
for i, result in enumerate(final_results):
    print(f"{i+1}. {result['project']} - ${result['amount']:,}")

final_count = len(final_results)
print('\nTotal count: ' + str(final_count))

print('__RESULT__:')
print(json.dumps(final_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)
