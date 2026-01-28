code = """import json
import re

# Load data from proper storage
mongo_data = locals().get('var_functions.query_db:10')
funding_data = locals().get('var_functions.query_db:5')

# Handle file paths
mongo_docs = []
funding_records = []

if isinstance(mongo_data, str) and '.json' in mongo_data:
    with open(mongo_data, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_data if mongo_data else []

if isinstance(funding_data, str) and '.json' in funding_data:
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data if funding_data else []

print('Loaded', len(mongo_docs), 'documents and', len(funding_records), 'funding records')

# Extract capital projects with design status from MongoDB
projects_in_design = []

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    construction_section_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_section_start > 0:
        # Extract the design section
        if construction_section_start > design_section_start:
            design_section = text[design_section_start:construction_section_start]
        else:
            design_section = text[design_section_start:design_section_start + 5000]
        
        # Extract project names (lines that look like project names)
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines, headers, bullet points
            if not line or line.startswith('(') or line.endswith(':'):
                continue
            if line.isupper():
                continue
            # Skip common noise words
            noise = ['Updates', 'Schedule', 'Project', 'Public Works', 'Commission', 'Page', 'To:', 'From:', 'Subject:', 'Item', 'Agenda', 'Complete Design', 'Advertise', 'Begin Construction']
            if any(n in line for n in noise):
                continue
            # Add if it looks like a project name and not already added
            if len(line) > 10 and line not in projects_in_design:
                projects_in_design.append(line)

# Get funding records with Amount > 50000
high_funding_projects = []
for record in funding_records:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            project_name = record.get('Project_Name', '')
            if project_name:
                high_funding_projects.append({
                    'name': project_name,
                    'amount': amount
                })
    except:
        continue

print('Found', len(projects_in_design), 'design projects in documents')
print('Found', len(high_funding_projects), 'funding records > $50k')

# Match design projects with funding records
matched_projects = []

# For each high funding project, check if it appears to be in design status
for funded_proj in high_funding_projects:
    funded_name = funded_proj['name'].lower()
    
    # Check against all design projects we found
    for design_proj in projects_in_design:
        design_name = design_proj.lower()
        
        # Calculate similarity - check if they share key words
        # Remove common words and compare
        common_words = ['project', 'improvements', 'repair', 'repairs', 'road', 'and', 'the', 'improvement']
        
        funded_words = [w for w in funded_name.split() if w not in common_words]
        design_words = [w for w in design_name.split() if w not in common_words]
        
        # Check for matches (at least 2 words in common)
        matches = set(funded_words).intersection(set(design_words))
        
        if len(matches) >= 2:
            matched_projects.append(funded_proj)
            break
        # Also check substring match for shorter names
        elif len(funded_words) <= 3 and any(fw in design_name for fw in funded_words):
            if 'project' not in funded_name or 'project' not in design_name or funded_name in design_name:
                matched_projects.append(funded_proj)
                break

# Remove duplicates
unique_matched = []
seen_names = set()
for proj in matched_projects:
    if proj['name'] not in seen_names:
        unique_matched.append(proj)
        seen_names.add(proj['name'])

# Count results
count = len(unique_matched)

# Create output
result = {
    'count': count,
    'projects': unique_matched[:10]  # First 10 for display
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
