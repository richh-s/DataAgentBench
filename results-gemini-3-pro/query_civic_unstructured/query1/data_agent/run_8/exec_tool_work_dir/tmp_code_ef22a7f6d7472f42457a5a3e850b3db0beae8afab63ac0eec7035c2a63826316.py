code = """import json

# Load funding data
with open(locals()['var_function-call-7721797773547696454'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-11187982915613525112'], 'r') as f:
    civic_docs = json.load(f)

# Create a set of funded projects > 50000
funded_projects = set()
for item in funding_data:
    try:
        amount = float(item['Amount'])
        if amount > 50000:
            funded_projects.add(item['Project_Name'].strip())
    except ValueError:
        pass

# Normalized set for case-insensitive matching
funded_projects_lower = {name.lower(): name for name in funded_projects}

design_projects_found = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check headers
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
            
        if in_design_section:
            if 'Capital Improvement Projects' in line and '(Design)' not in line:
                in_design_section = False
            elif 'Disaster Recovery Projects' in line:
                in_design_section = False
        
        if in_design_section:
            # Check if line matches a funded project
            # Exact match
            if line in funded_projects:
                design_projects_found.add(line)
            # Case-insensitive match
            elif line.lower() in funded_projects_lower:
                design_projects_found.add(funded_projects_lower[line.lower()])

print('__RESULT__:')
print(json.dumps({'count': len(design_projects_found), 'matches': list(design_projects_found)}))"""

env_args = {'var_function-call-10821165667219444455': ['Funding'], 'var_function-call-10821165667219446426': ['civic_docs'], 'var_function-call-7721797773547696454': 'file_storage/function-call-7721797773547696454.json', 'var_function-call-7721797773547696997': 'file_storage/function-call-7721797773547696997.json', 'var_function-call-11187982915613525112': 'file_storage/function-call-11187982915613525112.json'}

exec(code, env_args)
