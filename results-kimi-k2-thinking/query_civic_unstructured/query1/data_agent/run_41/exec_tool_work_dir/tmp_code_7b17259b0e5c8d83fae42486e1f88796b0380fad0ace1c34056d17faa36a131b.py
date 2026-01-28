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
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    funding_lookup[name.split(' (')[0]] = amount

design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos < 0:
        continue
    
    design_section = text[design_pos + 100:]
    cons_pos = design_section.find('Capital Improvement Projects (Construction)')
    if cons_pos > 0:
        design_section = design_section[:cons_pos]
    
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•'):
            continue
        if 'Updates:' in line or 'Schedule:' in line or 'Page' in line:
            continue
        
        project_name = line.rstrip('.,:;')
        if project_name in funding_lookup and funding_lookup[project_name] > 50000:
            design_projects.add(project_name)

print('__RESULT__:')
print(str(len(design_projects)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:82': [{'project_count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json'}

exec(code, env_args)
