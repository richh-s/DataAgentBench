code = """import json

# Extract park projects completed in 2022 from civic documents
civic_path = '/tmp/tmp7p8w2j7u.json'
with open(civic_path) as f:
    civic_docs = json.load(f)

park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for project names containing Park
        if 'Park' in line and len(line) > 5:
            # Skip headers
            if any(skip in line for skip in ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Agenda', 'Commission', 'Public Works']):
                continue
            if line.startswith('(') or line.startswith('cid'):
                continue
            
            # Look ahead for completion status and 2022 date
            next_section = '\n'.join(lines[i:i+15])
            lower_next = next_section.lower()
            
            # Check if completed in 2022
            if ('completed' in lower_next or 'completion' in lower_next) and '2022' in next_section:
                # Avoid future scheduled completions
                if 'will be completed' not in lower_next and 'to be completed' not in lower_next:
                    park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))

# Load funding data
funding_path = '/tmp/tmpg3x0v1j7.json'
with open(funding_path) as f:
    funding = json.load(f)

# Match projects with funding
total_funding = 0
matches = []

for project in unique_projects:
    for rec in funding:
        fund_name = rec.get('Project_Name', '')
        fund_amount = int(rec.get('Amount', 0))
        
        # Match if project name appears in funding name
        if project.lower() in fund_name.lower():
            total_funding += fund_amount
            matches.append({'project': project, 'funding_name': fund_name, 'amount': fund_amount})

result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'funding_matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:126': 'file_storage/functions.query_db:126.json'}

exec(code, env_args)
