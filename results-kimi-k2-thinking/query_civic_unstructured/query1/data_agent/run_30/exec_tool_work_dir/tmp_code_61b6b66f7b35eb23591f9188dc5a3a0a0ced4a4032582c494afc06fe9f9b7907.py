code = """import json

funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    docs = json.load(f)

print('Funding records:', len(funding))
print('Civic documents:', len(docs))

# Find matches
count = 0
for fund in funding:
    amount = int(fund['Amount'])
    if amount > 50000:
        name = fund['Project_Name'].lower()
        for doc in docs:
            text = doc.get('text', '').lower()
            if name in text and 'capital' in text and 'design' in text:
                count += 1
                break

print('Matches found:', count)
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
