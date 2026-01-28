code = """import json
import pandas as pd

# The result is stored in var_functions.query_db:0 - we need to handle the special character
# Let's check what variables are available
available_vars = [k for k in locals().keys() if 'query_db' in str(k)]
print('Available variables with query_db:', available_vars)

# Try to access the variable directly
var_name = 'var_functions.query_db:0'
if var_name in locals():
    result_path = locals()[var_name]
    print('Found path:', result_path)
    
    # Read the full result from the query
    with open(result_path, 'r') as f:
        languages_data = json.load(f)
    
    # Convert to DataFrame
    df_languages = pd.DataFrame(languages_data)
    
    # Check for Python in language descriptions
    df_languages['has_python'] = df_languages['language_description'].str.contains('Python', case=False, na=False)
    
    # Show some examples
    print("Total repositories:", len(df_languages))
    print("Repos with Python:", df_languages['has_python'].sum())
    print("Repos without Python:", (~df_languages['has_python']).sum())
    
    # Get list of repos without Python
    repos_without_python = df_languages[~df_languages['has_python']]['repo_name'].tolist()
    print("Sample repos without Python:", repos_without_python[:5])
    
    output = {
        'total_repos': len(df_languages),
        'repos_with_python': int(df_languages['has_python'].sum()),
        'repos_without_python': int((~df_languages['has_python']).sum()),
        'repos_without_python_list': repos_without_python[:10]
    }
    
    print('__RESULT__:')
    print(json.dumps(output))
else:
    print('Variable not found directly')
    # Let's try to find the actual variable
    for k in locals().keys():
        if 'query_db' in str(k):
            print('Key:', k, 'Value:', locals()[k])
    
    print('__RESULT__:')
    print(json.dumps({'error': 'Variable not found'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
