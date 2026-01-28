code = """import json

# Load all civic documents
civic_docs = json.load(open(locals()['var_functions.query_db:18'], 'r'))

# Load funding data
funding_records = json.load(open(locals()['var_functions.query_db:5'], 'r'))

# Create funding lookup
funding_lookup = {}
for rec in funding_records:
    funding_lookup[rec.get('Project_Name', '')] = int(rec.get('Amount', 0))

# Initialize results
park_projects_2022 = []

# Search through documents
for doc in civic_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Look for park projects completed in 2022
    if 'park' in text_lower and 'completed' in text_lower and '2022' in text_lower:
        # Look for specific patterns
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            lower_line = line.lower()
            
            # Find project name lines with park
            if 'park' in lower_line and len(line) > 10:
                # Skip headers
                if any(x in lower_line for x in ['status:', 'updates:', 'schedule:', 'description:', 'page']):
                    continue
                if line.startswith('(') or line.startswith('\u2022'):
                    continue
                
                # Check context around this line
                context_start = max(0, i-3)
                context_end = min(len(lines), i+6)
                context = ' '.join(lines[context_start:context_end])
                
                if 'completed' in context and '2022' in context:
                    park_projects_2022.append(line)

# Remove duplicates
unique_projects = []
seen = set()
for proj in park_projects_2022:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

# Sum up funding
total_funding = 0
for project in unique_projects:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
    else:
        # Check for similar names
        proj_lower = project.lower()
        for fund_name, amount in funding_lookup.items():
            if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
                total_funding += amount
                break

print('__RESULT__:')
print(json.dumps({
    'projects_found': unique_projects,
    'project_count': len(unique_projects),
    'total_funding': total_funding
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
