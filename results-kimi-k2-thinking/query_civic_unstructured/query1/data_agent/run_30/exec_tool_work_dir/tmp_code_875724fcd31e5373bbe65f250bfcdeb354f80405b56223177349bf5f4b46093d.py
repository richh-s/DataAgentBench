code = """import json

funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:2

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

count = 0
matched = []

for fund in funding_records:
    if int(fund['Amount']) > 50000:
        proj_name = fund['Project_Name'].lower()
        
        for doc in civic_docs:
            doc_text = doc.get('text', '').lower()
            if proj_name in doc_text:
                if 'capital' in doc_text and 'design' in doc_text:
                    count += 1
                    matched.append(fund['Project_Name'])
                    break

result = {'count': count, 'matched_projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
