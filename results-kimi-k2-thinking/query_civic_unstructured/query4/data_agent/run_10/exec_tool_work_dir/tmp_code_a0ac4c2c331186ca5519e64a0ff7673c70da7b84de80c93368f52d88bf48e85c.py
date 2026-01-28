code = """import json

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

# Load data from the files we've queried
funding_result = load_json(locals()['var_functions.query_db:66'])
civic_result = load_json(locals()['var_functions.query_db:64'])

print('Funding records:', len(funding_result))
print('Civic documents:', len(civic_result))

# Show some sample data
for doc in civic_result[:3]:
    print('Doc filename:', doc.get('filename'))
    preview = doc.get('text', '')[:200]
    print('Text preview:', preview.replace('\n', ' '))
    print('---')

# Count Spring 2022 references
spring_refs = 0
for doc in civic_result:
    text = doc.get('text', '').lower()
    if 'spring 2022' in text or '2022-spring' in text:
        spring_refs += 1

print('Documents with Spring 2022:', spring_refs)

result = {'spring_docs': spring_refs, 'total_docs': len(civic_result)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json'}

exec(code, env_args)
