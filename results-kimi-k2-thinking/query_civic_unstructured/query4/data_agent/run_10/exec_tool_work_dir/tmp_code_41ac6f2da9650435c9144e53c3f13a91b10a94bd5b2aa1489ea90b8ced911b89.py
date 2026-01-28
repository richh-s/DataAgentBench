code = """import json

funding_path = locals()['var_functions.query_db:66']
civic_path = locals()['var_functions.query_db:64']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

funding_lookup = {}
for item in funding_records:
    funding_lookup[item['Project_Name']] = int(item['Total_Amount'])

spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    low_text = text.lower()
    if 'spring 2022' in low_text or '2022-spring' in low_text:
        for line in text.split('\n'):
            line = line.strip()
            if line and line[0].isupper() and len(line) > 15:
                low_line = line.lower()
                if 'project' in low_line or 'improvement' in low_line:
                    spring_projects.add(line)

matched = {}
for project in spring_projects:
    if project in funding_lookup:
        matched[project] = funding_lookup[project]
    else:
        for funded in funding_lookup:
            if project.lower() in funded.lower():
                matched[funded] = funding_lookup[funded]
                break

count = len(matched)
total = sum(matched.values())

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json'}

exec(code, env_args)
