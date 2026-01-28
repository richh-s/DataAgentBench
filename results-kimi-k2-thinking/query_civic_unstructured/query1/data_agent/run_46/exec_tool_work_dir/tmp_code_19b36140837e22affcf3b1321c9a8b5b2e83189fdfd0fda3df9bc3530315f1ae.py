code = """import json, re, os, sys

# Load data from file paths stored in variables
funding_path = str(locals()['var_functions.query_db:6'])
civic_path = str(locals()['var_functions.query_db:8'])

# Read funding data
with open(funding_path, 'rb') as f:
    funding_bytes = f.read()
    funding_data = json.loads(funding_bytes.decode('utf-8', errors='ignore'))

# Read civic documents
with open(civic_path, 'rb') as f:
    civic_bytes = f.read()
    civic_docs = json.loads(civic_bytes.decode('utf-8', errors='ignore'))

# Create set of funding project names with amount > $50000
high_value_funding = set()
for record in funding_data:
    amount = int(record.get('Amount', 0))
    if amount > 50000:
        high_value_funding.add(record['Project_Name'].lower())

# Extract capital projects with design status from civic documents
capital_design_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_markers = ['Capital Improvement Projects (Design)', 'Capital Improvement Projects (Design Phase)']
    design_start = -1
    for marker in design_markers:
        design_start = text.find(marker)
        if design_start != -1:
            break
    
    if design_start == -1:
        continue
    
    # Find end of design section
    section_end_markers = ['Capital Improvement Projects (Construction)', 'Disaster Recovery Projects', 'Capital Improvement Projects (Not Started)']
    design_end = len(text)
    for marker in section_end_markers:
        pos = text.find(marker, design_start + 50)
        if pos != -1 and pos < design_end:
            design_end = pos
    
    design_section = text[design_start:design_end]
    
    # Extract individual project names
    for line in design_section.split('\n'):
        line = line.strip()
        
        # Filter lines
        if len(line) < 10 or line.startswith('(') or line.startswith('cid:'):
            continue
        if 'Capital Improvement' in line or 'RECOMMENDED ACTION' in line:
            continue
        
        # Skip disaster projects
        if any(x in line for x in ['FEMA', 'CalOES', 'CalJPIA']):
            continue
        
        # Check if it contains infrastructure keywords
        infrastructure_keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs','street','water','traffic']
        if any(kw.lower() in line.lower() for kw in infrastructure_keywords):
            capital_design_names.add(line.lower())

# Count matches with high-value funding
matched_project_count = 0

for design_project in capital_design_names:
    # Check for matches in funding
    for funding_project in high_value_funding:
        if design_project in funding_project or funding_project in design_project:
            # Additional check: make sure it's not just a partial word match
            if len(design_project) > 5 and len(funding_project) > 5:
                matched_project_count += 1
                break

# Output result
print('__RESULT__:')
print(json.dumps({'count': matched_project_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
