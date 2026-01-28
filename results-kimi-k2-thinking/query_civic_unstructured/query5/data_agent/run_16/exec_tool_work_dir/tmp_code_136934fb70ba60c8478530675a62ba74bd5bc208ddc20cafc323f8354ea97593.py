code = """import json
import re
import os

funding_path = var_functions.query_db:41
civic_path = var_functions.query_db:40

with open(funding_path) as f:
    funding_data = json.load(f)
    
with open(civic_path) as f:
    civic_data = json.load(f)

disaster_2022_projects = []

for fund_item in funding_data:
    proj_name = fund_item.get('Project_Name', '')
    amount = int(fund_item.get('Amount', 0))
    
    disaster_types = ['FEMA', 'CALOES', 'CALJPIA']
    is_disaster = any(d in proj_name.upper() for d in disaster_types)
    started_2022 = '2022' in proj_name
    
    if is_disaster and started_2022:
        disaster_2022_projects.append({'name': proj_name, 'amount': amount})

for civic_doc in civic_data:
    text = civic_doc.get('text', '')
    
    if '2022' not in text:
        continue
    
    pattern = r'([A-Z][^\n(]*?)\s*\(((?:FEMA|CalOES|CalJPIA)[^)]*Project)\)'
    matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
    
    for match in matches:
        proj_name_clean = match[0].strip()
        if proj_name_clean and len(proj_name_clean) > 5:
            for fund_check in funding_data:
                fund_name = fund_check.get('Project_Name', '')
                fund_amount = int(fund_check.get('Amount', 0))
                
                if proj_name_clean in fund_name or fund_name.startswith(proj_name_clean):
                    disaster_2022_projects.append({'name': fund_name, 'amount': fund_amount})

unique_map = {}
for p in disaster_2022_projects:
    name = p['name']
    if name not in unique_map:
        unique_map[name] = p['amount']

total = sum(unique_map.values())
project_list = [{'name': k, 'amount': v} for k, v in unique_map.items()]

result_final = {'total_funding': total, 'project_count': len(unique_map), 'projects': project_list}
print('__RESULT__:')
print(json.dumps(result_final))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'test': 'hello'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json'}

exec(code, env_args)
