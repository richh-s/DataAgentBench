code = """import json
funding_data = json.load(open('/tmp/tmp6v8h4l_u.json'))
civic_docs = json.load(open('/tmp/tmp1i3q6xjc.json'))

# Build funding lookup
funding = {}
for item in funding_data:
    name = item['Project_Name']
    amt = int(item['Amount'])
    funding[name] = funding.get(name, 0) + amt

# Count Spring 2022 references
spring_count = 0
for doc in civic_docs:
    if 'Spring 2022' in doc.get('text', '') or '2022-Spring' in doc.get('text', ''):
        spring_count += 1

# Find project names in Spring docs
spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isupper() and len(line) > 15:
                low = line.lower()
                if 'project' in low or 'improvement' in low:
                    spring_projects.add(line)

# Match
matched = {}
for proj in spring_projects:
    if proj in funding:
        matched[proj] = funding[proj]
    else:
        for funded in funding:
            if proj.lower() in funded.lower():
                matched[funded] = funding[funded]
                break

result = {'count': len(matched), 'total': sum(matched.values())}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}}

exec(code, env_args)
