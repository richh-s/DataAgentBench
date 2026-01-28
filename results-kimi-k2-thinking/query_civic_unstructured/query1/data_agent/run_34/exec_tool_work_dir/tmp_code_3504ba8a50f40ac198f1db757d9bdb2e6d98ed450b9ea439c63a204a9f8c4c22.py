code = """import json
import pandas as pd

# Load data
funding_file = locals()['var_functions.query_db:5']
civic_file = locals()['var_functions.query_db:12']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

design_projects = []
for doc in civic_data:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            clean = line.strip()
            if (clean and 
                not clean.startswith('(') and 
                len(clean) > 10 and 
                i < len(lines)-1 and 
                lines[i+1].strip() == '(cid:190)'):
                design_projects.append(clean)

design_projects = list(set(design_projects))

print('__RESULT__:')
print(json.dumps({
    'design_projects': design_projects,
    'count': len(design_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
