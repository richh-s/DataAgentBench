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
high_funding = []
for f in funding_data:
    if f.get('Amount'):
        try:
            amount = int(f['Amount'])
            if amount > 50000:
                high_funding.append(f)
        except:
            pass

print(f"Total funding records: {len(funding_data)}")
print(f"Funding records > $50,000: {len(high_funding)}")
print(f"Number of civic documents: {len(civic_docs)}")

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find Capital Improvement Projects (Design) section
    # Split by common section headers
    sections = re.split(r'Capital Improvement Projects \(Design\)', text, flags=re.IGNORECASE)
    
    if len(sections) > 1:
        design_section = sections[1]
        
        # Find where the design section ends (next major section)
        end_markers = [
            'Capital Improvement Projects (Construction)',
            'DISASTER RECOVERY PROJECTS', 
            'Disaster Recovery Projects',
            'Capital Improvement Projects (Not Started)'
        ]
        
        for marker in end_markers:
            if marker in design_section:
                design_section = design_section.split(marker)[0]
                break
        
        # Extract project names
        lines = design_section.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty lines and bullets
            if not line or line in ['•', '●', '■', '□', '\x95']:
                continue
                
            # Check if line looks like a project name (not a detail line)
            if (len(line) > 5 and 
                not line.startswith('(') and
                not line.startswith('•') and
                'Updates:' not in line and
                'Project Schedule' not in line and
                'Subject:' not in line and
                'RECOMMENDED ACTION' not in line):
                
                # Check if next line has project indicators
                has_project_details = False
                if i + 1 < len(lines):
                    next_line = lines[i+1].strip()
                    if ('Updates:' in next_line or 
                        'Project Schedule' in next_line or
                        next_line.startswith('(')):
                        has_project_details = True
                
                if has_project_details:
                    # Clean the project name
                    proj_name = re.sub(r'^[^\w]*', '', line)  # Remove leading non-word chars
                    proj_name = re.sub(r'\s+', ' ', proj_name)  # Normalize spaces
                    
                    if len(proj_name) > 5:
                        projects.append({
                            'project_name': proj_name,
                            'status': 'design',
                            'type': 'capital',
                            'source': doc.get('filename', '')
                        })

print(f"\nFound {len(projects)} capital projects with design status:")
for p in projects[:20]:
    print(f"  - {p['project_name']}")

# Match with funding data
matches = []
for proj in projects:
    proj_name = proj['project_name'].lower()
    
    for fund in high_funding:
        fund_name = fund['Project_Name'].lower()
        
        # Check for name overlap (partial matching)
        if (proj_name in fund_name or fund_name in proj_name or
            any(word in fund_name for word in proj_name.split() if len(word) > 4)):
            
            matches.append({
                'project_name': proj['project_name'],
                'funding_project_name': fund['Project_Name'],
                'amount': int(fund['Amount']),
                'funding_id': fund['Funding_ID']
            })
            break

print(f"\nFound {len(matches)} matching projects with funding > $50,000")

result = {
    'count': len(matches),
    'matches': matches
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
