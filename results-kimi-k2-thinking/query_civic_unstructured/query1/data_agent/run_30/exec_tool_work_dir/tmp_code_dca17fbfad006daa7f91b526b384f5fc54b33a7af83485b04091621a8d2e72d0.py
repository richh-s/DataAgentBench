code = """import json

funding_result = var_functions.query_db:0
civic_result = var_functions.query_db:2

print('Funding result type:', type(funding_result))
print('Civic result type:', type(civic_result))

if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_result

if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        docs = json.load(f)
else:
    docs = civic_result

print('Funding count:', len(funding))
print('Docs count:', len(docs))

# Main logic
count = 0
for fund in funding:
    amt = int(fund['Amount'])
    if amt > 50000:
        pname = fund['Project_Name'].lower()
        for doc in docs:
            text = doc.get('text', '').lower()
            if pname in text and 'capital' in text and 'design' in text:
                count += 1
                break

print('Count:', count)
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
