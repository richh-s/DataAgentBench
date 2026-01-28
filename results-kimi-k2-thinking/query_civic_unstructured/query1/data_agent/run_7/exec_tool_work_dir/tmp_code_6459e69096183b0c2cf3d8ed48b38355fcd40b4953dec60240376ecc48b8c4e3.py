code = """import json
import re

# Load data
mongo_key = 'var_functions.query_db:10'
funding_key = 'var_functions.query_db:5'

mongo_result = locals().get(mongo_key)
funding_result = locals().get(funding_key)

# Load data from file paths if they are strings
mongo_docs = []
funding_records = []

if isinstance(mongo_result, str):
    with open(mongo_result, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_result

if isinstance(funding_result, str):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

print('Loaded docs and records')

# Find all projects in MongoDB with design status
design_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for capital improvement projects in design status
    # Pattern: project name followed by design-related text
    sections = text.split('Capital Improvement Projects (Design)')
    
    if len(sections) > 1:
        design_section = sections[1].split('Capital Improvement Projects')[0]
        
        # Extract project names from this section
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Capture project names (not headers, not bullet points)
            if line and len(line) > 10 and not line.startswith('(') and not line.isupper():
                # Skip common noise
                if 'Updates:' not in line and 'Schedule:' not in line and 'Complete Design' not in line:
                    if not any(x in line for x in ['Public Works', 'Commission', 'Agenda', 'Page', 'To:', 'Subject:', 'Item']):
                        if line not in design_projects:
                            design_projects.append(line)

# Filter funding records > $50,000
high_funding = []
for record in funding_records:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            high_funding.append(record)
    except:
        continue

# Create mapping for easy lookup
funding_map = {}
for record in high_funding:
    name = record.get('Project_Name', '')
    if name:
        funding_map[name] = int(record.get('Amount', 0))

# Match design projects with funding
matched_projects = []

# Try to match by checking if project name contains key words from funding record
for design_proj in design_projects:
    # Clean up the design project name
    clean_design = design_proj.lower().replace('project', '').strip()
    
    for funded_name in funding_map:
        clean_funded = funded_name.lower().replace('project', '').strip()
        
        # Check for substantial overlap
        design_words = set(clean_design.split())
        funded_words = set(clean_funded.split())
        
        # Count matching words (excluding common words)
        common_words = {'and', 'road', 'repair', 'improvements', 'project'}
        matches = design_words.intersection(funded_words) - common_words
        
        if len(matches) >= 2:
            if funded_name not in [p['name'] for p in matched_projects]:
                matched_projects.append({
                    'name': funded_name,
                    'amount': funding_map[funded_name]
                })
                break

# Count final matches
count = len(matched_projects)

# Return result
result = json.dumps({
    'total_matches': count,
    'projects': matched_projects
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
