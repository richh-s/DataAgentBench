code = """import json

f_file = globals()['var_functions.query_db:4']
c_file = globals()['var_functions.query_db:5']

with open(f_file) as f:
    funding = json.load(f)
with open(c_file) as f:
    civic = json.load(f)

funded = {}
for rec in funding:
    amt = int(rec['Amount'])
    if amt > 50000:
        funded[rec['Project_Name']] = amt

count = 0
project_list = []

for doc in civic:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
        elif 'Capital Improvement Projects' in line and 'Design' not in line:
            in_design_section = False
        
        if in_design_section and line and line[0].isupper():
            if line in funded:
                count += 1
                project_list.append(line)

result = {'count': count, 'sample_projects': project_list[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5'], 'var_functions.execute_python:20': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding_name': 'Birdview Avenue Improvements'}, 'var_functions.execute_python:22': {'projects_with_funding': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:24': {'funding_projects': 276, 'message': 'Loaded funding data'}, 'var_functions.execute_python:26': {'total_funding_projects': 276, 'funding_dict_size': 276}}

exec(code, env_args)
