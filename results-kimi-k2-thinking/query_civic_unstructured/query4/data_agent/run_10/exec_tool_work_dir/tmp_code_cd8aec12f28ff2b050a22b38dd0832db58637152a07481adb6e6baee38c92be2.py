code = """import json

funding_path = locals()['var_functions.query_db:114']
civic_path = locals()['var_functions.query_db:116']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Total_Amount'])
    funding_lookup[name] = amount

# Find Spring 2022 projects
spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    ltext = text.lower()
    if 'spring 2022' in ltext or '2022-spring' in ltext:
        for line in text.split('\n'):
            line = line.strip()
            if line and line[0].isupper() and len(line) > 15:
                lline = line.lower()
                if 'project' in lline or 'improvement' in lline or 'repair' in lline:
                    spring_projects.add(line)

print('Spring candidates:', len(spring_projects))

# Match with funding
matched = {}
for proj in spring_projects:
    if proj in funding_lookup:
        matched[proj] = funding_lookup[proj]
    else:
        for funded in funding_lookup:
            if proj.lower() in funded.lower():
                matched[funded] = funding_lookup[funded]
                break

count = len(matched)
total = sum(matched.values())

print('Final count:', count, 'Total funding:', total)

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}, 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json'}

exec(code, env_args)
