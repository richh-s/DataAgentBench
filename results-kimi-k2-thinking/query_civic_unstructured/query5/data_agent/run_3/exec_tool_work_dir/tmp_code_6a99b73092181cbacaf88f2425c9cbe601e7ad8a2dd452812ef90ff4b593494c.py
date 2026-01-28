code = """import json
import pandas as pd
import re

# Load data
civic_docs = locals()['var_functions.query_db:0']
funding = locals()['var_functions.query_db:2']

# Convert file paths if needed
if isinstance(civic_docs, str):
    with open(civic_docs) as f:
        civic_docs = json.load(f)
if isinstance(funding, str):
    with open(funding) as f:
        funding = json.load(f)

# DataFrames
df_civic = pd.DataFrame(civic_docs)
df_funding = pd.DataFrame(funding)

# Find disaster projects in funding
disaster_mask = df_funding['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Fire', case=False)
funding_disaster = df_funding[disaster_mask].copy()
funding_disaster['Amount'] = funding_disaster['Amount'].astype(int)

print('Disaster projects in funding:', len(funding_disaster))

# Get disaster project names
disaster_names = funding_disaster['Project_Name'].unique()
print('Unique disaster names:', len(disaster_names))

# Find projects with 2022 mentions
projects_2022 = set()

for _, doc in df_civic.iterrows():
    text = doc['text']
    if '2022' not in text:
        continue
    for name in disaster_names:
        if name in text:
            projects_2022.add(name)

print('Disaster projects with 2022:', len(projects_2022))

# Calculate funding
total_funding = funding_disaster[funding_disaster['Project_Name'].isin(projects_2022)]['Amount'].sum()

result = {
    'total_funding': int(total_funding),
    'project_count': len(projects_2022)
}

print('Final result:', result)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'civic_docs_shape': [5, 3], 'funding_shape': [500, 4], 'civic_docs_columns': ['_id', 'filename', 'text'], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:18': {'total_funding': 1367000, 'project_count': 26, 'funding_records': 26}}

exec(code, env_args)
