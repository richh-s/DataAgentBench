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

# Let's extract project information from civic documents
# Strategy: look for projects under "Capital Improvement Projects (Design)" sections
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects (Design) section
    # Pattern: find the section header, then extract project names until next major section
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|DISASTER RECOVERY PROJECTS|Disaster Recovery Projects|$)'
    
    design_section_match = re.search(design_section_pattern, text, re.DOTALL | re.IGNORECASE)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Extract project names - they typically appear as standalone lines or after bullet points
        # Look for patterns like project names followed by updates or schedule
        lines = design_section.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and common markers
            if not line or line in ['•', '●', '■', '□', '■', '●']:
                i += 1
                continue
            
            # Look for project name patterns
            # Project names are typically followed by "(cid:" or "Updates:" or "Project Schedule"
            if (i + 1 < len(lines) and 
                ('Updates:' in lines[i+1] or 'Project Schedule' in lines[i+1] or 
                 'cid:' in lines[i+1] or lines[i+1].strip().startswith('•'))):
                
                # Clean up the project name
                proj_name = line.strip()
                
                # Remove common prefixes/suffixes
                proj_name = re.sub(r'^[^a-zA-Z]*', '', proj_name)  # Remove leading non-letters
                proj_name = re.sub(r'\s+', ' ', proj_name)  # Normalize spaces
                
                if len(proj_name) > 5:  # Filter out short noise
                    capital_design_projects.append({
                        'project_name': proj_name,
                        'status': 'design',
                        'type': 'capital',
                        'source_doc': doc.get('filename', '')
                    })
                    
                    # Skip to next project (skip the details lines)
                    while i < len(lines) and not (lines[i].strip() and 
                                                   not lines[i].strip().startswith('•') and
                                                   not lines[i].strip().startswith('cid:') and
                                                   'Updates:' not in lines[i] and
                                                   'Project Schedule' not in lines[i]):
                        i += 1
                    continue
            
            i += 1

print(f"\nFound {len(capital_design_projects)} capital projects with design status:")
for proj in capital_design_projects[:10]:  # Show first 10
    print(f"  - {proj['project_name']}")

if len(capital_design_projects) > 10:
    print(f"  ... and {len(capital_design_projects) - 10} more")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
