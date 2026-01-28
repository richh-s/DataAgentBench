code = """import json

# Load data from files
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Records loaded - Funding:', len(funding_records), 'Civic docs:', len(civic_docs))

# Find design projects in civic docs
design_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    t_lower = text.lower()
    
    # Look for capital improvement projects in design phase
    if 'capital improvement' in t_lower and 'design' in t_lower:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) >= 10:
                # Skip administrative lines
                skip = False
                for term in ['updates:', 'schedule:', 'staff ', 'city council', 'consultant', 'discussion:', 'page ', 'complete design', 'advertise:', 'construction']:
                    if term in line.lower():
                        skip = True
                        break
                if skip:
                    continue
                
                # Check if line contains infrastructure keywords
                infra_terms = ['road', 'avenue', 'drive', 'park', 'drain', 'bridge', 'walkway', 'sewer', 'traffic', 'signal', 'median', 'crosswalk']
                for term in infra_terms:
                    if term in line.lower():
                        design_project_names.append(line)
                        break

# Remove duplicates
design_project_names = list(set(design_project_names))
print('Potential design projects:', len(design_project_names))

# Match with funding
count = 0
for project in design_project_names:
    proj_lower = project.lower()
    for fund in funding_records:
        if int(fund['Amount']) > 50000:
            fund_lower = fund['Project_Name'].lower()
            if proj_lower == fund_lower or proj_lower in fund_lower or fund_lower in proj_lower:
                count += 1
                break

print('Final count:', count)
print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
