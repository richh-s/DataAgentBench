code = """import json
import re

# Load data from storage
funding_path = locals()['var_functions.query_db:22']
civic_path = locals()['var_functions.query_db:20']

# Load funding data
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Find all capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for Capital Improvement Projects (Design) section
    match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|$)', text, re.DOTALL | re.IGNORECASE)
    
    if match:
        section = match.group(1)
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            if len(line) < 5:
                continue
            
            # Skip non-project lines
            if line[0] in '(-•▪' or line.isupper() or 'cid:' in line:
                continue
            if 'PROJECTS' in line.upper():
                continue
            
            lower = line.lower()
            skip_terms = ['updates', 'project schedule', 'complete design', 'advertise', 'begin construction', 'project description', 'estimated schedule', 'complete construction', 'project updates', 'page', 'public works', 'commission', 'agenda', 'report', 'meeting', 'prepared by', 'approved by', 'subject']
            if any(term in lower for term in skip_terms):
                continue
            
            if lower in ['design', 'construction', 'not started']:
                continue
                
            # Clean line
            project_name = line
            for prefix in ['·', '•', '-', '▪']:
                if project_name.startswith(prefix):
                    project_name = project_name[1:].strip()
            
            design_projects.append(project_name)

# Remove duplicates
design_projects = list(set(design_projects))

print('Design capital projects found:', len(design_projects))

# Check funding amounts
funded_projects = []
for funding in funding_records:
    project_name = funding['Project_Name']
    amount = int(funding['Amount'])
    
    if amount > 50000 and project_name in design_projects:
        funded_projects.append({
            'Project_Name': project_name,
            'Amount': amount
        })

print('\nProjects meeting criteria:', len(funded_projects))
for proj in funded_projects:
    print('  -', proj['Project_Name'], ': $' + str(proj['Amount']))

# Return result
result = json.dumps({'count': len(funded_projects), 'projects': funded_projects})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:18': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
