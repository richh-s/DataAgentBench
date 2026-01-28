code = """import json
import pandas as pd
import re

# Load data
funding_file = locals()['var_functions.query_db:9']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Number of funding records: %d' % len(funding_data))
print('Number of civic documents: %d' % len(civic_docs))

# Create DataFrame for funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print('\nFirst 3 funding records:')
for i, rec in enumerate(funding_data[:3]):
    print('  %s' % str(rec))

print('\nFunding DataFrame head:')
print(funding_df.head())

# Identify disaster-related projects
keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster']
pattern = '|'.join(keywords)
disaster_funding = funding_df[funding_df['Project_Name'].str.contains(pattern, case=False, na=False)]

print('\nDisaster funding count: %d' % len(disaster_funding))
print(disaster_funding[['Project_Name', 'Amount']].head())

# Check civic documents
doc = civic_docs[0]
print('\nFirst doc filename: %s' % doc['filename'])
print('First 200 chars: %s' % doc['text'][:200])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
