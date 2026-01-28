code = """import json
import re

civic_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file, 'r') as cf:
    civic_docs = json.load(cf)

with open(funding_file, 'r') as ff:
    funding_data = json.load(ff)

projects_list = []
transaction_set = set()

for fund_entry in funding_data:
    proj_name = fund_entry['Project_Name']
    if 'fema' in proj_name.lower():
        project_dict = {
            'Project_Name': proj_name,
            'Funding_Source': fund_entry['Funding_Source'],
            'Amount': int(fund_entry['Amount']),
            'Status': 'Status not in civic documents'
        }
        projects_list.append(project_dict)
        transaction_set.add(proj_name.lower())

for document in civic_docs:
    content_lines = document['text'].split('\n')
    for content_line in content_lines:
        lowered = content_line.lower()
        if 'emergency' in lowered or 'fema' in lowered:
            stripped = content_line.strip()
            if len(stripped) > 8 and not stripped.startswith('('):
                lowered_stripped = stripped.lower()
                if lowered_stripped not in transaction_set:
                    matched_funding = None
                    for entry in funding_data:
                        entry_name = entry['Project_Name']
                        if stripped in entry_name or entry_name in stripped:
                            matched_funding = entry
                            break
                    
                    if matched_funding:
                        funding_amount = int(matched_funding['Amount'])
                        funding_source = matched_funding['Funding_Source']
                    else:
                        funding_amount = 0
                        funding_source = 'No match found'
                    
                    result_project = {
                        'Project_Name': stripped,
                        'Funding_Source': funding_source,
                        'Amount': funding_amount,
                        'Status': 'Referenced in civic documents'
                    }
                    projects_list.append(result_project)
                    transaction_set.add(lowered_stripped)

# Order by funding amount
projects_list.sort(key=lambda record: record['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(projects_list))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
