code = """import json, re

# Get file paths from storage
funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:6

# Read funding data
with open(funding_path) as f:
    funding_records = json.load(f)

# Read civic documents
with open(civic_path) as f:
    civic_documents = json.load(f)

# Build funding map (amount > 50000)
funding_map = {}
for rec in funding_records:
    amount = float(rec['Amount'])
    if amount > 50000:
        name = rec['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean] = amount

# Extract capital design projects from documents
capital_design = set()

for doc in civic_documents:
    text = doc.get('text', '')
    design_active = False
    
    for line in text.split('\n'):
        line = line.strip()
        
        # Track design section
        if 'Capital Improvement Projects (Design)' in line:
            design_active = True
        elif 'Capital Improvement Projects (Construction)' in line:
            design_active = False
        
        # Extract project names from design section
        if design_active and line and len(line) > 15:
            # Skip disaster projects
            if any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                continue
            
            # Skip meta content
            if any(word in line.upper() for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA']):
                continue
            
            # Skip section headers and bullet points
            if any(phrase in line for phrase in ['Updates:', 'Schedule:', 'Capital Improvement']):
                continue
            
            if line.startswith('(') or line.startswith('\u2022'):
                continue
            
            # Add project
            capital_design.add(line)

# Count matches
count = 0
matched = []

for proj in capital_design:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    
    if proj in funding_map or proj_clean in funding_map:
        count += 1
        amt = funding_map.get(proj) or funding_map.get(proj_clean, 0)
        matched.append({'name': proj, 'amount': int(amt)})

# Return result
result = {'count': count, 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
