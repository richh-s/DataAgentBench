code = """import re
import json

# Load the data from the stored results
funding_data = locals()['var_functions.query_db:20']
civic_docs = locals()['var_functions.query_db:6']

print('Loaded funding records:', len(funding_data))
print('Loaded civic documents:', len(civic_docs))

# Create a dict of project names to funding amounts for easy lookup
funding_lookup = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_lookup[project_name] = amount

# Also create partial name matches (without suffixes like (FEMA Project))
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check for suffixes and create base name
    for suffix in ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)', '(FEMA/CalOES Project)']:
        if suffix in project_name:
            base_name = project_name.replace(f' {suffix}', '').strip()
            # Add base name as alternate key
            if base_name not in funding_lookup or amount > funding_lookup[base_name]:
                funding_lookup[base_name] = amount
            break

print('Funding lookup created with', len(funding_lookup), 'entries')

# Now extract project information from civic documents
capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for sections about Capital Improvement Projects
    # Pattern to find projects with their status
    
    # Pattern for projects in Design phase
    design_section = re.findall(r'Capital Improvement Projects \(Design\)(.*?)Capital Improvement Projects \(Construction\)', text, re.DOTALL)
    if not design_section:
        design_section = re.findall(r'Capital Improvement Projects \(Design\)(.*?)Disaster Recovery Projects', text, re.DOTALL)
    if not design_section:
        design_section = re.findall(r'Capital Improvement Projects \(Design\)(.*)', text, re.DOTALL)
    
    if design_section:
        design_text = design_section[0]
        # Extract project names and details
        # Look for lines that seem to be project names
        lines = design_text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines, bullet points, and status indicators
            if (line and not line.startswith('(') and not line.startswith('•') and 
                not line.startswith('◦') and 'Updates:' not in line and 
                'Project Schedule:' not in line and 'Complete Design:' not in line and
                'Advertise:' not in line and 'Begin Construction:' not in line and
                'Estimated Schedule:' not in line and 'Project Description:' not in line):
                
                # Check if this looks like a project name
                if len(line) > 10 and not line.isupper() and '2022' not in line and '2023' not in line:
                    # Clean up the project name
                    project_name = re.sub(r'\s+', ' ', line).strip()
                    if project_name and not project_name.startswith('Page') and not project_name.startswith('Agenda'):
                        # Check if this project has funding > 50000
                        if project_name in funding_lookup:
                            amount = funding_lookup[project_name]
                            if amount > 50000:
                                project_info = {
                                    'Project_Name': project_name,
                                    'type': 'capital',
                                    'status': 'design',
                                    'funding': amount,
                                    'source': filename
                                }
                                capital_projects.append(project_info)
                                print(f'Found project: {project_name}, Funding: {amount}')

# Check for other formats
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Alternative pattern: find project names followed by parentheses with status
    # Look for patterns like "Project Name (Design)"
    
    # Find all capital projects mentioned
    capital_matches = re.findall(r'([A-Z][A-Za-z0-9 &\-.,]+(?:\([^)]*\))?\s*(?=\(Design\))', text)
    
    for match in capital_matches:
        project_name = match.strip()
        if 'FEMA' not in project_name and 'CalOES' not in project_name and len(project_name) > 10:
            # Clean up
            project_name_clean = project_name.split('(')[0].strip()
            if project_name_clean in funding_lookup:
                amount = funding_lookup[project_name_clean]
                if amount > 50000:
                    project_info = {
                        'Project_Name': project_name_clean,
                        'type': 'capital',
                        'status': 'design',
                        'funding': amount,
                        'source': 'pattern_match'
                    }
                    if project_info not in capital_projects:
                        capital_projects.append(project_info)
                        print(f'Found project via pattern: {project_name_clean}, Funding: {amount}')

print(f'\nTotal capital projects with design status and funding > $50,000: {len(capital_projects)}')

# Show results
for proj in capital_projects:
    print(f"- {proj['Project_Name']}: ${proj['funding']:,}")

print('\n__RESULT__:')
print(str(len(capital_projects)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
