code = """import json
import pandas as pd

# Load funding data
funding_file_path = locals()['var_functions.query_db:5']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_file_path = locals()['var_functions.query_db:0']
if isinstance(civic_file_path, str) and civic_file_path.endswith('.json'):
    with open(civic_file_path, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = locals()['var_functions.query_db:0']

# Create DataFrames for easier analysis
def safe_to_int(x):
    if pd.isna(x):
        return 0
    try:
        return int(x)
    except (ValueError, TypeError):
        return 0

funding_df = pd.DataFrame(funding_data)
if 'Amount' in funding_df.columns:
    funding_df['Amount'] = funding_df['Amount'].apply(safe_to_int)

print('__RESULT__:')
print(f'Funding records: {len(funding_df)}')
print(f'Funding columns: {list(funding_df.columns)}')

# Show sample funding data
print('\nSample funding data:')
print(funding_df.head(3).to_string())

# Check for disaster-related project names in funding
if 'Project_Name' in funding_df.columns:
    disaster_mask = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Cal OES|disaster', case=False, na=False)
    disaster_projects = funding_df[disaster_mask]
    print(f'\nFound {len(disaster_projects)} disaster-related projects in funding')
    if len(disaster_projects) > 0:
        print('Sample disaster projects:')
        print(disaster_projects[['Project_Name', 'Amount']].head(5).to_string())
else:
    print('Project_Name column not found in funding data')
    print(funding_df.head(2).to_string())

print('\nAnalysis complete')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
