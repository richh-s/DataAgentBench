code = """import json
import re

# Read the full result from the file
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    language_data = json.load(f)

# Function to check if a repository uses Python
def uses_python(language_desc):
    """Check if the language description mentions Python"""
    if not language_desc:
        return False
    # Look for Python in the language description
    return 'python' in language_desc.lower()

# Count statistics
total_repos = len(language_data)
python_repos = sum(1 for item in language_data if uses_python(item['language_description']))
non_python_repos = total_repos - python_repos

print("__RESULT__:")
print(json.dumps({
    "total_repositories": total_repos,
    "python_repositories": python_repos,
    "non_python_repositories": non_python_repos,
    "sample_python_repos": [item for item in language_data if uses_python(item['language_description'])][:5],
    "sample_non_python_repos": [item for item in language_data if not uses_python(item['language_description'])][:5]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
