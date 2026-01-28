code = """import json, re

# Load funding data from file
funding_file = locals()['var_functions.query_db:6']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents from file
civic_file = locals()['var_functions.query_db:8']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create a set of funding project names with amounts > $50,000
high_value_funding = set()
for record in funding_records:
    amount = int(record.get('Amount', 0))
    if amount > 50000:
        high_value_funding.add(record['Project_Name'].lower())

# Extract capital projects with design status from civic documents
capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section header
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find end of design section (start of construction section)
    design_end = text.find('Capital Improvement Projects (Construction)', design_start)
    if design_end == -1:
        design_end = len(text)
    
    # Process just the design section
    design_section = text[design_start:design_end]
    
    # Extract project names
    for line in design_section.split('\n'):
        line = line.strip()
        
        # Skip short lines, markers, and headings
        if len(line) < 10 or line.startswith('(') or 'Capital Improvement' in line:
            continue
        
        # Skip disaster projects
        if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
            continue
        
        # Check for infrastructure keywords
        keywords = ['road', 'park', 'drain', 'bridge', 'facility', 'system', 'plan', 'structure', 'study', 'improvements', 'repairs']
        if any(kw in line.lower() for kw in keywords):
            capital_design_projects.add(line.lower())

# Count how many capital design projects match high-value funding
matched_count = 0

for project in capital_design_projects:
    # Check for matching funding
    for funding_name in high_value_funding:
        if project in funding_name or funding_name in project:
            matched_count += 1
            break

result = {'count': matched_count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:78': {'test': 'success'}}

exec(code, env_args)
