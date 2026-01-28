code = """import json

# Load data from file paths
civic_path = var_functions.query_db:10
funding_path = var_functions.query_db:7

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_records = json.load(f)

# Create funding lookup
funding_lookup = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records}

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if document mentions Spring 2022
    if '2022-Spring' in text or 'Spring 2022' in text:
        # Extract potential project names (simple heuristic)
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 10 and 'Project' in line and line[0].isupper():
                spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match with funding
matched = []
for proj in spring_projects:
    if proj in funding_lookup:
        matched.append({'name': proj, 'funding': funding_lookup[proj]})

result = {
    'num_projects': len(matched),
    'total_funding': sum(p['funding'] for p in matched),
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
