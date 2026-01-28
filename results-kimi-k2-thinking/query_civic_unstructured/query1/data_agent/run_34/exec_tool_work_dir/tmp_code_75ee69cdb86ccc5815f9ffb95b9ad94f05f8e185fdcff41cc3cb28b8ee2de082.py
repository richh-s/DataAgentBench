code = """import json
import re

funding_path = locals()['var_functions.query_db:5']
civic_path = locals()['var_functions.query_db:12']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

design_projects = []
for doc in civic_data:
    text = doc['text']
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start > 0 and construction_start > design_start:
        design_section = text[design_start:construction_start]
        lines = design_section.split('\n')
        for i, line in enumerate(lines):
            clean_line = line.strip()
            if (clean_line and 
                not clean_line.startswith('(') and 
                not clean_line.startswith('Capital Improvement') and
                len(clean_line) > 10 and 
                len(clean_line) < 150 and
                i < len(lines) - 1 and 
                lines[i+1].strip() == '(cid:190)'):
                design_projects.append(clean_line)

design_projects = list(set(design_projects))

print('__RESULT__:')
print(json.dumps({
    'design_projects': design_projects,
    'count': len(design_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
