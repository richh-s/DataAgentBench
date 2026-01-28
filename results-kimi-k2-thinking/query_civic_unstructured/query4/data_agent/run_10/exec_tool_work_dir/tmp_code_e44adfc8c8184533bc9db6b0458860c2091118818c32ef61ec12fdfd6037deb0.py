code = """import json, os

# Load the actual data from the files
funding_file = locals()['var_functions.query_db:114']
civic_file = locals()['var_functions.query_db:116']

print('Funding file path:', funding_file)
print('Civic file path:', civic_file)

# Read the files
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Show first few funding records
print('\nFirst 5 funding records:')
for i in range(5):
    print(f"  {funding_data[i]['Project_Name']}: ${funding_data[i]['Total_Amount']}")

# Show first civic document
print('\nFirst civic document:')
print('  Filename:', civic_docs[0]['filename'])
text_preview = civic_docs[0]['text'][:500]
print('  Text preview:', text_preview.replace('\n', ' '))

# Check for Spring 2022 in all civic documents
spring_docs = []
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'spring 2022' in text or '2022-spring' in text:
        spring_docs.append(doc)

print('\nDocuments with Spring 2022 references:', len(spring_docs))
for doc in spring_docs:
    print('  -', doc['filename'])

result = {
    'funding_projects': len(funding_data),
    'civic_docs': len(civic_docs),
    'spring_2022_docs': len(spring_docs)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}, 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json'}

exec(code, env_args)
