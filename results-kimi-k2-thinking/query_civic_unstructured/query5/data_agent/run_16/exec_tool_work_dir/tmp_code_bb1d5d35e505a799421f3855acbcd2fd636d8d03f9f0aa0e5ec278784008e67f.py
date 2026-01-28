code = """import json
import re

# Read both JSON files
with open('funding_data.json', 'w') as f:
    json.dump(var_functions.query_db:41, f)

with open('civic_data.json', 'w') as f:
    json.dump(var_functions.query_db:40, f)

with open('funding_data.json') as f:
    funding_data = json.load(f)

with open('civic_data.json') as f:
    civic_data = json.load(f)

# Find disaster projects started in 2022
projects = {}

for item in funding_data:
    name = item.get('Project_Name', '')
    amt = int(item.get('Amount', 0))
    
    if '2022' in name and any(kw in name.upper() for kw in ['FEMA', 'CALOES', 'CALJPIA']):
        projects[name] = amt

for doc in civic_data:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    
    matches = re.findall(r'([A-Z][^\n(]*?)\s*\(((?:FEMA|CalOES|CalJPIA)[^)]*Project)\)', text, re.IGNORECASE)
    for match in matches:
        proj_name = match[0].strip()
        for fund_item in funding_data:
            fund_name = fund_item.get('Project_Name', '')
            fund_amt = int(fund_item.get('Amount', 0))
            if proj_name in fund_name and fund_name not in projects:
                projects[fund_name] = fund_amt

total = sum(projects.values())
result = {'total_funding': total, 'project_count': len(projects), 'projects': [{'name': k, 'amount': v} for k, v in projects.items()]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'test': 'hello'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json'}

exec(code, env_args)
