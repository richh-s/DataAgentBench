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
funding_df = pd.DataFrame(funding_data)
civic_df = pd.DataFrame(civic_docs_data)

# Save intermediate data for inspection
print('__RESULT__:')
print(f'Funding records: {len(funding_df)}')
print(f'Funding columns: {funding_df.columns.tolist()}')
print(f'Citivic documents: {len(civic_df)}')
print(f'Civic columns: {civic_df.columns.tolist()}')

# Show sample data
print('\nSample funding data:')
print(funding_df.head().to_string())

# Check for disaster-related project names in funding
print('\nDisaster-related project names in funding:')
disaster_mask = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Cal OES|disaster', case=False, na=False)
disaster_projects = funding_df[disaster_mask]
print(f'Found {len(disaster_projects)} disaster-related projects in funding')
print(disaster_projects[['Project_Name', 'Amount']].head().to_string())

# Check start years from civic docs (from text field)
# Try to find project start mentions
sample_text = civic_df['text'].iloc[0] if len(civic_df) > 0 else ''
print('\nSample civic doc text preview:')
print(sample_text[:1000])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
