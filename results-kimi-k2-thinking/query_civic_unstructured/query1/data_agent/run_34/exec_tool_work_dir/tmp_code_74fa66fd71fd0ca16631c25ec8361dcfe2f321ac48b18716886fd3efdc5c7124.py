code = """import json, pandas as pd, re

funding_path = str(locals()['var_functions.query_db:5'])
civic_path = str(locals()['var_functions.query_db:12'])

with open(funding_path) as f:
    funding_data = json.load(f)
with open(civic_path) as f:
    civic_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

design_projects = []

for doc in civic_data:
    text = doc['text']
    d_start = text.find('Capital Improvement Projects (Design)')
    c_start = text.find('Capital Improvement Projects (Construction)')
    
    if d_start >= 0 and c_start > d_start:
        section = text[d_start:c_start]
        lines = section.split('\n')
        for i in range(len(lines)-1):
            curr = lines[i].strip()
            nxt = lines[i+1].strip() if i+1 < len(lines) else ''
            if curr and nxt.startswith('(cid:190)') and not curr.startswith('(') and len(curr) > 10:
                design_projects.append(curr)

design_projects = list(set(design_projects))

count = 0
capital_matched = []
high_fund = funding_df[funding_df['Amount'] > 50000]

for _, row in high_fund.iterrows():
    fund_name = row['Project_Name']
    if fund_name in design_projects:
        count += 1
        capital_matched.append(fund_name)
    else:
        base_name = fund_name.split(' (')[0]
        for proj in design_projects:
            if base_name in proj or proj in fund_name:
                count += 1
                capital_matched.append(fund_name)
                break

# Filter out disaster/FEMA projects
capital_only = [p for p in capital_matched if 'fema' not in p.lower() and 'disaster' not in p.lower()]

print('__RESULT__:')
print(json.dumps({'count': len(capital_only), 'projects': capital_only}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
