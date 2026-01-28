code = """import json

# Get funding data from storage
funding_data = var_functions_query_db_36

# Filter for disaster projects with 2022 in the name
disaster_2022_projects = []
total_funding = 0

for record in funding_data:
    project_name = record.get('Project_Name', '')
    # Check if it's a disaster project (contains FEMA, CalOES, or CalJPIA) and has 2022
    if any(keyword in project_name for keyword in ['FEMA', 'CalOES', 'CalJPIA']) and '2022' in project_name:
        amount = int(record.get('Amount', 0))
        total_funding += amount
        disaster_2022_projects.append({
            'Project_Name': project_name,
            'Amount': amount
        })

# Create result
result = {
    'total_funding': total_funding,
    'num_projects': len(disaster_2022_projects),
    'projects': disaster_2022_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
