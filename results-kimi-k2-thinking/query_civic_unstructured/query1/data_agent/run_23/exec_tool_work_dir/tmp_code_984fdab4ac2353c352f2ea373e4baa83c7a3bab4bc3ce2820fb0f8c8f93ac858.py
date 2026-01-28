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

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

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

print(f"Projects with funding > $50,000: {len(funding_dict)}")

# Extract project information from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects sections
    # Pattern: Capital Improvement Projects (Design) followed by project listings
    
    # Find the design section
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY PROJECTS|$)'
    design_match = re.search(design_section_pattern, text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        design_text = design_match.group(1)
        
        # Extract project names - they typically appear as:
        # 1. Project name on its own line
        # 2. Followed by updates or schedule
        
        # Split by lines and look for project name patterns
        lines = design_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and common headers
            if (not line or 
                line.startswith('(') or 
                line.startswith('cid:') or 
                line in ['Updates:', 'Project Schedule:', 'Estimated Schedule:'] or
                'Complete Design:' in line or
                'Advertise:' in line or
                'Begin Construction:' in line):
                i += 1
                continue
            
            # Look for project names (typically title case or uppercase, not bullet points)
            if (len(line) > 10 and 
                not line.startswith('•') and 
                not line.startswith('-') and
                not line.startswith('□') and
                not line.isupper() and  # Skip all uppercase lines like "PAGE"
                any(word[0].isupper() for word in line.split()[:3]) and  # At least some title case
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
                        'complete design:' in next_line):
                        
                        project_name = line.strip()
                        capital_design_projects.append({
                            'project_name': project_name,
                            'status': 'design',
                            'type': 'capital',
                            'source_doc': doc.get('filename')
                        })
            
            i += 1

print(f"Capital projects with 'design' status found: {len(capital_design_projects)}")

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
        # Try fuzzy matching - check if any funded project name contains this project name
        # or vice versa
        for funded_name in funding_dict.keys():
            if (proj_name in funded_name or 
                funded_name in proj_name or
                # Check for common variations
                re.sub(r'\s+', ' ', proj_name.lower()) in re.sub(r'\s+', ' ', funded_name.lower()) or
                re.sub(r'\s+', ' ', funded_name.lower()) in re.sub(r'\s+', ' ', proj_name.lower())):
                
                matches.append({
                    'project_name': proj_name,
                    'funded_name': funded_name,
                    'funding_amount': funding_dict[funded_name]['amount'],
                    'funding_source': funding_dict[funded_name]['source'],
                    'status': 'design',
                    'type': 'capital'
                })
                break

# Remove duplicates
unique_matches = {}
for match in matches:
    key = match['project_name']
    if key not in unique_matches:
        unique_matches[key] = match

final_matches = list(unique_matches.values())
print(f"Matches with funding > $50,000: {len(final_matches)}")

# Print some examples for debugging
if final_matches:
    print("\nExample matches:")
    for i, match in enumerate(final_matches[:5]):
        print(f"{i+1}. {match['project_name']} - ${match['funding_amount']:,}")

result = len(final_matches)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
