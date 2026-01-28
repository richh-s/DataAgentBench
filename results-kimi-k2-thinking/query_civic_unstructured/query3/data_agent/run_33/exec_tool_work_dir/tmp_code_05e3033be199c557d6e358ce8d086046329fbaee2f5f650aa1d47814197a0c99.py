code = """import json, re, sys

civic_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path) as cf:
    civic_docs = json.load(cf)

with open(funding_path) as ff:
    funding_data = json.load(ff)

results = []
seen = set()

for f in funding_data:
    if 'fema' in f['Project_Name'].lower():
        results.append([f['Project_Name'], f['Funding_Source'], int(f['Amount']), 'Status: Not in civic docs'])
        seen.add(f['Project_Name'].lower())

for doc in civic_docs:
    lines = doc['text'].split('\n')
    for line in lines:
        line_lower = line.lower().strip()
        if 'emergency' in line_lower or 'fema' in line_lower:
            clean = line.strip()
            if len(clean) > 8 and not clean.startswith('(') and clean.lower() not in seen:
                funding_match = None
                for fund_item in funding_data:
                    if clean in fund_item['Project_Name'] or fund_item['Project_Name'] in clean:
                        funding_match = fund_item
                        break
                
                if funding_match:
                    amount_val = int(funding_match['Amount'])
                    source_val = funding_match['Funding_Source']
                else:
                    amount_val = 0
                    source_val = 'Unknown'
                
                results.append([clean, source_val, amount_val, 'Status: In civic docs'])
                seen.add(clean.lower())

results.sort(key=lambda x: x[2], reverse=True)

output = {'projects': results}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
