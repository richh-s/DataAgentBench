code = """import json
import pandas as pd
import re

# Load funding data
f_path = locals()['var_functions.query_db:5']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents 
c_path = locals()['var_functions.query_db:12']
with open(c_path, 'r') as f:
    civic_data = json.load(f)

# Process funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract all project names from design section
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    d_start = text.find('Capital Improvement Projects (Design)')
    c_start = text.find('Capital Improvement Projects (Construction)')
    
    if d_start >= 0 and c_start > d_start:
        section = text[d_start:c_start]
        lines = section.split('\n')
        for i in range(len(lines)-1):
            curr = lines[i].strip()
            nxt = lines[i+1].strip()
            if curr and '(cid:190)' in nxt and not curr.startswith('Capital') and not curr.startswith('(') and len(curr) > 10:
                design_projects.append(curr)

# Remove duplicates
design_projects = list(set(design_projects))

# Count matches > 50000
count = 0
matches = []

high_fund = funding_df[funding_df['Amount'] > 50000]

for _, row in high_fund.iterrows():
    fund_name = row['Project_Name']
    base_fund = fund_name.split(' (')[0]
    
    for design_proj in design_projects:
        if fund_name == design_proj or base_fund in design_proj or design_proj in fund_name:
            count += 1
            matches.append(fund_name)
            break

result = {'count': count, 'projects': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
