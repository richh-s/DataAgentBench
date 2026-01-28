code = """import json

# Get funding data from storage
funding_data = locals()['var_functions.query_db:72']

# Identify the park projects that were completed in 2022 based on the civic documents:
# 1. Bluffs Park Shade Structure - completed November 2022
# 2. Broad Beach Road Water Quality Repair - completed November 2022
# 3. Point Dume Walkway Repairs - completed November 2022

# Map project names to their funding amounts
project_funding = {
    'Bluffs Park Shade Structure': 0,
    'Broad Beach Road Water Quality Repair': 0,
    'Point Dume Walkway Repairs': 0
}

# Find matching projects in funding data
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    
    if 'Bluffs Park Shade Structure' in project_name:
        project_funding['Bluffs Park Shade Structure'] = amount
    elif project_name == 'Broad Beach Road Water Quality Repair':
        project_funding['Broad Beach Road Water Quality Repair'] = amount
    elif 'Point Dume Walkway Repairs' in project_name:
        project_funding['Point Dume Walkway Repairs'] = amount

# Calculate total
total_funding = sum(project_funding.values())

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'breakdown': project_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs'], 'var_functions.execute_python:52': {'debug': 'done'}, 'var_functions.execute_python:54': {'status': 'debug'}, 'var_functions.execute_python:58': {'status': 'debug_info_recorded'}, 'var_functions.execute_python:62': {'debug': 'path_identification'}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.execute_python:70': {'status': 'type_check_complete'}, 'var_functions.query_db:72': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}, {'Project_Name': 'Point Dume Walkway Repairs', 'Amount': '59000'}]}

exec(code, env_args)
