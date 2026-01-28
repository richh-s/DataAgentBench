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

design_keywords = ['design', 'designing', 'finalizing', 'complete design', 'design plans', 'design consultant']
construction_keywords = ['construction', 'under construction', 'begin construction', 'construction was completed']

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Check if this contains capital improvement projects section
    capital_section = ''
    capital_patterns = [
        r'capital improvement projects \(design\)(.*?)(?:capital improvement projects \(construction\)|$)',
        r'capital improvement projects \(design\)(.*?)(?:disaster recovery projects|$)',
        r'capital improvement projects \(design\)(.*?)(?:page \d+ of \d+|$)'
    ]
    
    for pattern in capital_patterns:
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            capital_section = match.group(1)
            break
    
    if capital_section:
        # Extract project names from this section
        # Look for project names that are formatted with line breaks or distinctive patterns
        lines = capital_section.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # Skip section headers
            if any(x in line.lower() for x in ['project description', 'project updates', 'project schedule', 'updates:', 'schedule:']):
                continue
                
            # Skip bullet points that are not project names
            if line.startswith('●') or line.startswith('❖') or line.startswith('•') or line.startswith('('):
                continue
                
            # Skip lines that look like status indicators
            if any(x in line.lower() for x in ['complete design:', 'advertise:', 'begin construction:', 'estimated schedule', 'project is']):
                continue
                
            # If line is likely a project name (not too short, not a common phrase)
            if len(line) > 10 and not any(phrase in line.lower() for phrase in ['city council', 'city submitted', 'staff is', 'staff has', 'consultant working']):
                # Check if it mentions design or is in design section
                is_design = 'design' in doc.get('text', '').lower() or any(keyword in line.lower() for keyword in design_keywords)
                is_capital = True  # Since we're in capital section
                
                if is_capital and is_design:
                    # Clean up the project name
                    proj_name = line.strip()
                    if proj_name and not proj_name.startswith('.'):
                        projects.append({
                            'Project_Name': proj_name,
                            'type': 'capital',
                            'status': 'design',
                            'source_doc': doc.get('filename', '')
                        })

# Print extracted projects
print(f"\nExtracted {len(projects)} potential capital design projects:")
for p in projects[:10]:  # Show first 10
    print(f"  - {p['Project_Name']}")

# Create a mapping of funding project names for matching
funding_map = {rec['Project_Name'].lower(): rec for rec in funding_records}

# Match and count
matched_projects = []

for proj in projects:
    proj_name_lower = proj['Project_Name'].lower()
    
    # Direct match
    if proj_name_lower in funding_map:
        if int(funding_map[proj_name_lower]['Amount']) > 50000:
            matched_projects.append({
                **proj,
                'Funding': funding_map[proj_name_lower]
            })
        continue
    
    # Fuzzy match - look for partial matches
    for fund_name, fund_info in funding_map.items():
        # Remove common suffixes for matching
        clean_proj_name = proj_name_lower.replace(' project', '')
        clean_fund_name = fund_name.replace(' project', '')
        
        # Check if one name contains the other
        if (clean_proj_name in clean_fund_name) or (clean_fund_name in clean_proj_name):
            if int(fund_info['Amount']) > 50000:
                matched_projects.append({
                    'Project_Name': proj['Project_Name'],
                    'type': proj['type'],
                    'status': proj['status'],
                    'Funding_Project_Name': fund_info['Project_Name'],
                    'Amount': int(fund_info['Amount']),
                    'Funding_Source': fund_info['Funding_Source']
                })
                break

print(f"\nMatched projects with funding > $50,000: {len(matched_projects)}")

# Format result for output
result = {
    'count': len(matched_projects),
    'projects': matched_projects
}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
