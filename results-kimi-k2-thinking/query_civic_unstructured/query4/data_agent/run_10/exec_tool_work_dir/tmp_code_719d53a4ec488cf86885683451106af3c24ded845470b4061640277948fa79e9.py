code = """import json

# Use the data from storage variables directly
funding_data = json.load(open('/tmp/tmp6v8h4l_u.json'))
civic_docs = json.load(open('/tmp/tmp1i3q6xjc.json'))

print('Loaded', len(funding_data), 'funding records and', len(civic_docs), 'civic documents')

# Build funding lookup
funding_lookup = {}
for r in funding_data:
    name = r['Project_Name']
    amt = int(r['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amt

# Simple search for Spring 2022
spring_count = 0
for doc in civic_docs:
    text = doc['text']
    if 'Spring 2022' in text or '2022-Spring' in text:
        spring_count += 1

print('Documents mentioning Spring 2022:', spring_count)

# Simple result
result = {'test_count': spring_count, 'funding_projects': len(funding_lookup)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json'}

exec(code, env_args)
