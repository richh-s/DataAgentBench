code = """import json
import re

# Load funding data
funding_data = var_functions.query_db:5

# Extract disaster project names explicitly containing 2022
disaster_2022_projects = []

# Keywords that indicate disaster projects
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'recovery', 'fire', 'culvert', 'bridge', 'drainage', 'storm']

for record in funding_data[:100]:  # Process first 100 to see patterns
    proj_name = record['Project_Name'].lower()
    
    # Check if project has 2022 and disaster keywords
    has_2022 = '2022' in record['Project_Name']
    is_disaster = any(keyword in proj_name for keyword in disaster_keywords)
    
    if has_2022 and is_disaster:
        disaster_2022_projects.append({
            'name': record['Project_Name'],
            'amount': record['Amount'],
            'source': record['Funding_Source']
        })

# Print results
print('__RESULT__:')
print(json.dumps({
    'projects_found': disaster_2022_projects,
    'count': len(disaster_2022_projects)
}, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:10': ['civic_docs'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
