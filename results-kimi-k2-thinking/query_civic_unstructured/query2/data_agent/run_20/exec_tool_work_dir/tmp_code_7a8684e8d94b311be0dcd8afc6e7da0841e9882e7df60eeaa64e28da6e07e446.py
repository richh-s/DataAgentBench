code = """import json

# Load data files
civic_path = locals()['var_functions.query_db:18']
funding_path = locals()['var_functions.query_db:5']

civic_docs = json.load(open(civic_path, 'r'))
funding_records = json.load(open(funding_path, 'r'))

# Get funding amounts by project name
funding_amounts = {}
for rec in funding_records:
    funding_amounts[rec.get('Project_Name', '')] = int(rec.get('Amount', 0))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text_data = doc.get('text', '')
    lower_data = text_data.lower()
    
    # Must contain all three keywords
    if 'park' in lower_data and 'completed' in lower_data and '2022' in lower_data:
        lines = text_data.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            lower_line = line.lower()
            if 'park' in lower_line and len(line) > 10:
                # Skip if it's a header/label
                if any(x in lower_line for x in ['status:', 'updates:', 'schedule:', 'project description:', 'page']):
                    continue
                if line.startswith('(') or line.startswith('\u2022'):
                    continue
                
                # Check context
                context_start = max(0, i-2)
                context_end = min(len(lines), i+6)
                context = ' '.join(lines[context_start:context_end]).lower()
                
                if 'completed' in context and '2022' in context:
                    park_projects.append(line)

# Remove duplicates from list
seen_projects = []
[seen_projects.append(p) for p in park_projects if p not in seen_projects]

# Calculate total funding
total_amount = 0
for project in seen_projects:
    if project in funding_amounts:
        total_amount += funding_amounts[project]
    else:
        # Try partial match
        proj_lower = project.lower()
        for fund_proj, fund_amount in funding_amounts.items():
            if proj_lower in fund_proj.lower() or fund_proj.lower() in proj_lower:
                total_amount += fund_amount
                break

result = {
    'projects': seen_projects,
    'project_count': len(seen_projects),
    'total_funding': total_amount
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
