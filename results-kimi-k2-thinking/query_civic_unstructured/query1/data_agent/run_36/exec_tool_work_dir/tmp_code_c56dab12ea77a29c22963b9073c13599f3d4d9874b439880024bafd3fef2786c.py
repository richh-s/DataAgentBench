code = """import json

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
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

print('Funding records over $50,000:', len(high_funding))
print('Civic documents:', len(civic_docs))

# Simple approach: extract project names mentioned in Design section
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find the design section
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    # Get text after start
    section = text[start:start+3000]
    
    # Find end of section
    end = section.find('capital improvement projects (construction)')
    if end == -1:
        end = section.find('disaster recovery projects')
    if end == -1:
        end = len(section)
    
    design_section = section[:end]
    
    # Look for potential project names (lines that don't contain common headers)
    lines = design_section.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip if contains these
        skip_terms = ['capital improvement', 'design', 'updates:', 'project schedule', 'subject', 'recommended action', 'date prepared', 'meeting date']
        should_skip = False
        for term in skip_terms:
            if term in line:
                should_skip = True
                break
        
        if should_skip:
            continue
        
        # Remove leading symbols and numbers
        clean_line = line.lstrip('0123456789.-•●■□ ')
        if clean_line and len(clean_line) > 5:
            design_projects.append(clean_line.title())

print('Potential design projects found:', len(design_projects))

# Match with funding data
matches = []
for design in design_projects[:30]:  # Check top candidates
    design_lower = design.lower()
    for fund in high_funding:
        fund_name = fund['Project_Name'].lower()
        # Simple matching
        if design_lower in fund_name or fund_name in design_lower:
            matches.append({
                'design': design,
                'funding': fund['Project_Name'],
                'amount': int(fund['Amount'])
            })
            break

result = {
    'capital_design_projects_with_funding_over_50k': len(matches),
    'matches': matches[:10]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
