code = """import json
import re

# Load data from storage
funding_path = locals()['var_functions.query_db:22']
civic_path = locals()['var_functions.query_db:20']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find design section for capital projects
    match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|$)', text, re.DOTALL | re.IGNORECASE)
    
    if match:
        section = match.group(1)
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            if len(line) < 5:
                continue
            
            # Filter lines
            if line[0] in '(-•' or line.isupper():
                continue
            if 'cid:' in line or 'PROJECTS' in line.upper():
                continue
            
            lower_line = line.lower()
            skip_terms = ['updates', 'schedule', 'design', 'construction', 'description', 'page', 'public works', 'commission', 'agenda', 'report', 'meeting', 'prepared by']
            if any(term in lower_line for term in skip_terms):
                continue
            
            # Clean and add
            for prefix in ['·', '•', '-']:
                if line.startswith(prefix):
                    line = line[1:].strip()
            
            design_projects.add(line)

print('Design projects found:', len(design_projects))

# Check funding
results = []
for funding in funding_records:
    name = funding['Project_Name']
    amount = int(funding['Amount'])
    
    if amount > 50000 and name in design_projects:
        results.append({'name': name, 'amount': amount})

print('\nFiltered count:', len(results))
for r in results:
    print(r['name'], ':', r['amount'])

# Output
output = {'count': len(results), 'projects': results}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:18': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
