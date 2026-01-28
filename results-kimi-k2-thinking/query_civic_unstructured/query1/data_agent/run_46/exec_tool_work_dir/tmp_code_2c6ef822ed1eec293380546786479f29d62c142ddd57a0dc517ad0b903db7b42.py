code = """import json, re

# Access the variables using dictionary-style lookup to avoid syntax errors
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:8']

# Load the data from files
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Filter funding records for amounts greater than $50,000
high_funding_names = set()
for record in funding_data:
    amount = int(record.get('Amount', 0))
    if amount > 50000:
        high_funding_names.add(record['Project_Name'].lower())

# Extract capital projects with design status from civic documents
design_project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    if design_section_start == -1:
        continue
    
    # Find where the design section ends
    next_section_start = text.find('Capital Improvement Projects (Construction)', design_section_start)
    if next_section_start == -1:
        next_section_start = len(text)
    
    # Extract the design section
    design_section_text = text[design_section_start:next_section_start]
    
    # Split into lines and process
    for line in design_section_text.split('\n'):
        line = line.strip()
        
        # Skip empty lines and headings
        if len(line) < 10 or line.startswith('('):
            continue
        if 'Capital Improvement' in line:
            continue
        
        # Skip disaster project indicators
        if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
            continue
        
        # Check if this is likely a capital project name (contains infrastructure keywords)
        keywords = ['road', 'park', 'drain', 'bridge', 'facility', 'system', 'plan', 'structure', 'study', 'improvements', 'repairs', 'street', 'water', 'traffic', 'building']
        if any(kw in line.lower() for kw in keywords):
            design_project_names.add(line.lower())

# Count the capital design projects that have funding > $50,000
matched_count = 0

for project_name in design_project_names:
    # Check for matching funding
    for funding_name in high_funding_names:
        # Direct match or partial match
        if project_name in funding_name or funding_name in project_name:
            matched_count += 1
            break

# Return the result
print('__RESULT__:')
print(json.dumps({'count': matched_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
