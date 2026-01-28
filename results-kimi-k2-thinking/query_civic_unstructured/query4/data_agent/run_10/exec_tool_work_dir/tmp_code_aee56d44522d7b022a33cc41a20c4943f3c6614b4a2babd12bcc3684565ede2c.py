code = """import json

funding_path = locals()['var_functions.query_db:8']
civic_path = locals()['var_functions.query_db:4']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Build funding lookup
funding = {}
for r in funding_data:
    name = r['Project_Name']
    amt = int(r['Amount'])
    funding[name] = funding.get(name, 0) + amt

# Find Spring 2022 projects
spring = []
for doc in civic_docs:
    text = doc.get('text', '')
    t = text.lower()
    if 'spring 2022' in t or '2022-spring' in t:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 15 and line[0].isupper():
                l = line.lower()
                if 'project' in l or 'improvement' in l or 'repair' in l:
                    spring.append(line)

unique_spring = list(set(spring))

# Match
matched = {}
for proj in unique_spring:
    if proj in funding:
        matched[proj] = funding[proj]
    else:
        for funded in funding:
            if proj.lower() in funded.lower():
                matched[funded] = funding[funded]
                break

count = len(matched)
total = sum(matched.values())

print('Matched projects:', count)
print('Total funding:', total)

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs']}

exec(code, env_args)
