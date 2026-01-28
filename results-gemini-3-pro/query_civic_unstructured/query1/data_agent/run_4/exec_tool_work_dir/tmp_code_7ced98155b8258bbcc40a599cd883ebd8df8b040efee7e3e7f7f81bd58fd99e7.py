code = """import json

# Load funding data
with open('var_function-call-1424370091685766711.json', 'r') as f:
    funding_records = json.load(f)

# Filter funding for > 50,000
high_funding_projects = {}
for r in funding_records:
    try:
        amount = float(r['Amount'])
        if amount > 50000:
            high_funding_projects[r['Project_Name'].strip()] = amount
    except ValueError:
        continue

# Load civic docs
with open('var_function-call-10286396622452696184.json', 'r') as f:
    docs = json.load(f)

capital_design_projects = set()

for doc in docs:
    text = doc.get('text', '')
    # Use splitlines to avoid escape char issues
    lines = text.splitlines()
    
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
        
        # Stop conditions
        # Use simple string checks
        if 'Capital Improvement Projects' in line and 'Design' not in line:
            in_design_section = False
        if 'Disaster Recovery Projects' in line:
            in_design_section = False
            
        if in_design_section:
            # Skip bullet points and metadata
            # Check for (cid:
            if line.startswith('(cid:'): continue
            if line.startswith('Page '): continue
            if line.startswith('Agenda Item'): continue
            
            l_lower = line.lower()
            if l_lower.startswith('prepared by'): continue
            if l_lower.startswith('approved by'): continue
            if l_lower.startswith('date prepared'): continue
            if l_lower.startswith('meeting date'): continue
            if l_lower.startswith('subject:'): continue
            if l_lower.startswith('recommended action:'): continue
            if l_lower.startswith('discussion:'): continue
                
            if 'Updates:' in line or 'Schedule:' in line: continue
            
            if line.startswith('Item') or line.startswith('To:') or line.startswith('From:'): continue
            
            project_name = line.strip()
            if len(project_name) < 5: continue
                
            capital_design_projects.add(project_name)

# Now check intersection
matching_projects = []
for p in capital_design_projects:
    if p in high_funding_projects:
        matching_projects.append(p)

print('__RESULT__:')
print(json.dumps({'matches': matching_projects, 'extracted_candidates': list(capital_design_projects)}))"""

env_args = {'var_function-call-1424370091685766711': 'file_storage/function-call-1424370091685766711.json', 'var_function-call-10286396622452696184': 'file_storage/function-call-10286396622452696184.json'}

exec(code, env_args)
