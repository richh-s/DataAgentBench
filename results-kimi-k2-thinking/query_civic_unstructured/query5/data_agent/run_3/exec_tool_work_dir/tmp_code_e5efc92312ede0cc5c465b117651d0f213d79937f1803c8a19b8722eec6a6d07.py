code = """import json
import pandas as pd
import re

# Load the data
civic_docs_data = locals()['var_functions.query_db:0']
funding_data = locals()['var_functions.query_db:2']

# Load from files if they're strings
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)
        
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert to DataFrames
df_civic = pd.DataFrame(civic_docs_data)
df_funding = pd.DataFrame(funding_data)

print('Documents loaded:', len(df_civic))
print('Funding records loaded:', len(df_funding))

# Find disaster-related projects in funding data
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Fire']
funding_disaster = df_funding[df_funding['Project_Name'].str.contains('|'.join(disaster_keywords), case=False)].copy()

print('Disaster-related funding records:', len(funding_disaster))

# Get unique disaster project names
disaster_project_names = funding_disaster['Project_Name'].unique()
print('Unique disaster projects:', len(disaster_project_names))

# Search for these projects in civic documents with 2022 mentions
projects_with_2022 = set()

for _, doc in df_civic.iterrows():
    text = doc['text']
    for proj_name in disaster_project_names:
        if proj_name in text:
            # Check if 2022 appears in the document
            if '2022' in text:
                projects_with_2022.add(proj_name)

print('Disaster projects mentioning 2022:', len(projects_with_2022))

# Calculate total funding
filtered_funding = funding_disaster[funding_disaster['Project_Name'].isin(projects_with_2022)]
total_funding = filtered_funding['Amount'].astype(int).sum()

print('Total funding for disaster projects that mention 2022: $', total_funding)

result = {
    'total_funding': int(total_funding),
    'project_count': len(projects_with_2022),
    'funding_records': len(filtered_funding)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'civic_docs_shape': [5, 3], 'funding_shape': [500, 4], 'civic_docs_columns': ['_id', 'filename', 'text'], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
