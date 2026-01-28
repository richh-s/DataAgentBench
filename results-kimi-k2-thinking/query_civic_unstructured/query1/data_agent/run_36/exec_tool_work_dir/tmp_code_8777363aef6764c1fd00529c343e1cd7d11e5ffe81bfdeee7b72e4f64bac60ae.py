code = """import json
import re

# Load the full results from both queries

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_file = var_functions.query_db:2
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Filter funding > $50,000
high_funding = [f for f in funding_data if f['Amount'] and int(f['Amount']) > 50000]

print(f"Total funding records: {len(funding_data)}")
print(f"Funding records > $50,000: {len(high_funding)}")
print(f"Number of civic documents: {len(civic_docs)}")

# Extract project information from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects (Design) section
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|DISASTER RECOVERY PROJECTS|Disaster Recovery Projects|$)'
    
    design_section_match = re.search(design_section_pattern, text, re.DOTALL | re.IGNORECASE)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Extract project names - look for standalone lines followed by project details
        lines = design_section.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and markers
            if not line or line in ['•', '●', '■', '□']:
                i += 1
                continue
            
            # Check if this line is likely a project name
            # Look ahead for indicators of project details
            if (i + 1 < len(lines) and 
                ('Updates:' in lines[i+1] or 'Project Schedule' in lines[i+1] or 
                 'cid:' in lines[i+1])):
                
                # Clean up the project name
                proj_name = line.strip()
                
                # Remove leading special characters and normalize spaces
                proj_name = re.sub(r'^[^a-zA-Z0-9]*', '', proj_name)
                proj_name = re.sub(r'\s+', ' ', proj_name)
                
                # Filter out noise and common phrases
                if (len(proj_name) > 5 and 
                    'Subject:' not in proj_name and
                    'RECOMMENDED ACTION' not in proj_name):
                    
                    capital_design_projects.append({
                        'project_name': proj_name,
                        'status': 'design',
                        'type': 'capital',
                        'source_doc': doc.get('filename', '')
                    })
            
            i += 1

print(f"\nFound {len(capital_design_projects)} capital projects with design status:")
for proj in capital_design_projects[:15]:
    print(f"  - {proj['project_name']}")

if len(capital_design_projects) > 15:
    print(f"  ... and {len(capital_design_projects) - 15} more")

# Now match these projects with funding > $50,000
project_names_from_docs = [p['project_name'].lower() for p in capital_design_projects]
funding_matches = []

for funding in high_funding:
    funding_proj_name = funding['Project_Name'].lower()
    
    # Look for exact or partial matches
    for doc_proj in capital_design_projects:
        doc_name = doc_proj['project_name'].lower()
        
        # Check if one name contains the other (allowing for variations)
        if (doc_name in funding_proj_name or funding_proj_name in doc_name):
            funding_matches.append({
                'project_name': doc_proj['project_name'],
                'funding_amount': int(funding['Amount']),
                'funding_id': funding['Funding_ID']
            })
            break

print(f"\nFound {len(funding_matches)} matches between design projects and funding > $50,000:")
for match in funding_matches:
    print(f"  - {match['project_name']}: ${match['funding_amount']:,}")

result = {
    'total_capital_design_projects': len(capital_design_projects),
    'projects_with_high_funding': len(funding_matches),
    'matching_projects': funding_matches
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
