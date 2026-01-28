code = """import json

# Get the file path from storage
funding_file_path = locals()['var_functions.query_db:5']

# Open and load the funding data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'recovery', 'fire']
disaster_2022_projects = []

for record in funding_data:
    proj_name = record['Project_Name']
    amount = record['Amount']
    
    # Check for 2022 in project name
    has_2022 = '2022' in proj_name
    
    # Check if it's a disaster project
    is_disaster = any(keyword in proj_name.lower() for keyword in disaster_keywords)
    
    if has_2022 and is_disaster:
        disaster_2022_projects.append({
            'project': proj_name,
            'amount': int(amount),
            'source': record['Funding_Source']
        })

total = sum(p['amount'] for p in disaster_2022_projects)

result = {
    'total_funding': total,
    'project_count': len(disaster_2022_projects),
    'projects': disaster_2022_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:10': ['civic_docs'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
