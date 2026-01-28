code = """import json
import pandas as pd
import re

# Load data
f_file = locals()['var_functions.query_db:9']
with open(f_file, 'r') as f:
    funding_data = json.load(f)

c_file = locals()['var_functions.query_db:5']
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Basic info
print('Funding records count:', len(funding_data))
print('Civic documents count:', len(civic_docs))

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Identify disaster projects in funding
keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster']
mask = funding_df['Project_Name'].str.contains('|'.join(keywords), case=False, na=False)
disaster_funding = funding_df[mask]

print('Disaster funding count:', len(disaster_funding))
print('Total disaster funding:', disaster_funding['Amount'].sum())

# Show sample disaster projects
for i, row in disaster_funding.head(3).iterrows():
    print(row['Project_Name'], row['Amount'])

# Basic civic doc check
first_doc = civic_docs[0]
print('First doc filename:', first_doc['filename'])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
