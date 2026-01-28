code = """import json

# Direct approach - load the actual temp files from the system
civic_docs = json.load(open('/tmp/tmpu9m4oj6r.json'))
funding = json.load(open('/tmp/tmpg3x0v1j7.json'))

print('Civic docs loaded:', len(civic_docs))
print('Funding records loaded:', len(funding))

# Based on the document preview, we know these park projects were completed in 2022:
# From the preview: "Bluffs Park Shade Structure" was completed November 2022
# Let's search for this pattern

park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Split lines safely
    lines = text.splitlines()
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for park project names
        if 'Park' in line and len(line) > 5:
            # Skip headers
            if 'Subject:' in line or 'Page' in line or 'Item' in line:
                continue
            if line.startswith('('):
                continue
            
            # Check context
            context_start = max(0, i-2)
            context_end = min(len(lines), i+15)
            context = ' '.join(lines[context_start:context_end])
            
            # Check for completion in 2022
            context_lower = context.lower()
            if ('completed' in context_lower or 'completion' in context_lower) and '2022' in context:
                if 'will be completed' not in context_lower:
                    park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))

# Match with funding
total_funding = 0
matches = []

for project in unique_projects:
    project_lower = project.lower()
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        if project_lower in fund_name.lower():
            total_funding += fund_amount
            matches.append({'project': project, 'funding_name': fund_name, 'amount': fund_amount})

result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'matches': matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:126': 'file_storage/functions.query_db:126.json'}

exec(code, env_args)
