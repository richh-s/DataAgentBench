code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Let's first identify disaster-related projects from funding data based on naming patterns
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency']

disaster_projects = []
for item in funding_data:
    project_name = item['Project_Name']
    # Check if it's a disaster project based on suffixes or keywords
    if any(keyword in project_name.upper() for keyword in disaster_keywords):
        disaster_projects.append({
            'Project_Name': project_name,
            'Funding_ID': item['Funding_ID'],
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount'])
        })

print('__RESULT__:')
print(json.dumps({
    'total_disaster_projects_in_funding': len(disaster_projects),
    'sample_disaster_projects': disaster_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
