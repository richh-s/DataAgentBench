code = """import json
import re

# Load the readme data from the file
with open(locals()['var_functions.query_db:8'], 'r') as f:
    readme_data = json.load(f)

# Load non-python repos from previous result
non_python_repos = locals()['var_functions.execute_python:12']['non_python_repos']
non_python_repo_names = locals()['var_functions.execute_python:12']['sample_non_python']

# Create a set for faster lookup
non_python_set = set(non_python_repo_names)

# Filter README data for non-Python repositories
non_python_readmes = [r for r in readme_data if r['sample_repo_name'] in non_python_set]

# Check for copyright information
readmes_with_copyright = []
for readme in non_python_readmes:
    content = readme.get('content', '')
    if content and content != 'None':
        # Look for copyright patterns
        if re.search(r'copyright', content, re.IGNORECASE):
            readmes_with_copyright.append(readme['sample_repo_name'])

result = {
    'total_readmes_checked': len(non_python_readmes),
    'readmes_with_copyright': len(readmes_with_copyright),
    'sample_copyright_repos': readmes_with_copyright[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_repos': 3325634, 'non_python_repos': 2774729, 'sample_non_python': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}}

exec(code, env_args)
