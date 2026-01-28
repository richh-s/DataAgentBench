code = """import json
import pandas as pd
import re
import os

# Check available files in the data directory
print('Checking data directory...')
if os.path.exists('data'):
    files = os.listdir('data')
    print(f'Files in data/: {files}')
else:
    print('data directory not found')

# Load funding data
print('\nTrying to load funding data...')
funding_files = [f for f in files if 'funding' in f.lower()]
if funding_files:
    with open(f'data/{funding_files[0]}', 'r') as f:
        funding_data = json.load(f)
    print(f'Loaded {len(funding_data)} funding records')
else:
    print('No funding file found')

# Convert to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print('\nFirst few records:')
print(funding_df.head())

# Identify disaster-related projects
pattern = r'\(FEMA Project\)|\(CalOES Project\)|\(CalJPIA Project\)|\(FEMA/CalOES Project\)'
disaster_mask = funding_df['Project_Name'].str.contains(pattern, case=False, na=False)
disaster_projects = funding_df[disaster_mask]

print(f'\nFound {len(disaster_projects)} disaster projects')
print('Sample disaster projects:')
print(disaster_projects[['Project_Name', 'Amount']].head(10))

# Filter for projects with 2022 in the name
projects_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Load civic documents to find additional 2022 disaster projects
print('\nLoading civic documents...')
civic_files = [f for f in files if 'civic' in f.lower() or '694' in f]
if civic_files:
    with open(f'data/{civic_files[0]}', 'r') as f:
        civic_docs = json.load(f)
    print(f'Loaded {len(civic_docs)} civic documents')
    
    # Look for 2022 disaster projects in documents
    additional_projects = []
    for doc in civic_docs:
        text = doc['text']
        if '2022' in text:
            # Check for disaster indicators
            if any(term in text.lower() for term in ['fema', 'caloes', 'caljpia']):
                # Look for project names in disaster_projects
                for _, proj in disaster_projects.iterrows():
                    proj_name_clean = proj['Project_Name'].split('(')[0].strip()  # Remove suffixes
                    if proj_name_clean.lower() in text.lower() and proj_name_clean not in [p.split('(')[0].strip() for p in projects_2022['Project_Name']]:
                        additional_projects.append(proj)
    
    if additional_projects:
        additional_df = pd.DataFrame(additional_projects)
        projects_2022 = pd.concat([projects_2022, additional_df]).drop_duplicates()
else:
    print('No civic docs file found')

# Calculate total funding
total_funding = projects_2022['Amount'].sum()
num_projects = len(projects_2022)

print(f'\nTotal disaster projects starting in 2022: {num_projects}')
print(f'Total funding: ${total_funding:,}')

# Prepare result
result = {
    'total_funding': int(total_funding),
    'num_projects': int(num_projects),
    'projects': projects_2022[['Project_Name', 'Amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
