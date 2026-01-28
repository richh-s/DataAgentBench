code = """import json

# List all non-private variables
all_vars = {k: v for k, v in locals().items() if not k.startswith('__')}
print('All available variables:')
for k, v in all_vars.items():
    print(f'  {k}: {type(v).__name__} = {str(v)[:100]}')

print('\n\nLooking for specific patterns...')
for k, v in all_vars.items():
    if 'query_db' in str(k) and not k.startswith('_'):
        print(f'Found query_db variable: {k}')
    if 'languages' in str(v).lower() or 'readme' in str(v).lower():
        print(f'Found potential data in {k}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_repos': 3325634, 'repos_with_python': 550905, 'repos_without_python': 2774729, 'repos_without_python_list': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'status': 'setup complete', 'repos_without_python_count': 2774729}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:20': {'languages_loaded': False, 'readme_loaded': False, 'languages_count': 0, 'readme_count': 0}}

exec(code, env_args)
