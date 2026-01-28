code = """import json

# Load the data files
civic_file = locals()['var_functions.query_db:4']
funding_file = locals()['var_functions.query_db:8']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Count records
print('Civic documents:', len(civic_docs))
print('Funding records:', len(funding_data))

# Look at civic document structure
for i, doc in enumerate(civic_docs[:3]):
    print('\nDocument', i+1)
    print('Filename:', doc.get('filename'))
    print('Text preview:', doc.get('text')[:200])

# Look at funding data
print('\nFirst 5 funding records:')
for i, record in enumerate(funding_data[:5]):
    print(record)

result = {
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data),
    'sample_civic_text': civic_docs[0].get('text')[:500]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
