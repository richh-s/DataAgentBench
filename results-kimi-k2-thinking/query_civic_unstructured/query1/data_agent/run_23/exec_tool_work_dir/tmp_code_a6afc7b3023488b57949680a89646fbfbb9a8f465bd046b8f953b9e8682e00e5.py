code = """import json
import re

# Load the funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the filtered civic documents (ones that contain Design section)
civic_file = var_functions.query_db:8
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create a dictionary of projects with funding > 50000
funding_dict = {}
for record in funding_data:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            project_name = record.get('Project_Name', '').strip()
            funding_dict[project_name.lower()] = {
                'original_name': project_name,
                'funding_id': record.get('Funding_ID'),
                'amount': amount,
                'source': record.get('Funding_Source')
            }
    except (ValueError, TypeError):
        continue

print('Projects with funding > $50,000: ' + str(len(funding_dict)))

# Extract capital design projects from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    not_started_start = text.find('Capital Improvement Projects (Not Started)')
    
    if design_start == -1:
        continue
    
    # Determine section boundaries
    end_pos = len(text)
    if construction_start > design_start:
        end_pos = min(end_pos, construction_start)
    if not_started_start > design_start:
        end_pos = min(end_pos, not_started_start)
    
    design_section = text[design_start:end_pos]
    
    # Extract project names - look for lines that are project titles
    lines = design_section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty/invalid lines
        if not line or len(line) < 10:
            continue
        
        # Skip common headers and markers
        skip_patterns = [
            'cid:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:',
            'Complete Design:', 'Advertise:', 'Begin Construction:',
            'RECOMMENDED ACTION:', 'DISCUSSION:', 'Page ', 'of 6',
            'Capital Improvement Projects', 'Project Description:'
        ]
        
        if any(pattern in line for pattern in skip_patterns):
            continue
        
        # Skip lines that are all uppercase (like PAGE HEADERS)
        if line.isupper() and len(line.split()) <= 5:
            continue
        
        # Skip bullet points and special characters
        if line.startswith(('•', '-', '□', '(', ')', '*')):
            continue
        
        # Project names typically:
        # - Have multiple words
        # - Start with capital letters
        # - Not just numbers/dates
        # - Followed by project-related content
        
        words = line.split()
        if len(words) < 2:
            continue
        
        # Check if line starts with capital letter and has mixed case
        if not line[0].isupper():
            continue
        
        # Check if next line contains project-related keywords
        has_project_context = False
        if i + 1 < len(lines):
            next_line = lines[i+1].lower()
            context_keywords = [
                'updates:', 'project schedule:', 'estimated schedule:',
                'staff', 'city', 'project', 'complete design:',
                'advertise:', 'begin construction:', 'plans'
            ]
            has_project_context = any(keyword in next_line for keyword in context_keywords)
        
        # Alternative: check if the line looks like a project name (ends with 'Project', etc.)
        is_likely_project = (
            line.endswith(('Project', 'Improvements', 'Repairs', 'Drainage', 
                          'Study', 'Replacement', 'Upgrades', 'System')) or
            'Improvements' in line or 'Drainage' in line or 'Repairs' in line
        )
        
        if has_project_context or is_likely_project:
            capital_design_projects.append(line.strip())

# Remove duplicates
capital_design_projects = list(set(capital_design_projects))
print('Capital design projects found: ' + str(len(capital_design_projects)))

# Now match with funding
matches = []

for project_name in capital_design_projects:
    proj_key = project_name.lower()
    
    # Direct match
    if proj_key in funding_dict:
        matches.append({
            'project_name': project_name,
            'funded_name': funding_dict[proj_key]['original_name'],
            'funding_amount': funding_dict[proj_key]['amount'],
            'status': 'design',
            'type': 'capital'
        })
    else:
        # Fuzzy matching - check if project name is contained in funded name or vice versa
        for funded_key, funded_info in funding_dict.items():
            # Check if one contains the other
            if (proj_key in funded_key or funded_key in proj_key):
                # Additional check: avoid matching very short/common words
                if len(proj_key.split()) >= 2:
                    matches.append({
                        'project_name': project_name,
                        'funded_name': funded_info['original_name'],
                        'funding_amount': funded_info['amount'],
                        'status': 'design',
                        'type': 'capital'
                    })
                    break

# Remove duplicates based on project_name
unique_matches = []
seen_projects = set()

for match in matches:
    if match['project_name'] not in seen_projects:
        unique_matches.append(match)
        seen_projects.add(match['project_name'])

print('Final matches: ' + str(len(unique_matches)))

if unique_matches:
    print('\nExample matches:')
    for i, match in enumerate(unique_matches[:5]):
        print(str(i+1) + '. ' + match['project_name'] + ' - $' + str(match['funding_amount']))

result = len(unique_matches)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
