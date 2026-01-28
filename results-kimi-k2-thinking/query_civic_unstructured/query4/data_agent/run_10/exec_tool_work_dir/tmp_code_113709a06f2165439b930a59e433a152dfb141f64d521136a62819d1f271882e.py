code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:66']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
civic_path = locals()['var_functions.query_db:64']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding_records))
print('Civic docs:', len(civic_docs))

# Build simple funding lookup
funding = {}
for item in funding_records:
    name = item['Project_Name']
    amount = int(item['Total_Amount'])
    funding[name] = amount

# Simple search for Spring 2022
spring_count = 0
for doc in civic_docs:
    text = doc['text']
    if 'Spring 2022' in text or '2022-Spring' in text:
        spring_count += 1

result = {'spring_2022_docs': spring_count, 'funding_projects': len(funding)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json'}

exec(code, env_args)
