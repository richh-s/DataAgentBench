code = """import json

# Load documents
civic_docs = json.load(open(locals()['var_functions.query_db:18'], 'r'))
funding_records = json.load(open(locals()['var_functions.query_db:5'], 'r'))

# Build funding dictionary
funding_dict = {}
for rec in funding_records:
    funding_dict[rec.get('Project_Name', '')] = int(rec.get('Amount', 0))

# Search for park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        lower = line.lower()
        if 'park' in lower:
            # Skip header lines
            if any(x in lower for x in ['status:', 'updates:', 'schedule:', 'description:', 'page']):
                continue
            if line.startswith('('):
                continue
            
            # Get context
            context_start = max(0, i-2)
            context_end = min(len(lines), i+6)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'completed' in context and '2022' in context:
                park_projects.append(line)

# Remove duplicates
unique_projects = []
seen = set()
for p in park_projects:
    if p not in seen:
        seen.add(p)
        unique_projects.append(p)

# Sum funding amounts
total = 0
for proj in unique_projects:
    if proj in funding_dict:
        total += funding_dict[proj]
    else:
        # Try partial matching
        proj_lower = proj.lower()
        for fund_proj, amount in funding_dict.items():
            if proj_lower in fund_proj.lower() or fund_proj.lower() in proj_lower:
                total += amount
                break

print('__RESULT__:')
print(json.dumps({'total_funding': total}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
