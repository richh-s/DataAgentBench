code = """import json
import re

# Load the funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents
civic_file = var_functions.query_db:1
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Funding records: ' + str(len(funding_data)))
print('Civic documents: ' + str(len(civic_docs)))

# Create a dictionary of projects with funding > 50000
funding_dict = {}
for record in funding_data:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            project_name = record.get('Project_Name', '').strip()
            funding_dict[project_name] = {
                'funding_id': record.get('Funding_ID'),
                'amount': amount,
                'source': record.get('Funding_Source')
            }
    except (ValueError, TypeError):
        continue

print('Projects with funding > $50,000: ' + str(len(funding_dict)))

# Extract project information from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects sections
    design_section_start = text.find('Capital Improvement Projects (Design)')
    construction_section_start = text.find('Capital Improvement Projects (Construction)')
    not_started_section_start = text.find('Capital Improvement Projects (Not Started)')
    
    if design_section_start != -1:
        # Determine where the design section ends
        end_positions = []
        if construction_section_start != -1 and construction_section_start > design_section_start:
            end_positions.append(construction_section_start)
        if not_started_section_start != -1 and not_started_section_start > design_section_start:
            end_positions.append(not_started_section_start)
        
        if end_positions:
            design_section_end = min(end_positions)
            design_text = text[design_section_start:design_section_end]
        else:
            design_text = text[design_section_start:]
        
        # Split by lines and look for project name patterns
        lines = design_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and common headers
            if (not line or 
                line.startswith('(') or 
                'cid:' in line or
                line in ['Updates:', 'Project Schedule:', 'Estimated Schedule:'] or
                'Complete Design:' in line or
                'Advertise:' in line or
                'Begin Construction:' in line):
                i += 1
                continue
            
            # Look for project names (typically title case, not bullet points)
            if (len(line) > 10 and 
                not line.startswith('•') and 
                not line.startswith('-') and
                not line.startswith('□') and
                not line.isupper() and  # Skip all uppercase lines like PAGE
                len(line.split()) >= 2):  # At least 2 words
                
                # Check if next line has project-related keywords
                if i + 1 < len(lines):
                    next_line = lines[i+1].strip().lower()
                    if ('updates:' in next_line or 
                        'project schedule:' in next_line or
                        'estimated schedule:' in next_line or
                        'staff' in next_line or
                        'city' in next_line or
                        'project' in next_line or
                        'complete design:' in next_line or
                        i+2 < len(lines) and ('updates:' in lines[i+2].lower() or 
                                           'project schedule:' in lines[i+2].lower())):
                        
                        project_name = line.strip()
                        # Clean up common formatting issues
                        if project_name and not project_name.isdigit():
                            capital_design_projects.append({
                                'project_name': project_name,
                                'status': 'design',
                                'type': 'capital',
                                'source_doc': doc.get('filename')
                            })
            
            i += 1

print('Capital projects with design status found: ' + str(len(capital_design_projects)))

# Show some extracted projects for debugging
# print('Sample extracted projects:')
# for p in capital_design_projects[:10]:
#     print('  - ' + p['project_name'])

# Now match with funding data
matches = []
for project in capital_design_projects:
    proj_name = project['project_name']
    
    # Direct match
    if proj_name in funding_dict:
        matches.append({
            'project_name': proj_name,
            'funding_amount': funding_dict[proj_name]['amount'],
            'funding_source': funding_dict[proj_name]['source'],
            'status': 'design',
            'type': 'capital'
        })
    else:
        # Try variations
        proj_name_clean = re.sub(r'\s+', ' ', proj_name.lower().strip())
        
        for funded_name in funding_dict.keys():
            funded_name_clean = re.sub(r'\s+', ' ', funded_name.lower().strip())
            
            # Check if one is contained in the other
            if (proj_name_clean in funded_name_clean or 
                funded_name_clean in proj_name_clean):
                
                # Avoid matching very short substrings within unrelated names
                if len(proj_name_clean.split()) >= 2:
                    matches.append({
                        'project_name': proj_name,
                        'funded_name': funded_name,
                        'funding_amount': funding_dict[funded_name]['amount'],
                        'funding_source': funding_dict[funded_name]['source'],
                        'status': 'design',
                        'type': 'capital'
                    })
                    break

# Remove duplicates based on project_name
unique_matches = {}
for match in matches:
    key = match['project_name']
    if key not in unique_matches:
        unique_matches[key] = match

final_matches = list(unique_matches.values())
print('Matches with funding > $50,000: ' + str(len(final_matches)))

# Print some examples for debugging
if final_matches:
    print('\nExample matches:')
    for i, match in enumerate(final_matches[:5]):
        print(str(i+1) + '. ' + match['project_name'] + ' - $' + str(match['funding_amount']))

result = len(final_matches)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
