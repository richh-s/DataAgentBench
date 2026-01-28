code = """import json, re

# Load data from storage
civic_docs = json.load(open(var_functions.query_db:4))
funding_records = json.load(open(var_functions.query_db:8))

# Build funding lookup with aggregated amounts
funding = {}
for r in funding_records:
    name = r['Project_Name']
    amt = int(r['Amount'])
    funding[name] = funding.get(name, 0) + amt

# Find Spring 2022 projects in civic documents
spring = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isupper() and len(line) > 15:
                low = line.lower()
                if 'project' in low or 'improvement' in low or 'repair' in low:
                    spring.append(line)

# Remove duplicates
unique_spring = list(set(spring))

# Match with funding database
matched = {}
for proj in unique_spring:
    if proj in funding:
        matched[proj] = funding[proj]
    else:
        for funded in funding:
            if proj.lower() in funded.lower() or funded.lower() in proj.lower():
                matched[funded] = funding[funded]
                break

count = len(matched)
total = sum(matched.values())

result = {'count': count, 'total_funding': total, 'projects': list(matched.keys())}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
