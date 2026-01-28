code = """import json, re

# Get file paths
funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:6

# Load data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Count capital design projects with funding > $50,000
count = 0
matched_projects = []

# Build funding lookup for projects > $50k
funding_lookup = {}
for item in funding_data:
    amount = float(item['Amount'])
    if amount > 50000:
        name = item['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_lookup[name] = amount
        funding_lookup[clean_name] = amount

# Process civic documents to find capital design projects
for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Track section
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
        elif 'Capital Improvement Projects (Construction)' in line:
            in_design_section = False
        
        # Process project names in design section
        if in_design_section and line and len(line) > 15:
            # Skip disaster projects
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or 'fire' in line:
                continue
            
            # Skip meta lines
            if line.startswith('(') or 'RECOMMENDED' in line.upper() or 'UPDATES:' in line.upper() or 'SCHEDULE:' in line.upper():
                continue
            
            # Check if project has funding > $50k
            clean_line = re.sub(r'\s*\([^)]*\)\s*$', '', line).strip()
            if line in funding_lookup or clean_line in funding_lookup:
                count += 1
                amount = funding_lookup.get(line) or funding_lookup.get(clean_line, 0)
                matched_projects.append({'project': line, 'amount': int(amount)})

result = {'count': count, 'projects': matched_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
