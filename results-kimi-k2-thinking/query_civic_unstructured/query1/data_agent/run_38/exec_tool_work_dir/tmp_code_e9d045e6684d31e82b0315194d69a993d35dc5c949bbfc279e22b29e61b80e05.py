code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:22']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
civic_path = locals()['var_functions.query_db:20']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project names from design section
design_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find section
    import re
    pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|$)'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if match:
        section = match.group(1)
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            if len(line) > 5 and not line[0] in '(-' and not line.isupper() and 'cid:' not in line and 'PROJECTS' not in line.upper():
                lower = line.lower()
                if not any(x in lower for x in ['updates', 'schedule', 'design', 'construction', 'description', 'page', 'public works', 'commission', 'agenda']):
                    if lower not in ['design', 'construction', 'not started']:
                        design_project_names.append(line)

# Remove duplicates
design_project_names = list(set(design_project_names))

print('Design projects:', len(design_project_names))

# Check funding
matching_projects = []
for funding in funding_records:
    amount = int(funding['Amount'])
    if amount > 50000 and funding['Project_Name'] in design_project_names:
        matching_projects.append({
            'Project_Name': funding['Project_Name'],
            'Amount': amount
        })

print('Matching count:', len(matching_projects))

result = json.dumps({'count': len(matching_projects), 'projects': matching_projects})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:18': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
