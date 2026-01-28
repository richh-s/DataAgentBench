code = """import json
import re

funding_file = locals()['var_functions.query_db:84']
civic_file = locals()['var_functions.query_db:54']

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_data = json.load(f)

funding_lookup = {}
for item in funding_data:
    proj_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[proj_name] = amount
    base_name = proj_name.split(' (')[0]
    funding_lookup[base_name] = amount

found = set()

for doc in civic_data:
    text = doc.get('text', '')
    ds = text.find('Capital Improvement Projects (Design)')
    if ds < 0:
        continue
    
    design_text = text[ds + 100:]
    cs = design_text.find('Capital Improvement Projects (Construction)')
    if cs > 0:
        design_text = design_text[:cs]
    
    for line in design_text.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•'):
            continue
        if 'Updates:' in line or 'Schedule:' in line or 'Page' in line:
            continue
        
        clean_name = line.rstrip('.,:;')
        if clean_name in funding_lookup:
            if funding_lookup[clean_name] > 50000:
                found.add(clean_name)

print('__RESULT__:')
print(str(len(found)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:82': [{'project_count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json'}

exec(code, env_args)
