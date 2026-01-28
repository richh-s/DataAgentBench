code = """import json
import pandas as pd
import re

# Access the data using the storage keys
civic_docs_key = 'var_functions.query_db:16'
funding_key = 'var_functions.query_db:17'

# Read the data from the files
civic_docs_file = locals()[civic_docs_key]
funding_file = locals()[funding_key]

with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding DataFrame
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs_data),
    'funding_count': len(funding_data),
    'sample_civic_doc_filename': civic_docs_data[0]['filename'] if civic_docs_data else None,
    'total_funding_available': int(df_funding['Amount'].sum())
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
