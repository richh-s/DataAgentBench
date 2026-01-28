code = """import json
import pandas as pd
import re

# Load data
f_file = locals()['var_functions.query_db:9']
c_file = locals()['var_functions.query_db:5']

with open(f_file, 'r') as f:
    funding_data = json.load(f)
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrames
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Find disaster funding
keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster']
is_disaster = funding_df['Project_Name'].str.contains('|'.join(keywords), case=False, na=False)
disaster_funding = funding_df[is_disaster]

# Calculate totals
total_all = disaster_funding['Amount'].sum()

# Check for 2022 in project names
twentytwos = disaster_funding[disaster_funding['Project_Name'].str.contains('2022', case=False, na=False)]
total_2022 = twentytwos['Amount'].sum()

# Output result
result = {'all_disaster': int(total_all), 'twentytwo_disaster': int(total_2022)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:18': {'total_disaster_funding': 1410000, 'disaster_project_count': 27, 'sample_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': 85000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': 14000}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': 81000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': 43000}]}}

exec(code, env_args)
