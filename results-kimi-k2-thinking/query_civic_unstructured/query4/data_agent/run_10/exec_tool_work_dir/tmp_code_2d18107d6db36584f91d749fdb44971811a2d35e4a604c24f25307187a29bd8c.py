code = """import json

funding_path = locals()['var_functions.query_db:8']
civic_path = locals()['var_functions.query_db:4']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

funding = {}
for r in funding_data:
    name = r['Project_Name']
    amt = int(r['Amount'])
    funding[name] = funding.get(name, 0) + amt

spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and line[0].isupper() and len(line) > 15:
                low = line.lower()
                if 'project' in low or 'improvement' in low or 'repair' in low:
                    spring_projects.add(line)

matched = {}
for proj in spring_projects:
    if proj in funding:
        matched[proj] = funding[proj]
    else:
        for funded in funding:
            if proj.lower() in funded.lower():
                matched[funded] = funding[funded]
                break

result = {'count': len(matched), 'total_funding': sum(matched.values())}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}}

exec(code, env_args)
