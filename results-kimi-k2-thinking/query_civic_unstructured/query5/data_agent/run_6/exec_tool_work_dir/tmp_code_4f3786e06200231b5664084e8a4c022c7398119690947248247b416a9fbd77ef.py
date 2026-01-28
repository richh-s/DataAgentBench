code = """import json
import pandas as pd
import re

# Load the data
with open('/tmp/tmp2v7m_6l3.json', 'r') as f:
    civic_docs = json.load(f)

with open('/tmp/tmpf4d6q2f3.json', 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Find all disaster projects from funding data
# Disaster projects have FEMA, CalOES, or CalJPIA in their names
disaster_mask = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)
disaster_funding = funding_df[disaster_mask].copy()
disaster_funding['Amount'] = disaster_funding['Amount'].astype(int)

# Find projects with 2022 in their names
projects_2022 = disaster_funding[disaster_funding['Project_Name'].str.contains('2022', case=False, na=False)]

# Process civic documents to find 2022 disaster projects
for doc in civic_docs:
    text = doc['text']
    if '2022' in text and any(indicator in text.lower() for indicator in ['fema', 'caloes', 'disaster']):
        lines = text.split('\n')
        for line in lines:
            if '2022' in line and (('FEMA' in line) or ('CalOES' in line) or ('disaster' in line.lower())):
                # Look for related project names
                for proj_name in disaster_funding['Project_Name']:
                    if any(keyword.lower() in line.lower() for keyword in proj_name.split() if len(keyword) > 5):
                        projects_2022 = pd.concat([projects_2022, disaster_funding[disaster_funding['Project_Name'] == proj_name]])

# Remove duplicates and calculate total
projects_2022_unique = projects_2022.drop_duplicates()
total_funding = projects_2022_unique['Amount'].sum()
num_projects = len(projects_2022_unique)

print('Total funding for 2022 disaster projects:', total_funding)
print('Number of projects:', num_projects)

# Prepare result
result = {
    'total_funding': int(total_funding),
    'num_projects': int(num_projects),
    'projects': projects_2022_unique[['Project_Name', 'Amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
