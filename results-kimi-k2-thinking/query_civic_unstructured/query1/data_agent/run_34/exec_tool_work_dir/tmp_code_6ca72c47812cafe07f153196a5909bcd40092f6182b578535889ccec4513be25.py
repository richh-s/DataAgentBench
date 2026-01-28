code = """import json, pandas, re

f_path = locals()['var_functions.query_db:5']
c_path = locals()['var_functions.query_db:12']

with open(f_path) as f:
    funding = json.load(f)
with open(c_path) as f:
    civic = json.load(f)

# Process funding data
funding_df = pandas.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design project names from civic documents
all_design = []

for doc in civic:
    text = doc.get('text', '')
    d_start = text.find('Capital Improvement Projects (Design)')
    c_start = text.find('Capital Improvement Projects (Construction)')
    
    if d_start >= 0 and c_start > d_start:
        section = text[d_start:c_start]
        lines = section.split('\n')
        for i in range(len(lines) - 1):
            curr = lines[i].strip()
            nxt = lines[i+1].strip()
            if curr and nxt.startswith('(cid:190)') and not curr.startswith('Capital'):
                if not curr.startswith('(') and len(curr) > 10:
                    all_design.append(curr)

# Remove duplicates
unique_design = list(set(all_design))

# Count capital projects with design status and > 50000 funding
count = 0
capital_projects = []

high_fund = funding_df[funding_df['Amount'] > 50000]

for _, row in high_fund.iterrows():
    fund_name = row['Project_Name']
    base_name = fund_name.split(' (')[0]
    
    # Match by base name since some projects have suffixes
    for design_name in unique_design:
        if base_name == design_name or base_name in design_name or design_name in fund_name:
            # Filter for capital projects (not disaster recovery)
            if 'fema' not in fund_name.lower() and 'disaster' not in fund_name.lower():
                count += 1
                capital_projects.append(fund_name)
                break

result = {'count': count, 'projects': capital_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
