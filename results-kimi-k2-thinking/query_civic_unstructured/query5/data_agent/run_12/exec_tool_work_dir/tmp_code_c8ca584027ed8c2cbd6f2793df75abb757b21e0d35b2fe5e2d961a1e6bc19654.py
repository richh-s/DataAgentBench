code = """import json
import pandas as pd
import re

# Load funding data
f = open(locals()['var_functions.query_db:5'], 'r')
funding_data = json.load(f)
f.close()

# Load civic documents  
f = open(locals()['var_functions.query_db:0'], 'r')
civic_data = json.load(f)
f.close()

# Process funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Get all disaster-related projects
pattern = 'FEMA|Cal\.?OES|CalJPIA|disaster|recovery'
disaster_df = funding_df[funding_df['Project_Name'].str.contains(pattern, case=False, na=False)].copy()

# Extract project names and dates from civic documents
disaster_project_names = []
project_dates = {}

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    for line in lines:
        line = line.strip()
        if not line or len(line) > 200:
            continue
        
        # Look for project headers
        if any(keyword in line.lower() for keyword in ['project', 'improvement', 'repair', 'replacement']) and \
           not line.startswith('(') and not line.startswith('-'):
            current_project = line
        
        # Check for disaster projects with 2022 dates
        if current_project and re.search(pattern, line, re.IGNORECASE) and '2022' in line:
            clean_name = current_project.split('(')[0].strip()
            if clean_name not in disaster_project_names:
                disaster_project_names.append(clean_name)
                project_dates[clean_name] = '2022'

# Match with funding data
total_2022_funding = 0
matched_projects = []

# First, check projects with 2022 in the name
twenty22_in_name = disaster_df[disaster_df['Project_Name'].str.contains('2022', case=False, na=False)]
total_2022_funding += twenty22_in_name['Amount'].sum()
matched_projects.extend(twenty22_in_name['Project_Name'].tolist())

# Then check against extracted project names
for clean_name in disaster_project_names:
    for _, row in disaster_df.iterrows():
        fund_name = row['Project_Name']
        if fund_name in matched_projects:
            continue
            
        fund_clean = fund_name.split('(')[0].strip()
        # Check if names match
        if (clean_name in fund_clean or fund_clean in clean_name):
            total_2022_funding += row['Amount']
            matched_projects.append(fund_name)

result = {
    'total_funding_2022': int(total_2022_funding),
    'matched_projects_count': len(matched_projects),
    'sample_matched': matched_projects[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'total_funding_2022': 0, 'total_disaster_funding': 1410000, 'disaster_2022_projects_count': 0}, 'var_functions.execute_python:22': {'total_funding_2022': 0, 'project_count': 0}}

exec(code, env_args)
