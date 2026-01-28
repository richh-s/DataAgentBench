code = """import json
import re

f1 = open('divey_tmp_funding.json', 'w')
f1.write(str(var_functions.query_db:41))
f1.close()

f2 = open('divey_tmp_civic.json', 'w')
f2.write(str(var_functions.query_db:40))
f2.close()

with open('divey_tmp_funding.json') as f:
    funding = json.load(f)

with open('divey_tmp_civic.json') as f:
    civic = json.load(f)

total = 0
projects = []

for item in funding:
    name = item.get('Project_Name', '')
    amt = int(item.get('Amount', 0))
    
    if '2022' in name and any(k in name.upper() for k in ['FEMA','CALOES','CALJPIA']):
        total += amt
        projects.append({'name': name, 'amount': amt})

for doc in civic:
    text = doc.get('text', '')
    if '2022' in text:
        matches = re.findall(r'([A-Z][^\n(]*?)\s*\(((?:FEMA|CalOES|CalJPIA)[^)]*Project)\)', text, re.IGNORECASE)
        for match in matches:
            proj_name = match[0].strip()
            for fund_item in funding:
                fund_name = fund_item.get('Project_Name', '')
                fund_amt = int(fund_item.get('Amount', 0))
                if proj_name in fund_name:
                    if not any(p['name'] == fund_name for p in projects):
                        total += fund_amt
                        projects.append({'name': fund_name, 'amount': fund_amt})

result = {'total_funding': total, 'project_count': len(projects), 'projects': projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'test': 'hello'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json'}

exec(code, env_args)
