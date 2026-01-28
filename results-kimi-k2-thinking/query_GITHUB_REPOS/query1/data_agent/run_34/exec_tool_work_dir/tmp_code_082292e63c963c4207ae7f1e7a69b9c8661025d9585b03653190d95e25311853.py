code = """import json
import pandas as pd
import re
import os

# Print available variables
print('Available variables:')
for key in sorted(locals().keys()):
    if not key.startswith('__'):
        print(f'  {key}')

# Check for variables that might contain our data
languages_data = None
readme_data = None

# Try different approaches to find the data
for var_name in list(locals().keys()):
    var_value = locals()[var_name]
    if isinstance(var_value, str) and ('languages' in var_value or 'readme' in var_value):
        print(f'Found potential path: {var_name} = {var_value}')
        if os.path.exists(var_value):
            print(f'File exists: {var_value}')
            with open(var_value, 'r') as f:
                data = json.load(f)
                if 'language' in str(data[0]) if data else False:
                    languages_data = data
                    print('Loaded languages data')
                elif 'sample_path' in str(data[0]) if data else False:
                    readme_data = data
                    print('Loaded readme data')
        else:
            print(f'File does not exist: {var_value}')

print('_' * 50)
print(f'Languages data loaded: {languages_data is not None}')
print(f'README data loaded: {readme_data is not None}')

print('__RESULT__:')
print(json.dumps({
    'languages_loaded': languages_data is not None,
    'readme_loaded': readme_data is not None,
    'languages_count': len(languages_data) if languages_data else 0,
    'readme_count': len(readme_data) if readme_data else 0
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_repos': 3325634, 'repos_with_python': 550905, 'repos_without_python': 2774729, 'repos_without_python_list': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'status': 'setup complete', 'repos_without_python_count': 2774729}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
