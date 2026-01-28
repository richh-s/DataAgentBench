code = """import json
import re

# Load data
funding_file = var_functions.query_db:4
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:2
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Filter funding > $50,000
high_funding = []
for record in funding_data:
    if record.get('Amount'):
        try:
            amount = int(record['Amount'])
            if amount > 50000:
                high_funding.append(record)
        except:
            pass

print(f"Total funding records: {len(funding_data)}")
print(f"Funding > $50,000: {len(high_funding)}")
print(f"Civic documents: {len(civic_docs)}")

# Extract design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find where design projects section starts
    design_start = text.lower().find('capital improvement projects (design)')
    if design_start < 0:
        design_start = text.lower().find('capital improvement projects(design)')
    
    if design_start >= 0:
        design_section = text[design_start:design_start+2000]  # Look at reasonable section length
        
        # Find where it ends (next major section)
        construction_pos = design_section.lower().find('capital improvement projects (construction)')
        disaster_pos = design_section.lower().find('disaster recovery projects')
        
        end_pos = len(design_section)
        if construction_pos > 0:
            end_pos = min(end_pos, construction_pos)
        if disaster_pos > 0:
            end_pos = min(end_pos, disaster_pos)
            
        design_section = design_section[:end_pos]
        
        # Extract project names (look for lines that are project names)
        lines = design_section.split('\n')
        
        for line_num in range(len(lines)):
            line = lines[line_num].strip()
            
            # Clean line
            if not line or len(line) < 5:
                continue
                
            # Skip common headers and markers
            skip_patterns = ['capital improvement', 'design', 'updates:', 'project schedule', 'subject:', 'recommended action', '•', '●', '■', '□']
            should_skip = False
            for pattern in skip_patterns:
                if pattern.lower() in line.lower():
                    should_skip = True
                    break
            if should_skip:
                continue
            
            # Check if this looks like a project name (next line has project details)
            if line_num + 1 < len(lines):
                next_line = lines[line_num + 1].strip()
                if 'Updates:' in next_line or 'Project Schedule' in next_line or next_line.startswith('('):
                    # Clean the project name
                    proj_name = re.sub('^[^\w]*', '', line)  # Remove leading non-word chars
                    proj_name = re.sub('\s+', ' ', proj_name)  # Normalize spaces
                    
                    if len(proj_name) > 5:
                        design_projects.append({
                            'name': proj_name,
                            'status': 'design',
                            'type': 'capital'
                        })

print(f"\nDesign projects found: {len(design_projects)}")
for project in design_projects[:15]:
    print(f"  - {project['name']}")

# Match with funding data
matches = []
for design_proj in design_projects:
    design_name = design_proj['name'].lower()
    
    for fund in high_funding:
        fund_name = fund['Project_Name'].lower()
        
        # Check for various forms of matching
        if fund_name == design_name or design_name in fund_name or fund_name in design_name:
            matches.append({
                'design_project': design_proj['name'],
                'funding_project': fund['Project_Name'],
                'amount': int(fund['Amount'])
            })
            break
        else:
            # Check word overlap for longer names
            design_words = set([w for w in design_name.split() if len(w) > 3])
            fund_words = set([w for w in fund_name.split() if len(w) > 3])
            
            # If significant word overlap
            if design_words & fund_words and len(design_words & fund_words) >= 2:
                matches.append({
                    'design_project': design_proj['name'],
                    'funding_project': fund['Project_Name'],
                    'amount': int(fund['Amount'])
                })
                break

print(f"\nMatching projects with funding > $50,000: {len(matches)}")
for match in matches[:10]:
    print(f"  - {match['design_project']}: ${match['amount']:,}")

result = {'count': len(matches), 'projects': matches}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
