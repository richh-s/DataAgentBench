code = """import json
import re

civic_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file) as cf:
    civic_docs = json.load(cf)

with open(funding_file) as ff:
    funding_data = json.load(ff)

results = []
seen = set()

for f in funding_data:
    name = f['Project_Name']
    if 'fema' in name.lower():
        project = {}
        project['Project_Name'] = name
        project['Funding_Source'] = f['Funding_Source']
        project['Amount'] = int(f['Amount'])
        project['Status'] = 'No status in civic docs'
        results.append(project)
        seen.add(name.lower())

for doc in civic_docs:
    lines = doc['text'].split('\n')
    for line in lines:
        line_low = line.lower().strip()
        if 'emergency' in line_low or 'fema' in line_low:
            clean_line = line.strip()
            if len(clean_line) > 8 and not clean_line.startswith('('):
                if clean_line.lower() not in seen:
                    matched = None
                    for fund_item in funding_data:
                        if clean_line in fund_item['Project_Name'] or fund_item['Project_Name'] in clean_line:
                            matched = fund_item
                            break
                    
                    if matched:
                        amt = int(matched['Amount'])
                        src = matched['Funding_Source']
                    else:
                        amt = 0
                        src = 'Unknown funding'
                    
                    result = {}
                    result['Project_Name'] = clean_line
                    result['Funding_Source'] = src
                    result['Amount'] = amt
                    result['Status'] = 'Mentioned in civic docs'
                    results.append(result)
                    seen.add(clean_line.lower())

results.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
