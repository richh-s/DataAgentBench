code = """import json

# Get funding data
funding_result = var_functions.query_db_36

# Initialize variables
total_funding = 0
projects_2022 = []

# Parse each funding record
for record in funding_result:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    
    # Check if it's a disaster project (contains FEMA, CalOES, or CalJPIA)
    if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
        # Check if it started in 2022 (contains 2022 in the name)
        if '2022' in project_name:
            total_funding += amount
            projects_2022.append({
                'Project_Name': project_name,
                'Amount': amount
            })

# Result
result = {
    'total_funding': total_funding,
    'num_projects': len(projects_2022),
    'projects': projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
