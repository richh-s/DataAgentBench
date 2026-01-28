code = """import pandas as pd
import json
import re

# Load funding data from the file
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data from the file
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Identify FEMA/emergency projects from funding data
fema_emergency_funding = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    if 'emergency' in project_name or 'fema' in project_name:
        fema_emergency_funding.append(record)

print('\nFEMA/Emergency projects from funding data:', len(fema_emergency_funding))
for proj in fema_emergency_funding:
    print('Project:', proj['Project_Name'], '| Source:', proj['Funding_Source'], '| Amount:', proj['Amount'])

# Also look for projects with FEMA/emergency-related keywords in their names
all_emergency_projects = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    project_info = record
    
    # Check if project name contains emergency-related keywords
    emergency_keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning', 'siren']
    is_emergency = any(keyword in project_name for keyword in emergency_keywords)
    
    if is_emergency:
        all_emergency_projects.append(project_info)

print('\nAll emergency-related projects from funding data:', len(all_emergency_projects))
for proj in all_emergency_projects:
    print('Project:', proj['Project_Name'], '| Source:', proj['Funding_Source'], '| Amount:', proj['Amount'])

# Also check if funding sources suggest emergency/disaster nature
disaster_funding_sources = []
for record in funding_data:
    funding_source = record['Funding_Source'].lower()
    project_name = record['Project_Name'].lower()
    
    # Sources that typically fund disaster/emergency projects
    if ('federal' in funding_source or 'government' in funding_source or 
        'caloes' in project_name or 'caljpia' in project_name or 'fema' in project_name or
        'disaster' in project_name):
        disaster_funding_sources.append(record)

print('\nPotential disaster/emergency projects based on funding source:', len(disaster_funding_sources))
for proj in disaster_funding_sources[:10]:
    print('Project:', proj['Project_Name'], '| Source:', proj['Funding_Source'], '| Amount:', proj['Amount'])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
