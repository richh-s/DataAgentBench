code = """import json

# Load funding data
f1 = open(var_functions.query_db:0)
funding = json.load(f1)
f1.close()

# Load civic documents
f2 = open(var_functions.query_db:2)
docs = json.load(f2)
f2.close()

# Filter funding > $50k
high_funding_names = []
for r in funding:
    if int(r['Amount']) > 50000:
        high_funding_names.append(r['Project_Name'])

# Extract capital design project names
design_projects = []
for doc in docs:
    text = doc.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    # Get section up to end
    design_section = text[start:]
    
    # Find where section ends
    next_section = design_section.find('Capital Improvement Projects (Construction)')
    if next_section != -1:
        design_section = design_section[:next_section]
    
    # Extract lines that could be project names
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        # Basic filtering
        if len(line) > 20 and not line.startswith('(') and 'Updates:' not in line and 'Schedule:' not in line:
            # Remove bullets if present
            if line and line[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and len(line) > 2 and line[1] == '.':
                line = line[2:].strip()
            if len(line) > 15:
                design_projects.append(line)

# Simple matching - count overlaps where project name or funding name contains the other
matched_count = 0
for proj in design_projects:
    for fund in high_funding_names:
        if proj in fund or fund in proj or proj.lower() == fund.lower():
            matched_count += 1
            break

print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
