code = """import json

# Simple load of documents
civic_docs = json.load(open(locals()['var_functions.query_db:18'], 'r'))
funding_data = json.load(open(locals()['var_functions.query_db:5'], 'r'))

# Build funding lookup
funding_lookup = {}
for rec in funding_data:
    funding_lookup[rec.get('Project_Name', '')] = int(rec.get('Amount', 0))

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        lower_line = line.lower()
        if 'park' in lower_line:
            # Skip metadata
            if any(x in lower_line for x in ['status:', 'updates:', 'schedule:', 'description:', 'page']):
                continue
            if line.startswith('(') or line.startswith('\u2022'):
                continue
            
            # Check context
            context_start = max(0, i-2)
            context_end = min(len(lines), i+6)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'completed' in context and '2022' in context:
                park_projects_2022.append(line)

# Remove duplicates
unique = []
for p in park_projects_2022:
    if p not in unique:
        unique.append(p)

# Sum funding
total = 0
for proj in unique:
    if proj in funding_lookup:
        total += funding_lookup[proj]
    else:
        proj_lower = proj.lower()
        for fund_proj, amount in funding_lookup.items():
            if proj_lower in fund_proj.lower():
                total += amount
                break

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
