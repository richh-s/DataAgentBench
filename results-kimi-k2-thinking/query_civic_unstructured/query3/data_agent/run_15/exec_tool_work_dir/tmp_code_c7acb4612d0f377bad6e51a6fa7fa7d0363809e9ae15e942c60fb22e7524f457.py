code = """import pandas as pd
import json

# Load funding data
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# First, let's identify all FEMA/emergency related projects from funding data
fema_emergency_projects = []
emergency_keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning', 'siren']

for record in funding_data:
    project_name_lower = record['Project_Name'].lower()
    funding_source_lower = record['Funding_Source'].lower()
    
    is_emergency = any(keyword in project_name_lower for keyword in emergency_keywords) or \
                   'federal' in funding_source_lower or \
                   'caloes' in project_name_lower or \
                   'caljpia' in project_name_lower
    
    if is_emergency:
        record_copy = record.copy()
        record_copy['is_emergency'] = True
        fema_emergency_projects.append(record_copy)

print('\nFEMA/Emergency related projects in funding data:', len(fema_emergency_projects))

# Convert to DataFrame for easier analysis
fema_df = pd.DataFrame(fema_emergency_projects)

# Print results
result_list = []
for _, row in fema_df.iterrows():
    project_info = {
        'Project_Name': row['Project_Name'],
        'Funding_Source': row['Funding_Source'],
        'Amount': int(row['Amount']),
        'Status': 'Unknown'  # Will try to extract from civic docs
    }
    result_list.append(project_info)
    print('Project:', row['Project_Name'])
    print('Funding_Source:', row['Funding_Source'])
    print('Amount:', row['Amount'])
    print('---')

print('\nTotal projects found:', len(result_list))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
