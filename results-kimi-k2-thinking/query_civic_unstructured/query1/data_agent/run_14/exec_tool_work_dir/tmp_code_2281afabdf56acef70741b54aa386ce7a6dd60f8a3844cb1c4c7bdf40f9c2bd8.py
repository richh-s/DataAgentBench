code = """import json
import re

f_file = globals()['var_functions.query_db:4']
c_file = globals()['var_functions.query_db:5']

with open(f_file, 'r') as f:
    funding = json.load(f)

with open(c_file, 'r') as f:
    civic = json.load(f)

funded_projects = {}
for rec in funding:
    amt = int(rec['Amount'])
    if amt > 50000:
        funded_projects[rec['Project_Name']] = amt

count = 0
names = []
for doc in civic:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    if 'design' in text_lower and 'capital' in text_lower:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isupper() and line in funded_projects:
                count = count + 1
                names.append(line)

result = {'count': count, 'projects': names}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5'], 'var_functions.execute_python:20': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding_name': 'Birdview Avenue Improvements'}, 'var_functions.execute_python:22': {'projects_with_funding': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:24': {'funding_projects': 276, 'message': 'Loaded funding data'}, 'var_functions.execute_python:26': {'total_funding_projects': 276, 'funding_dict_size': 276}}

exec(code, env_args)
