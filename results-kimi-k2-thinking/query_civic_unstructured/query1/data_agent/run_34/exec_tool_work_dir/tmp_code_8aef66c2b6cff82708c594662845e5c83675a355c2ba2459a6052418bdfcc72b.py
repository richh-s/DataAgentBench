code = """import json
import pandas as pd

# Load data
f_path = locals()['var_functions.query_db:5']
c_path = locals()['var_functions.query_db:12']

with open(f_path, 'r') as f:
    funding_data = json.load(f)

with open(c_path, 'r') as f:
    civic_data = json.load(f)

# Process funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design projects - look for lines before the (cid:190) markers
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    i = 0
    while i < len(lines) - 1:
        line_current = lines[i].strip()
        line_next = lines[i + 1].strip()
        if line_current and '(cid:190)' in line_next and not line_current.startswith('Capital') and not line_current.startswith('(') and len(line_current) > 10:
            design_projects.append(line_current)
        i += 1

design_projects = list(set(design_projects))

# Count capital design projects with funding > 50000
count = 0
high_fund = funding_df[funding_df['Amount'] > 50000]

for idx, row in high_fund.iterrows():
    fund_name = row['Project_Name']
    if fund_name in design_projects:
        count += 1
    else:
        base_name = fund_name.split(' (')[0]
        for proj in design_projects:
            if base_name in proj:
                count += 1
                break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
