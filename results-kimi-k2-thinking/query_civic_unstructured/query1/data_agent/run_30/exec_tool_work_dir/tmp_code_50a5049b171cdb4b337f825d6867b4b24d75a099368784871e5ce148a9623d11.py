code = """import json

funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    docs = json.load(f)

count = 0
for doc in docs:
    text = doc.get('text','').lower()
    if 'capital' in text and 'design' in text:
        for f in funding:
            if int(f['Amount']) > 50000:
                count += 1
                break
        break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
