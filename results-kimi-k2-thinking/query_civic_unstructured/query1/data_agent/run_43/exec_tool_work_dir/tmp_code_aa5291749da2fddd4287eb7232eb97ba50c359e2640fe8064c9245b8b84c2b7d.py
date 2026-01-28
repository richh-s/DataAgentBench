code = """import json

# Load the funding data
funding_data = json.load(open(var_functions.query_db:5))

# Load the civic documents
civic_docs = json.load(open(var_functions.query_db:6))

# Build funding lookup: project name -> amount
funding_amounts = {}
for item in funding_data:
    project_name = item.get('Project_Name')
    amount = int(item.get('Amount'))
    funding_amounts[project_name] = amount

# Extract capital projects with design status from civic documents
design_capital_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find sections about Capital Improvement Projects
    if 'Capital Improvement Projects' in text:
        # Split into lines and process
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and obvious non-project lines
            if not line or len(line) < 5:
                continue
            # Skip page numbers, headers, etc.
            if line.startswith('Page') or line.startswith('Item'):
                continue
            if 'Schedule:' in line or 'Updates:' in line or 'Project Description:' in line:
                continue
            
            # Look for design status in the surrounding text
            pos = text.find(line)
            if pos > 0:
                # Check next 300 characters for design status
                context = text[pos:pos+300]
                if 'Design' in context or 'design' in context:
                    # Clean up project name
                    clean_name = line.replace('• ', '').replace('○ ', '').strip()
                    # Add if it looks like a real project name
                    if 10 < len(clean_name) < 150 and not clean_name.startswith('202'):
                        design_capital_projects.add(clean_name)

# Match design projects with funding > 50000
count = 0
matched_projects = []

for design_proj in design_capital_projects:
    # Try to match with funded projects
    for funded_name, amount in funding_amounts.items():
        if amount > 50000:
            # Check for name similarity (substring match)
            d_lower = design_proj.lower()
            f_lower = funded_name.lower()
            
            # One name contains the other
            if d_lower in f_lower or f_lower in d_lower:
                # Additional check: length difference not too large
                if abs(len(design_proj) - len(funded_name)) < 40:
                    count += 1
                    matched_projects.append({
                        'project': design_proj,
                        'funding': amount,
                        'funded_as': funded_name
                    })
                    break

# Return the count
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
