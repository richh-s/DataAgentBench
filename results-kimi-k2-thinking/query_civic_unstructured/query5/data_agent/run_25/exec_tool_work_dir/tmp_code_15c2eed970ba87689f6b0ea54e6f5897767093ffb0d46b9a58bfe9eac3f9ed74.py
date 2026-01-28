code = """import json
import re

# Load funding data
funding_data = locals()['var_functions.query_db:2']

# If funding_data is a string (file path), read the file
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Load civic docs
civic_docs = locals()['var_functions.query_db:5']
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

# Let's first identify disaster-related projects from funding data based on naming patterns
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency']

disaster_projects_funding = []
for item in funding_data:
    project_name = item['Project_Name']
    # Check if it's a disaster project based on suffixes or keywords
    if any(keyword in project_name.upper() for keyword in disaster_keywords):
        disaster_projects_funding.append({
            'Project_Name': project_name,
            'Funding_ID': item['Funding_ID'],
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount'])
        })

print('__RESULT__:')
print(json.dumps({
    'total_disaster_projects_in_funding': len(disaster_projects_funding),
    'sample_disaster_projects': disaster_projects_funding[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
