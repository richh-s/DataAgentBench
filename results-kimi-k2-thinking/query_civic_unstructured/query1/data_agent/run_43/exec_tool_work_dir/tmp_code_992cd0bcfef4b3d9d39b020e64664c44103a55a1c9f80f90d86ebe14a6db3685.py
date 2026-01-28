code = """import json

# Load funding data with Amount > 50000
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
civic_docs_file = var_functions.query_db:6
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Extract design status capital projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and obvious non-project lines
        if not line or len(line) < 10:
            continue
        
        # Skip lines that are clearly not project names
        skip_terms = ['Page', 'Item', 'Updates', 'Schedule', 'Staff', 'City', 'Consultant', 'Project is', 'To:', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date', 'Subject', 'Discussion', 'RECOMMENDED ACTION', 'Funding', 'Agreement']
        if any(term in line for term in skip_terms):
            continue
        
        if line.startswith('202') or line.startswith('Page'):
            continue
        
        # Look for design status in following lines
        status = None
        for j in range(i, min(i+5, len(lines))):
            next_line = lines[j].strip().lower()
            if 'design' in next_line:
                status = 'design'
                break
        
        if status == 'design':
            # Clean up project name
            proj_name = line.replace('• ', '').replace('○ ', '').strip()
            
            # Only add reasonable project names
            if 10 < len(proj_name) < 150:
                projects.append({
                    'Project_Name': proj_name,
                    'status': 'design',
                    'type': 'capital'
                })

# Remove duplicates
unique_projects = {}
for p in projects:
    unique_projects[p['Project_Name']] = p

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Amount'])

# Match and count
matched = 0
details = []

for proj_name in unique_projects.keys():
    # Check direct matches
    if proj_name in funding_lookup and funding_lookup[proj_name] > 50000:
        matched += 1
        details.append({'Project_Name': proj_name, 'Amount': funding_lookup[proj_name]})
    else:
        # Check partial matches
        for funded_name, amount in funding_lookup.items():
            if amount > 50000:
                # Simple substring matching
                if proj_name.lower() in funded_name.lower() or funded_name.lower() in proj_name.lower():
                    # Ensure they're reasonably similar
                    if abs(len(proj_name) - len(funded_name)) < 50:
                        matched += 1
                        details.append({'Project_Name': proj_name, 'Amount': amount, 'Funded_As': funded_name})
                        break

result = {
    'count': matched,
    'projects': sorted(details, key=lambda x: x['Amount'], reverse=True)[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
