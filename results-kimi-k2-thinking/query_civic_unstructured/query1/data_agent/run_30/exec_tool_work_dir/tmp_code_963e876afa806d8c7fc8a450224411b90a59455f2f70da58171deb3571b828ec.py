code = """import json

# Get file paths from storage
funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:2']

# Load the data
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_records), 'funding records and', len(civic_docs), 'civic documents')

# Count capital design projects with funding > $50,000
count = 0

for fund in funding_records:
    amount = int(fund['Amount'])
    if amount > 50000:
        project_name = fund['Project_Name'].lower()
        
        for doc in civic_docs:
            text = doc.get('text', '').lower()
            
            # Check if project appears in document and is a capital design project
            if project_name in text:
                if 'capital' in text and 'design' in text:
                    count += 1
                    break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
