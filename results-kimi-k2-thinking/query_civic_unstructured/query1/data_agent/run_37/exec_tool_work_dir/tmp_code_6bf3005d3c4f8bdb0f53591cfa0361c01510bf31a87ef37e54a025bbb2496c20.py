code = """import json
import re
import os

# Try to load the data from known file paths
funding_path = 'file_storage/execute_python_2/query_db_2.json'
civic_path = 'file_storage/execute_python_5/query_db_5.json'

if os.path.exists(funding_path):
    with open(funding_path) as f:
        funding_data = json.load(f)
    print('Loaded funding data: %d records' % len(funding_data))
else:
    print('Funding path not found')
    funding_data = []

if os.path.exists(civic_path):
    with open(civic_path) as f:
        civic_docs = json.load(f)
    print('Loaded civic docs: %d documents' % len(civic_docs))
else:
    print('Civic path not found')
    civic_docs = []

# Step 1: Create funding lookup for projects > $50,000
funding_lookup = {}
for rec in funding_data:
    try:
        amount = int(rec.get('Amount', 0))
        if amount > 50000:
            project_name = rec.get('Project_Name', '')
            funding_lookup[project_name] = amount
    except:
        continue

print('Projects with >$50k funding:', len(funding_lookup))

# Step 2: Extract project info from civic documents
capital_design_count = 0
found_projects = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Skip headers/footers
        if any(skip in line.lower() for skip in ['project schedule', 'updates', 'discussion', 'agenda:', 'to:', 'prepared by:', 'date:', 'subject:']):
            continue
        
        # Check if this line could be a project name
        if len(line) < 80 and not line.startswith('(') and not any(x in line.lower() for x in ['complete design:', 'advertise:', 'begin construction:']):
            # Look at context (surrounding lines) for status and type
            context_start = max(0, i-3)
            context_end = min(len(lines), i+8)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'capital' in context and 'design' in context:
                # Check if this is a funded project
                if line in funding_lookup:
                    found_projects.append({
                        'name': line,
                        'amount': funding_lookup[line]
                    })
                    capital_design_count += 1

# Remove duplicates
unique_projects = []
seen = set()
for p in found_projects:
    if p['name'] not in seen:
        seen.add(p['name'])
        unique_projects.append(p)

print('Capital design projects with >$50k funding:', len(unique_projects))
print('__RESULT__:')
result = {'total_count': len(unique_projects), 'projects': unique_projects}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
