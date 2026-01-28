code = """import json, re

funding_path = locals()['var_functions.query_db:8']
civic_path = locals()['var_functions.query_db:4']

funding_data = json.load(open(funding_path))
civic_docs = json.load(open(civic_path))

funding_lookup = {}
for r in funding_data:
    funding_lookup[r['Project_Name']] = funding_lookup.get(r['Project_Name'], 0) + int(r['Amount'])

spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text or 'March 2022' in text or 'April 2022' in text or 'May 2022' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 15 and line[0].isupper():
                low = line.lower()
                if 'project' in low or 'improvement' in low or 'repair' in low:
                    spring_projects.add(line)

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

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500}

exec(code, env_args)
