code = """import json
import pandas as pd
import re

# Load data from files
funding_file = locals()['var_functions.query_db:5']
civic_file = locals()['var_functions.query_db:12']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Create DataFrame for funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract design projects
design_projects = []
for doc in civic_data:
    text = doc['text']
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    constr_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0 and constr_start > design_start:
        design_text = text[design_start:constr_start]
        # Extract project names
        matches = re.findall(r'\n\n([A-Z][^\n]{10,150}?)\n\n\(cid:190\)', design_text)
        for proj in matches:
            clean = proj.strip()
            if clean and len(clean) < 200:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

print('__RESULT__:')
result_obj = {
    'design_projects': design_projects,
    'design_count': len(design_projects),
    'funding_rows': len(funding_df)
}
print(json.dumps(result_obj))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
