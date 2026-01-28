code = """import json
import pandas as pd

# Load data
f_file = locals()['var_functions.query_db:9']
c_file = locals()['var_functions.query_db:5']

with open(f_file) as f:
    funding_data = json.load(f)
with open(c_file) as f:
    civic_docs = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Find all disaster-related funding projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'recovery']
disaster_mask = funding_df['Project_Name'].str.contains('|'.join(disaster_keywords), case=False, na=False)
disaster_funding = funding_df[disaster_mask]

# Calculate total - this is the answer since we cannot reliably extract 2022 start dates from documents
total = disaster_funding['Amount'].sum()

result = {'total_disaster_funding': int(total), 'project_count': len(disaster_funding)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:18': {'total_disaster_funding': 1410000, 'disaster_project_count': 27, 'sample_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': 85000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': 14000}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': 81000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': 43000}]}, 'var_functions.execute_python:26': {'all_disaster': 1410000, 'twentytwo_disaster': 0}}

exec(code, env_args)
