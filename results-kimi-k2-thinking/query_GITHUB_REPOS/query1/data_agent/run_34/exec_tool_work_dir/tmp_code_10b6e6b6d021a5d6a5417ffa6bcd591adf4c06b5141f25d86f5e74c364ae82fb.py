code = """import json
import os

# Find JSON files
json_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            path = os.path.join(root, file)
            json_files.append(path)

print('Found JSON files:')
for f in json_files:
    print(f)

# Identify files
languages_file = None
readme_file = None

for f in json_files:
    with open(f, 'r') as file:
        try:
            data = json.load(file)
            if data and isinstance(data, list) and len(data) > 0:
                first_item = data[0]
                if isinstance(first_item, dict):
                    if 'language_description' in first_item:
                        languages_file = f
                        print('Languages file found:', f)
                    elif 'sample_path' in first_item and 'content' in first_item:
                        readme_file = f
                        print('README file found:', f)
        except:
            pass

result = {
    'languages_file': languages_file,
    'readme_file': readme_file,
    'languages_found': languages_file is not None,
    'readme_found': readme_file is not None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_repos': 3325634, 'repos_with_python': 550905, 'repos_without_python': 2774729, 'repos_without_python_list': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'status': 'setup complete', 'repos_without_python_count': 2774729}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:20': {'languages_loaded': False, 'readme_loaded': False, 'languages_count': 0, 'readme_count': 0}}

exec(code, env_args)
