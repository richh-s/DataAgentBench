code = """import json

# Load data
civic_docs = json.load(open(locals()['var_functions.query_db:18'], 'r'))
funding = json.load(open(locals()['var_functions.query_db:5'], 'r'))

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    if 'completed' in lower_text and '2022' in lower_text and 'park' in lower_text:
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            lower_line = line.lower()
            
            if 'park' in lower_line and len(line) > 10:
                # Skip headers and metadata
                skip_terms = ['status:', 'updates:', 'schedule:', 'project description:', 'page']
                is_header = False
                for term in skip_terms:
                    if term in lower_line:
                        is_header = True
                        break
                if is_header:
                    continue
                if line.startswith('(') or line.startswith('•'):
                    continue
                
                # Check context for 2022 completion
                context_start = max(0, i-2)
                context_end = min(len(lines), i+6)
                context_text = ' '.join(lines[context_start:context_end]).lower()
                
                if 'completed' in context_text and '2022' in context_text:
                    park_projects_2022.append(line)

# Remove duplicates
unique_projects = []
added = set()
for proj in park_projects_2022:
    if proj not in added:
        added.add(proj)
        unique_projects.append(proj)

# Get total funding
funding_lookup = {}
for record in funding:
    funding_lookup[record.get('Project_Name', '')] = int(record.get('Amount', 0))

total_funding = 0
for project in unique_projects:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
    else:
        # Try fuzzy matching
        proj_lower = project.lower()
        for fproj, amount in funding_lookup.items():
            if proj_lower in fproj.lower() or fproj.lower() in proj_lower:
                total_funding += amount
                break

result = {'total_funding': total_funding, 'project_count': len(unique_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
