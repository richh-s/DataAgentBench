code = """import json
import pandas as pd
import re

# Load funding data
funding_file = locals()['var_functions.query_db:5']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
civic_file = locals()['var_functions.query_db:12']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Process funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract design projects from civic documents
design_projects = []
for doc in civic_data:
    text = doc.get('text', '')
    # Find design section boundaries
    design_start = text.find('Capital Improvement Projects (Design)')
    constr_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0 and constr_start > design_start:
        design_section = text[design_start:constr_start]
        # Find project names (appear before (cid:190) markers)
        lines = design_section.split('\n')
        for i in range(len(lines)-1):
            line = lines[i].strip()
            if (line and 
                not line.startswith('(') and 
                len(line) > 10 and 
                lines[i+1].strip() == '(cid:190)'):
                # Clean project name
                clean_name = re.sub(r'[^A-Za-z0-9 &\-.,()]', '', line)
                if clean_name:
                    design_projects.append(clean_name)

# Remove duplicates
design_projects = list(set(design_projects))

# Filter funding for design projects with amount > 50000
design_funding = funding_df[funding_df['Project_Name'].isin(design_projects) & (funding_df['Amount'] > 50000)]

count = len(design_funding)
print('__RESULT__:')
print(json.dumps({
    'count': count,
    'matching_projects': design_funding[['Project_Name', 'Amount']].to_dict(orient='records')
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
