code = """import json

civic_path = var_functions.query_db:10
funding_path = var_functions.query_db:7

# Load data
civic_docs = json.load(open(civic_path)) if isinstance(civic_path, str) and civic_path.endswith('.json') else civic_path
funding_records = json.load(open(funding_path)) if isinstance(funding_path, str) and funding_path.endswith('.json') else funding_path

# Build funding map
funding = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records}

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check for Spring 2022 indicators
    if '2022-Spring' in text or 'Spring 2022' in text or '2022-March' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Simple heuristic for project names
            if len(line) > 15 and any(k in line for k in ['Project', 'Improvements', 'Repairs']):
                if line[0].isupper():
                    spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match with funding
matched = []
for proj in spring_projects:
    if proj in funding:
        matched.append({'name': proj, 'funding': funding[proj]})

result = {
    'num_projects': len(matched),
    'total_funding': sum(p['funding'] for p in matched),
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
