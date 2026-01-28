code = """import json

# Access funding data from previous query
# The variable should be available as var_functions.query_db_36 or similar

# Since I can't access the variables directly, let me make a new query to get the funding data

# For now, let me search through what we know:
# - Funding database has project names and amounts
# - Disaster projects have FEMA, CalOES, or CalJPIA in their names
# - 2022 projects have '2022' in their names or descriptions

# I'll manually check the funding data by re-querying
import pandas as pd

# Use a simpler approach - directly filter the data
print('Starting analysis...')

# Initialize result
result = {'total_funding': 0, 'num_projects': 0, 'projects': []}

# The funding data is stored in var_functions.query_db_36
# Let me try to access it
try:
    funding_data = var_functions.query_db_36
    print(f'Loaded {len(funding_data)} funding records')
    
    # Process records
    for record in funding_data:
        project_name = record.get('Project_Name', '')
        if any(keyword in project_name for keyword in ['FEMA', 'CalOES', 'CalJPIA']) and '2022' in project_name:
            amount = int(record.get('Amount', 0))
            result['total_funding'] += amount
            result['num_projects'] += 1
            result['projects'].append({
                'Project_Name': project_name,
                'Amount': amount
            })
    
    print('__RESULT__:')
    print(json.dumps(result))
    
except Exception as e:
    print(f'Error: {e}')
    # Try alternative variable name
    try:
        funding_data = var_functions_query_db_36
        print(f'Loaded {len(funding_data)} funding records (alt)')
        
        for record in funding_data:
            project_name = record.get('Project_Name', '')
            if any(keyword in project_name for keyword in ['FEMA', 'CalOES', 'CalJPIA']) and '2022' in project_name:
                amount = int(record.get('Amount', 0))
                result['total_funding'] += amount
                result['num_projects'] += 1
                result['projects'].append({
                    'Project_Name': project_name,
                    'Amount': amount
                })
        
        print('__RESULT__:')
        print(json.dumps(result))
        
    except:
        # If I can't access the variables, query the database again
        print('Could not access stored data')
        result = {'error': 'Data access failed'}
        print('__RESULT__:')
        print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
