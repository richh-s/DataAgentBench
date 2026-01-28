code = """import json
import re

# Read funding data
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic docs data  
civic_docs_file = locals()['var_functions.query_db:8']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Parse civic docs to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects (Design) section
    if 'Capital Improvement Projects (Design)' in text:
        # Extract projects in this section
        # Pattern: project name followed by updates/schedule
        design_section = text.split('Capital Improvement Projects (Design)')[1]
        
        # Split by common patterns to identify projects
        lines = design_section.split('\n')
        current_project = None
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('(') or 'Project Schedule' in line or 'Updates' in line:
                continue
                
            # Check if this looks like a project name (more than just a few words, not a date/season)
            if len(line) > 10 and not any(keyword in line for keyword in ['Complete Design', 'Advertise', 'Begin Construction', 'Page', 'Agenda Item']):
                # Could be a project name
                if ':' not in line and '•' not in line:
                    current_project = line.strip()
                    # Clean up common artifacts
                    current_project = re.sub(r'^[^a-zA-Z]*', '', current_project)
                    if current_project and len(current_project) > 5:
                        projects.append({
                            'Project_Name': current_project,
                            'type': 'capital',
                            'status': 'design'
                        })

# Filter funding > $50,000
high_funding = [f for f in funding_data if int(f['Amount']) > 50000]

print(f"Capital design projects found: {len(projects)}")
print(f"High funding projects (>50k): {len(high_funding)}")

# Create lookup for high funding projects
funding_lookup = {f['Project_Name'].lower(): int(f['Amount']) for f in high_funding}

# Match projects with funding
matched_projects = []
for proj in projects:
    proj_name = proj['Project_Name']
    proj_name_lower = proj_name.lower()
    
    # Direct match
    if proj_name_lower in funding_lookup:
        matched_projects.append({
            'Project_Name': proj_name,
            'Amount': funding_lookup[proj_name_lower],
            'type': proj['type'],
            'status': proj['status']
        })
    else:
        # Fuzzy match - check if any funded project contains this name
        for funded_name, amount in funding_lookup.items():
            if proj_name_lower in funded_name or funded_name in proj_name_lower:
                if abs(len(proj_name_lower) - len(funded_name)) < 10:  # Close in length
                    matched_projects.append({
                        'Project_Name': proj_name,
                        'Amount': amount,
                        'type': proj['type'],
                        'status': proj['status']
                    })
                    break

# Remove duplicates
unique_matched = []
seen_names = set()
for proj in matched_projects:
    if proj['Project_Name'] not in seen_names:
        unique_matched.append(proj)
        seen_names.add(proj['Project_Name'])

print(f"Matched capital design projects with >50k funding: {len(unique_matched)}")

# Display matches for verification
for proj in unique_matched[:10]:
    print(f"  {proj['Project_Name']}: ${proj['Amount']:,}")

result = len(unique_matched)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
