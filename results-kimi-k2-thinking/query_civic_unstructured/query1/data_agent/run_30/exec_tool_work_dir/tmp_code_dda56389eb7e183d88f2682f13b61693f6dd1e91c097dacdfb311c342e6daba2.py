code = """import json
import re

# Load funding data
with open(var_functions.query_db:0, 'r') as f:
    funding_records = json.load(f)

print(f"Number of funding records with Amount > 50000: {len(funding_records)}")

# Load civic docs data
with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")

# Extract project information from civic docs
# Look for capital projects with design status
projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    capital_section = ''
    
    # Find capital projects (design) section
    if 'capital improvement projects (design)' in text:
        start = text.find('capital improvement projects (design)')
        # Find end of section (look for next major section)
        end_positions = []
        for marker in ['capital improvement projects (construction)', 'disaster recovery projects', 'page 1 of', 'page 2 of']:
            pos = text.find(marker, start)
            if pos > start:
                end_positions.append(pos)
        
        if end_positions:
            end = min(end_positions)
        else:
            end = start + 5000  # Take reasonable chunk
            
        capital_section = text[start:end]
    
    if capital_section:
        # Extract what look like project names
        # Look for lines that are likely project names
        section_text = doc.get('text', '')[text.find('capital improvement projects (design)'):text.find('capital improvement projects (design)')+len(capital_section)]
        lines = section_text.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Skip common non-project lines
            skip_patterns = ['project ', 'updates:', 'schedule:', 'recommended action', 'complete design', 'advertise:', 'begin construction', 'staff is', 'city council', 'city submitted', 'consultant', 'estimated schedule', 'discussion:', 'to:', 'from:', 'subject:', 'date:', 'page ']
            if any(pattern in line.lower() for pattern in skip_patterns):
                continue
            
            # Skip very short lines
            if len(line) < 10:
                continue
            
            # Skip bullet points
            if line.startswith('●') or line.startswith('❖') or line.startswith('•') or line.startswith('(') or line.startswith(')'):
                continue
            
            # If line looks like a project name (contains project-related keywords or is title-like)
            if any(keyword in line.lower() for keyword in ['road', 'avenue', 'drive', 'street', 'park', 'drain', 'storm', 'bridge', 'walkway', 'trail', 'sewer', 'water', 'traffic', 'signal', 'sign']):
                # Verify this is in design status
                if 'design' in doc.get('text', '').lower():
                    projects.append({
                        'Project_Name': line.strip(),
                        'type': 'capital',
                        'status': 'design',
                        'source_doc': doc.get('filename', '')
                    })

# Remove duplicates
unique_projects = []
seen_names = set()

for proj in projects:
    name_key = proj['Project_Name'].lower().strip()
    if name_key not in seen_names:
        seen_names.add(name_key)
        unique_projects.append(proj)

projects = unique_projects

print(f"Extracted {len(projects)} potential capital design projects")
for i, p in enumerate(projects[:15]):
    print(f"  {i+1}. {p['Project_Name']}")

# Create funding lookup
capital_design_projects = []

for proj in projects:
    proj_name = proj['Project_Name']
    proj_name_lower = proj_name.lower()
    
    # Look for matching funding
    for fund in funding_records:
        fund_name = fund['Project_Name']
        fund_name_lower = fund_name.lower()
        fund_amount = int(fund['Amount'])
        
        # Check if funding > 50000
        if fund_amount <= 50000:
            continue
            
        # Direct match or partial match
        if (proj_name_lower == fund_name_lower or 
            proj_name_lower in fund_name_lower or 
            fund_name_lower in proj_name_lower):
            
            capital_design_projects.append({
                'Project_Name': proj_name,
                'Funding_Project_Name': fund_name,
                'Amount': fund_amount,
                'Funding_Source': fund['Funding_Source']
            })
            break

print(f"\nFound {len(capital_design_projects)} capital design projects with funding > $50,000")

# Format result
result = {
    'total_count': len(capital_design_projects),
    'projects': capital_design_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
