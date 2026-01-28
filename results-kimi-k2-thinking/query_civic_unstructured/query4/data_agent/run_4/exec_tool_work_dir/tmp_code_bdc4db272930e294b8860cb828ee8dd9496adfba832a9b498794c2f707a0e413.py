code = """import json

# Load the data from the stored files
civic_docs_file = var_functions.query_db:2
funding_file = var_functions.query_db:4

# Read civic documents
civic_docs = []
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_file if isinstance(civic_docs_file, list) else []

# Read funding data
funding_data = []
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file if isinstance(funding_file, list) else []

print('Data loaded:')
print(f'- Civic documents: {len(civic_docs)}')
print(f'- Funding records: {len(funding_data)}')

# Create funding lookup
funding_lookup = {}
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[proj_name] = amount

print(f'- Unique projects with funding: {len(funding_lookup)}')

# Show sample data
if civic_docs:
    print(f'\nFirst civic doc filename: {civic_docs[0].get("filename")}')
    print(f'First civic doc text sample: {civic_docs[0].get("text", "")[:200]}...')

if funding_data:
    print(f'\nFirst funding record: {funding_data[0]}')

# Let's search for Spring 2022 in the text
spring_2022_matches = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        spring_2022_matches.append(doc)

print(f'\nDocuments mentioning Spring 2022: {len(spring_2022_matches)}')

result = {
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data),
    'funding_projects_count': len(funding_lookup),
    'spring_2022_docs_count': len(spring_2022_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
