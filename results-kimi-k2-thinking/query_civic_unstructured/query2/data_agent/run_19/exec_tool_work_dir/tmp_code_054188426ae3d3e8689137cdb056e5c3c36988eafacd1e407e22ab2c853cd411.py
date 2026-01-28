code = """import json

# Load funding data
f_path = locals()['var_functions.query_db:0']
with open(f_path, 'r') as file:
    funding_records = json.load(file)

# Load civic documents
c_path = locals()['var_functions.query_db:14']
with open(c_path, 'r') as file:
    civic_docs = json.load(file)

# Find park projects completed in 2022
park_funding_total = 0
projects_list = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    
    # Check for specific completed park projects mentioned
    if 'Bluffs Park Shade Structure' in text and 'November 2022' in text:
        for rec in funding_records:
            if rec.get('Project_Name') == 'Bluffs Park Shade Structure':
                park_funding_total += int(rec.get('Amount', 0))
                projects_list.append('Bluffs Park Shade Structure')
    
    if 'Broad Beach Road Water Quality Repair' in text and 'November 2022' in text:
        for rec in funding_records:
            if 'Broad Beach Road Water Quality Repair' in rec.get('Project_Name', ''):
                park_funding_total += int(rec.get('Amount', 0))
                projects_list.append(rec.get('Project_Name'))
    
    if 'Point Dume Walkway Repairs' in text and 'November 2022' in text:
        for rec in funding_records:
            if rec.get('Project_Name') == 'Point Dume Walkway Repairs':
                park_funding_total += int(rec.get('Amount', 0))
                projects_list.append('Point Dume Walkway Repairs')

# Remove duplicates and recalculate
total = 0
unique_projects = list(set(projects_list))
for proj in unique_projects:
    for rec in funding_records:
        if rec.get('Project_Name') == proj:
            total += int(rec.get('Amount', 0))

result = {
    'total_funding': total,
    'projects': len(unique_projects),
    'project_names': sorted(unique_projects)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'total_park_funding_2022': 105000, 'projects': 1, 'names': ['Bluffs Park Shade Structure']}, 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
