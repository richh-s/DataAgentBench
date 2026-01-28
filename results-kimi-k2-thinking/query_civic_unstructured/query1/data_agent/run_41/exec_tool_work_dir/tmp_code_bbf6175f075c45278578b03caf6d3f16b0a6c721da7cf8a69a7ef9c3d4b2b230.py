code = """import json
import re

# Load data
funding_result = locals()['var_functions.query_db:24']
civic_result = locals()['var_functions.query_db:6']

# Create funding lookup dictionary
funding_lookup = {}
for item in funding_result:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name] = amount

# Also add base names without suffixes
for item in funding_result:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    
    # Find and remove common suffixes
    for suffix in [' (FEMA Project)', ' (CalJPIA Project)', ' (CalOES Project)', ' (FEMA/CalOES Project)', ' - Design (FEMA Project)']:
        if suffix in project_name:
            base_name = project_name.replace(suffix, '')
            if base_name not in funding_lookup:
                funding_lookup[base_name] = amount
            break

print('Funding lookup size:', len(funding_lookup))

# Process civic documents to find capital projects with design status
design_projects = []

for doc in civic_result:
    text = doc.get('text', '')
    
    # Extract projects from "Capital Improvement Projects (Design)" section
    # Pattern: look for this header and extract project names until next major section
    design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|CAPITAL IMPROVEMENT PROJECTS \(CONSTRUCTION\)|$)', text, re.DOTALL)
    
    if design_section:
        section_text = design_section.group(1)
        
        # Look for project names - they are typically on their own lines, title case, not bullet points
        lines = section_text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and obvious non-project lines
            if (not line or line.startswith('(') or line.startswith('•') or 
                line.startswith('◦') or line.startswith('-') or
                'Updates:' in line or 'Project Schedule:' in line or
                'Estimated Schedule:' in line or 'Complete Design:' in line or
                'Advertise:' in line or 'Begin Construction:' in line or
                'Page' in line or 'Agenda Item' in line):
                continue
                
            # Check if line looks like a project name (reasonable length, mixed case, contains words)
            if 10 < len(line) < 150 and any(c.isupper() for c in line) and any(c.islower() for c in line):
                # Clean up the name
                project_name = re.sub(r'\s+', ' ', line).strip()
                
                # Check if this project has funding > 50000
                if project_name in funding_lookup:
                    amount = funding_lookup[project_name]
                    if amount > 50000:
                        design_projects.append({
                            'name': project_name,
                            'funding': amount,
                            'type': 'capital',
                            'status': 'design'
                        })
                        print(f'Found: {project_name} - ${amount:,}')
                # Try without trailing period if present
                elif project_name.endswith('.') and project_name[:-1] in funding_lookup:
                    amount = funding_lookup[project_name[:-1]]
                    if amount > 50000:
                        design_projects.append({
                            'name': project_name[:-1],
                            'funding': amount,
                            'type': 'capital',
                            'status': 'design'
                        })
                        print(f'Found: {project_name[:-1]} - ${amount:,}')

# Remove duplicates
design_projects_clean = []
seen = set()
for proj in design_projects:
    if proj['name'] not in seen:
        design_projects_clean.append(proj)
        seen.add(proj['name'])

print(f'\nTotal unique capital projects with design status and funding > $50,000: {len(design_projects_clean)}')

# Print all found projects
print('\nAll projects:')
for proj in design_projects_clean:
    print(f"  - {proj['name']}: ${proj['funding']:,}")

result = len(design_projects_clean)
print('\n__RESULT__:')
print(str(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
