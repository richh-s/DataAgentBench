code = """import json
import pandas as pd

# Check available variables
print('Available variables:', [k for k in locals().keys() if not k.startswith('_')])

# Read the full result from the first query
var_name = 'var_functions.query_db:0'
if var_name in locals():
    result_path = locals()[var_name]
    print('Reading languages data from:', result_path)
    
    with open(result_path, 'r') as f:
        languages_data = json.load(f)
    
    df_languages = pd.DataFrame(languages_data)
    df_languages['has_python'] = df_languages['language_description'].str.contains('Python', case=False, na=False)
    
    repos_without_python = df_languages[~df_languages['has_python']]['repo_name'].tolist()
    print(f'Total repos without Python: {len(repos_without_python)}')
    
    # Sample for demonstration
    sample_repos = repos_without_python[:100]
    print('Sample repos for query:', sample_repos[:5])
else:
    print('Languages variable not found')

# Read README data
readme_var = 'var_functions.query_db:6'
if readme_var in locals():
    readme_path = locals()[readme_var]
    print('Reading README data from:', readme_path)
    
    with open(readme_path, 'r') as f:
        readme_data = json.load(f)
    
    df_readmes = pd.DataFrame(readme_data)
    print(f'Total READMEs retrieved: {len(df_readmes)}')
    print('Columns:', df_readmes.columns.tolist())
    print('Sample paths:', df_readmes['sample_path'].head(10).tolist())
else:
    print('README variable not found')

print('__RESULT__:')
print(json.dumps({'status': 'setup complete', 'repos_without_python_count': len(repos_without_python) if "repos_without_python" in locals() else 0}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_repos': 3325634, 'repos_with_python': 550905, 'repos_without_python': 2774729, 'repos_without_python_list': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
