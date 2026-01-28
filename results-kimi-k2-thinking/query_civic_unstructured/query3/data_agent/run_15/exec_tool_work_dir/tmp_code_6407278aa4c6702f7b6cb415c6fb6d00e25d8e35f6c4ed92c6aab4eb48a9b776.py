code = """import pandas as pd
import json
import re

# Load funding data from the file
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data from the file
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Identify FEMA/emergency projects from funding data
fema_emergency_funding = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    if 'emergency' in project_name or 'fema' in project_name:
        fema_emergency_funding.append(record)

print(f"\nFEMA/Emergency projects from funding data: {len(fema_emergency_funding)}")
for proj in fema_emergency_funding:
    print(f"- {proj['Project_Name']} | {proj['Funding_Source']} | {proj['Amount']}")

# Let's also look at funding sources that might be emergency-related
emergency_sources = [
    'Federal Assistance', 'FEMA', 'Disaster Relief', 'Emergency', 'CalOES',
    'CalJPIA', 'Government Grant', 'State Development Grant'
]

fema_related_by_source = []
for record in funding_data:
    funding_source = record['Funding_Source'].lower()
    project_name = record['Project_Name'].lower()
    if ('fema' in funding_source or 'federal' in funding_source or 'emergency' in funding_source or
        'disaster' in funding_source or 'caloes' in funding_source or 'caljpia' in funding_source or
        'fema' in project_name or 'emergency' in project_name or '(fema' in project_name or
        'disaster' in project_name or 'caloes' in project_name or 'caljpia' in project_name):
        fema_related_by_source.append(record)

print(f"\nAll potentially FEMA/emergency related by source or name: {len(fema_related_by_source)}")
for proj in fema_related_by_source[:15]:
    print(f"- {proj['Project_Name']} | {proj['Funding_Source']} | {proj['Amount']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
