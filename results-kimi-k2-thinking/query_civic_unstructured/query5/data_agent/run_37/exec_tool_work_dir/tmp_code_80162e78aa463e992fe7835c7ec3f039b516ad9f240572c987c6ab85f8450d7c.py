code = """import json
import pandas as pd
import re

# Load funding data
funding_file = locals()['var_functions.query_db:9']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Number of funding records:', len(funding_data))
print('Number of civic documents:', len(civic_docs))

# Convert funding to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print('\nFirst 3 funding records:')
for i, rec in enumerate(funding_data[:3]):
    print('  ', i+1, rec)

print('\nFunding DataFrame head:')
print(funding_df.head())

# Look for disaster-related keywords in project names
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster']
disaster_mask = funding_df['Project_Name'].str.contains('|'.join(disaster_keywords), case=False, na=False)
disaster_funding = funding_df[disaster_mask]

print('\nDisaster-related funding records found:', len(disaster_funding))
print(disaster_funding[['Project_Name', 'Amount']].head())

# Now look at civic documents to find project details
print('\nFirst civic document filename:', civic_docs[0]['filename'])
print('Text excerpt:', civic_docs[0]['text'][:200])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
