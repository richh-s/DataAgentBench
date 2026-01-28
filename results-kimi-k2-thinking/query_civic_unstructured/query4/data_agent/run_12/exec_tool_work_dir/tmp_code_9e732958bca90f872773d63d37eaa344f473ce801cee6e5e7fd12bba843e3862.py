code = """import json

# Load the civic documents
with open('var_functions.query_db:2', 'r') as f:
    docs = json.load(f)

# Load the funding data
with open('var_functions.query_db:12', 'r') as f:
    funding = json.load(f)

print('Civic docs:', len(docs))
print('Funding records:', len(funding))

# Build funding lookup
fund_lookup = {}
for item in funding:
    fund_lookup[item['Project_Name']] = int(item['Amount'])

# Find Spring 2022 projects
spring_projects = []

# Simple pattern matching
for doc in docs:
    text = doc.get('text', '').lower()
    
    # Look for Spring 2022 patterns
    patterns = ['spring 2022', '2022-spring', 'march 2022', '2022-03', 'april 2022', '2022-04', 'may 2022', '2022-05']
    
    for pattern in patterns:
        if pattern in text:
            # Extract surrounding text to find project names
            # Find lines with project names
            lines = doc.get('text', '').split('\n')
            for line in lines:
                line_clean = line.strip()
                if len(line_clean) > 10 and not line_clean.startswith('(') and not ':' in line_clean[:20]:
                    # Check if this line has funding
                    if line_clean in fund_lookup:
                        spring_projects.append({
                            'name': line_clean,
                            'funding': fund_lookup[line_clean]
                        })

# Remove duplicates
unique = {}
for proj in spring_projects:
    unique[proj['name']] = proj['funding']

spring_count = len(unique)
spring_funding = sum(unique.values())

print('Spring 2022 count:', spring_count)
print('Spring 2022 funding:', spring_funding)

# Check for Morning View specifically
morning_view = '2022 Morning View Resurfacing & Storm Drain Improvements'
if morning_view in fund_lookup and morning_view not in unique:
    unique[morning_view] = fund_lookup[morning_view]
    spring_count = len(unique)
    spring_funding = sum(unique.values())

result = {
    'count': spring_count,
    'total_funding': spring_funding,
    'projects': [{'name': k, 'funding': v} for k, v in unique.items()]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
