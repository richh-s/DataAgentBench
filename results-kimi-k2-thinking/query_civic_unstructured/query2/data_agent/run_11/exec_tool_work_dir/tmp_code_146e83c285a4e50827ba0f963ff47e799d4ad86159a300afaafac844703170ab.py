code = """import json

# Load data from files
civic_file_path = '/tmp/tmp7p8w2j7u.json'
funding_file_path = '/tmp/tmpg3x0v1j7.json'

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file_path, 'r') as f:
    funding = json.load(f)

# Based on document inspection, find park projects completed in 2022
# From the agenda text we saw: "Bluffs Park Shade Structure" was completed November 2022

park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for park projects with 2022 completion
    if 'Park' in text and '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        lines = text.splitlines()
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for project names containing Park
            if 'Park' in line and len(line) > 5:
                # Skip headers
                if 'Subject:' in line or 'Page' in line or 'Item' in line:
                    continue
                if line.startswith('('):
                    continue
                
                # Check context for completion in 2022
                start = max(0, i-2)
                end = min(len(lines), i+15)
                context = ' '.join(lines[start:end])
                
                context_lower = context.lower()
                if 'completed' in context_lower and '2022' in context:
                    if 'will be completed' not in context_lower:
                        park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))

# Find funding matches
total_funding = 0
matches = []

for project in unique_projects:
    project_lower = project.lower()
    for rec in funding:
        fund_name = rec.get('Project_Name', '')
        fund_amount = int(rec.get('Amount', 0))
        
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
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:126': 'file_storage/functions.query_db:126.json'}

exec(code, env_args)
