code = """import json

# Load the civic documents data
civic_docs = json.load(open(locals()['var_functions.query_db:2'], 'r'))

# Load the funding data
funding_records = json.load(open(locals()['var_functions.query_db:5'], 'r'))

# Build funding lookup by project name
funding_lookup = {}
for record in funding_records:
    pname = record.get('Project_Name', '')
    amt = int(record.get('Amount', 0))
    if pname:
        funding_lookup[pname] = amt

# Find park projects completed in 2022
completed_2022_park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('
')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        lower_line = line.lower()
        
        # Look for project names containing 'park'
        if 'park' in lower_line and len(line) > 10:
            # Skip header/metadata lines
            is_header = False
            header_words = ['status:', 'updates:', 'schedule:', 'project description:', 'page']
            for hw in header_words:
                if hw in lower_line:
                    is_header = True
                    break
            if is_header:
                continue
            if line.startswith('(') or line.startswith('•'):
                continue
            
            # Check if completed in 2022 by looking at context
            context_start = max(0, i-2)
            context_end = min(len(lines), i+6)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'completed' in context and '2022' in context:
                completed_2022_park_projects.append(line)

# Remove duplicate project names
unique_projects = []
added = set()
for p in completed_2022_park_projects:
    if p not in added:
        added.add(p)
        unique_projects.append(p)

# Get funding amounts for these projects
total_funding = 0
project_details = []

for project in unique_projects:
    if project in funding_lookup:
        amount = funding_lookup[project]
        total_funding += amount
        project_details.append({'project': project, 'amount': amount})
    else:
        # Try to find similar project names in funding data
        for fproj, famount in funding_lookup.items():
            if project.lower() in fproj.lower() or fproj.lower() in project.lower():
                total_funding += famount
                project_details.append({'project': project, 'amount': famount, 'matched': fproj})
                break

result = {
    'completed_2022_park_projects': unique_projects,
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'project_details': project_details
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
