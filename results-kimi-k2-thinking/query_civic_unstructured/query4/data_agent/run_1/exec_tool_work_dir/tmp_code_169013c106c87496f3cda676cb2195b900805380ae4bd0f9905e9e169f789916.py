code = """import json

# Load data from files
civic_file = locals()['var_functions.query_db:42']
funding_file = locals()['var_functions.query_db:18']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

print('Loaded civic_docs:', len(civic_docs))
print('Loaded funding:', len(funding))

# Extract Spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check for 2022 with spring months
        if '2022' in line and any(month in line for month in ['March', 'April', 'May']):
            # Look backwards for project name
            for j in range(max(0, i-6), i):
                prev = lines[j].strip()
                # Heuristic: project names are capitalized, longer than 10 chars, not headers
                if prev and len(prev) > 10 and prev[0].isupper():
                    if 'Updates:' not in prev and 'Schedule:' not in prev and 'Item' not in prev:
                        spring_projects.add(prev)
                        break

print('Spring 2022 projects found:', len(spring_projects))

# Match with funding data
matched = []
total_funding = 0

for proj in spring_projects:
    for fund in funding:
        fund_name = fund['Project_Name']
        # Simple matching
        if proj.lower() in fund_name.lower() or fund_name.lower() in proj.lower():
            amount = int(fund['Amount'])
            matched.append({'project': proj, 'funding': fund_name, 'amount': amount})
            total_funding += amount
            break

print('Matched with funding:', len(matched))
print('Total funding:', total_funding)

# Create result
result = {
    'project_count': len(spring_projects),
    'total_funding': total_funding,
    'funded_projects': len(matched)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
