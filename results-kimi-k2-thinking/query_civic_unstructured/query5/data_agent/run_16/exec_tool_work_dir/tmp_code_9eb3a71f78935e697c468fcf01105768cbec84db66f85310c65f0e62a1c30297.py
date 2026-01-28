code = """import json
import re
import os

funding_path = var_functions.query_db:30
civic_path = var_functions.query_db:31

with open(funding_path) as f1:
    funding_list = json.load(f1)

with open(civic_path) as f2:
    civic_list = json.load(f2)

disaster_in_2022 = []

for fund_item in funding_list:
    proj_name = fund_item.get('Project_Name', '')
    amount = int(fund_item.get('Amount', 0))
    
    is_disaster = any(keyword in proj_name.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA'])
    has_2022 = '2022' in proj_name
    
    if is_disaster and has_2022:
        disaster_in_2022.append({'name': proj_name, 'amount': amount})

for civic_doc in civic_list:
    doc_text = civic_doc.get('text', '')
    if '2022' not in doc_text:
        continue
    
    lines = doc_text.split('\n')
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped or '2022' not in line_stripped:
            continue
        
        if any(keyword in line_stripped.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA']):
            clean_name_match = re.search(r'([A-Z][^\(]*?)(?:\s*\([^)]*\)\s*)?$', line_stripped)
            if clean_name_match:
                clean_name = clean_name_match.group(1).strip()
                if clean_name:
                    for fund_check in funding_list:
                        fund_name = fund_check.get('Project_Name', '')
                        if clean_name in fund_name or fund_name in clean_name:
                            amount_val = int(fund_check.get('Amount', 0))
                            disaster_in_2022.append({'name': fund_name, 'amount': amount_val})

unique_dict = {}
for p in disaster_in_2022:
    n = p['name']
    if n not in unique_dict:
        unique_dict[n] = p['amount']

total_fund = sum(unique_dict.values())
project_details = [{'name': k, 'amount': v} for k, v in unique_dict.items()]

output = {'total_funding': total_fund, 'project_count': len(unique_dict), 'projects': project_details}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'test': 'hello'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
