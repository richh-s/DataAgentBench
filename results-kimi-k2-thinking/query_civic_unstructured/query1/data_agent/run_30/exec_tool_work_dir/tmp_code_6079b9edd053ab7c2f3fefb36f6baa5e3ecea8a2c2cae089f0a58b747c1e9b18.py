code = """import json

funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:2

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Data loaded successfully')

count = 0

for fund in funding_records:
    amount = int(fund['Amount'])
    if amount > 50000:
        project_name = fund['Project_Name'].lower()
        
        for doc in civic_docs:
            text = doc.get('text', '').lower()
            
            if project_name in text and 'capital' in text and 'design' in text:
                count = count + 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
