code = """import json
import re

# Load the readme data from the file
with open(locals()['var_functions.query_db:8'], 'r') as f:
    readme_data = json.load(f)

# Calculate proportion based on available data
# We need to intersect readme repos with non-python repos
readme_repos = set([r['sample_repo_name'] for r in readme_data if r.get('content') != 'None'])

# Get a sample to check for copyright patterns
sample_size = min(100, len(readme_data))
sample_readmes = readme_data[:sample_size]

readmes_with_copyright = 0
total_with_content = 0

copyright_repos = []

for readme in sample_readmes:
    content = readme.get('content', '')
    if content and content != 'None':
        total_with_content += 1
        # Look for copyright patterns
        if re.search(r'copyright', content, re.IGNORECASE):
            readmes_with_copyright += 1
            copyright_repos.append(readme['sample_repo_name'])

result = {
    'total_readmes_sampled': len(sample_readmes),
    'readmes_with_content': total_with_content,
    'readmes_with_copyright': readmes_with_copyright,
    'copyright_percent': (readmes_with_copyright / total_with_content * 100) if total_with_content > 0 else 0,
    'sample_copyright_repos': copyright_repos
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_repos': 3325634, 'non_python_repos': 2774729, 'sample_non_python': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.execute_python:14': {'total_readmes_checked': 0, 'readmes_with_copyright': 0, 'sample_copyright_repos': []}}

exec(code, env_args)
