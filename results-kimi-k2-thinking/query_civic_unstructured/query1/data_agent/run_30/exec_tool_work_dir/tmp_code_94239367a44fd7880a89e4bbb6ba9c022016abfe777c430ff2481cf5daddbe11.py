code = """import json

funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:2

with open(funding_path, 'r') as f:
    funding = json.load(f)

with open(civic_path, 'r') as f:
    docs = json.load(f)

print('Records loaded')

# Count matches
count = 0
matched = []

for fund in funding:
    if int(fund['Amount']) > 50000:
        fund_name = fund['Project_Name'].lower()
        
        for doc in docs:
            text = doc.get('text', '').lower()
            
            # Check project name appears in document  
            if fund_name in text:
                # Check if capital design project
                if 'capital' in text and 'design' in text:
                    count = count + 1
                    matched.append(fund['Project_Name'])
                    break

result = {'count': count, 'matched': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
