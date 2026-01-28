code = """import json
import pandas as pd

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding DataFrame
df_funding = pd.DataFrame(funding_data)

# Filter for emergency/FEMA projects based on project name keywords
keywords = ['fema', 'emergency', 'warning']
emergency_funding = df_funding[df_funding['Project_Name'].str.contains('|'.join(keywords), case=False)]

# Create results
results = []
for _, row in emergency_funding.iterrows():
    results.append({
        'Project_Name': row['Project_Name'],
        'Funding_Source': row['Funding_Source'],
        'Amount': int(row['Amount']),
        'Status': 'Unknown'
    })

# Sort and output
results = sorted(results, key=lambda x: x['Project_Name'])
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
