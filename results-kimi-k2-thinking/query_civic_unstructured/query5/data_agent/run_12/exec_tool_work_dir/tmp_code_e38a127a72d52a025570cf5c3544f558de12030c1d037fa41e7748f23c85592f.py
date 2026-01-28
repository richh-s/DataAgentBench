code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:0'], 'r') as f:
    civic_data = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Extract disaster projects from funding
disaster_mask = funding_df['Project_Name'].str.contains('FEMA|Cal\.?OES|CalJPIA', case=False, na=False)
disaster_funding = funding_df[disaster_mask]

# Extract project names from civic documents that mention 2022 and disaster
projects_from_docs = []

for doc in civic_data:
    text = doc.get('text', '')
    if '2022' in text:
        # Look for project sections mentioning 2022
        sections = text.split('\n')
        for section in sections:
            section = section.strip()
            if len(section) < 200 and '2022' in section:
                # Check if it mentions disaster/FEMA
                if re.search(r'FEMA|Cal\.?OES|CalJPIA|disaster|recovery', section, re.IGNORECASE):
                    # Extract project name (first significant line)
                    if not section.startswith(('(', '-', '•')) and len(section) > 5:
                        projects_from_docs.append(section)

# Get unique project names
unique_projects = list(set(projects_from_docs))

# Match with funding by finding projects where the doc project name appears in funding name
total_funding_2022 = 0
for fund_idx, fund_row in disaster_funding.iterrows():
    fund_name = fund_row['Project_Name'].lower()
    fund_amount = fund_row['Amount']
    
    for doc_proj in unique_projects:
        doc_clean = doc_proj.split('(')[0].strip().lower()
        # Check if doc project name is in funding name or vice versa
        if doc_clean in fund_name or fund_name in doc_clean:
            if len(doc_clean) > 10:  # Avoid too short matches
                total_funding_2022 += fund_amount
                break

result = int(total_funding_2022)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'total_funding_2022': 0, 'total_disaster_funding': 1410000, 'disaster_2022_projects_count': 0}, 'var_functions.execute_python:22': {'total_funding_2022': 0, 'project_count': 0}, 'var_functions.execute_python:26': 0}

exec(code, env_args)
