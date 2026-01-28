code = """import json

# Load the data - use the correct storage keys
with open(locals()['var_functions.query_db:2'], 'r') as f:
    docs = json.load(f)

with open(locals()['var_functions.query_db:12'], 'r') as f:
    funding = json.load(f)

print('Loaded %d documents and %d funding records' % (len(docs), len(funding)))

# Build funding lookup by project name
funding_lookup = {}
for rec in funding:
    funding_lookup[rec['Project_Name']] = int(rec['Amount'])

# Find projects with Spring 2022 start dates
spring_2022_projects = []

# Patterns to look for
spring_patterns = ['spring 2022', '2022-spring', 'march 2022', '2022-march', '2022-03', 'april 2022', '2022-april', '2022-04', 'may 2022', '2022-may', '2022-05']

for doc in docs:
    text = doc.get('text', '').lower()
    
    # Check if this document mentions Spring 2022
    found_spring = False
    for pattern in spring_patterns:
        if pattern in text:
            found_spring = True
            break
    
    if found_spring:
        # Extract potential project names - look for lines that are likely project names
        for line in doc.get('text', '').split('\n'):
            line_clean = line.strip()
            # Project names are typically longer and don't start with bullets
            if len(line_clean) > 8 and not line_clean.startswith('(') and ' ' in line_clean:
                # Check if this project has funding
                if line_clean in funding_lookup:
                    spring_2022_projects.append({
                        'name': line_clean,
                        'funding': funding_lookup[line_clean]
                    })

# Remove duplicate projects
unique_projects = {}
for proj in spring_2022_projects:
    unique_projects[proj['name']] = proj['funding']

# Also check for specific known 2022 project
if '2022 Morning View Resurfacing & Storm Drain Improvements' in funding_lookup:
    mv_name = '2022 Morning View Resurfacing & Storm Drain Improvements'
    if mv_name not in unique_projects:
        unique_projects[mv_name] = funding_lookup[mv_name]

# Calculate final results
count = len(unique_projects)
total_funding = sum(unique_projects.values())

print('Spring 2022 projects: %d' % count)
print('Total funding: %d' % total_funding)

# Return result
result = {
    'count': count,
    'total_funding': total_funding,
    'projects': [{'name': k, 'amount': v} for k, v in unique_projects.items()]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
