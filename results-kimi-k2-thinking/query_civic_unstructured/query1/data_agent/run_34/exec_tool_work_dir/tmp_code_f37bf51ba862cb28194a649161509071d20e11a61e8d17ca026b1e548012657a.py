code = """import json, pandas as pd, re

# Load data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_functions.query_db:12'], 'r') as f:
    civic_data = json.load(f)

# Process funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design projects
design_projects = []
for doc in civic_data:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        # Split into lines
        lines = text.splitlines()
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if (line_clean and 
                i < len(lines)-1 and 
                '(cid:190)' in lines[i+1] and
                not line_clean.startswith('(') and
                len(line_clean) > 10):
                design_projects.append(line_clean)

design_projects = list(set(design_projects))

# Filter funding > 50000 for design projects
matched_projects = []
for idx, row in funding_df.iterrows():
    if row['Amount'] > 50000 and row['Project_Name'] in design_projects:
        matched_projects.append(row['Project_Name'])

print('__RESULT__:')
print(json.dumps({
    'count': len(matched_projects),
    'projects': matched_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
