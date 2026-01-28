code = """import json
import re

# Load the README data and non-Python repos list
with open('/tmp/tmpk_kr1t6d/results.json', 'r') as f:
    readme_data = json.load(f)

with open('/tmp/tmp0u_njy_s/results.json', 'r') as f:
    non_python_repos_data = json.load(f)

# Create a set of non-Python repo names for fast lookup
non_python_repos = set(item['repo_name'] for item in non_python_repos_data)

print('Total README files sampled: ' + str(len(readme_data)))
print('Total non-Python repos in our sample: ' + str(len(non_python_repos)))

# Check which README files are from non-Python repos
non_python_readmes = []
python_readmes = []

for item in readme_data:
    repo_name = item['sample_repo_name']
    content = item['content']
    
    if repo_name in non_python_repos:
        non_python_readmes.append(item)
    else:
        python_readmes.append(item)

print('READMEs from non-Python repos: ' + str(len(non_python_readmes)))
print('READMEs from Python repos: ' + str(len(python_readmes)))

# Function to check for copyright information
def has_copyright(content):
    if not content:
        return False
    # Look for copyright patterns (case-insensitive)
    copyright_patterns = [
        r'copyright\s+[©\(c\)]?\s*\d{4}',
        r'©\s*\d{4}',
        r'\(c\)\s*\d{4}',
        r'copyright\s+by',
        r'copyright\s+holder',
        r'copyright\s+notice'
    ]
    
    content_lower = content.lower()
    for pattern in copyright_patterns:
        if re.search(pattern, content_lower):
            return True
    return False

# Analyze copyright in non-Python repos
non_python_with_copyright = 0
non_python_total = len(non_python_readmes)

for item in non_python_readmes:
    if has_copyright(item['content']):
        non_python_with_copyright += 1

# Analyze copyright in Python repos for comparison
python_with_copyright = 0
python_total = len(python_readmes)

for item in python_readmes:
    if has_copyright(item['content']):
        python_with_copyright += 1

print()
print('Non-Python repos:')
print('  Total sampled: ' + str(non_python_total))
print('  With copyright: ' + str(non_python_with_copyright))
if non_python_total > 0:
    proportion = non_python_with_copyright/non_python_total
    print('  Proportion: ' + '{:.2%}'.format(proportion))
else:
    print('  Proportion: N/A')

print()
print('Python repos:')
print('  Total sampled: ' + str(python_total))
print('  With copyright: ' + str(python_with_copyright))
if python_total > 0:
    proportion = python_with_copyright/python_total
    print('  Proportion: ' + '{:.2%}'.format(proportion))
else:
    print('  Proportion: N/A')

result = {
    'non_python_total': non_python_total,
    'non_python_with_copyright': non_python_with_copyright,
    'non_python_proportion': non_python_with_copyright/non_python_total if non_python_total > 0 else None,
    'python_total': python_total,
    'python_with_copyright': python_with_copyright,
    'python_proportion': python_with_copyright/python_total if python_total > 0 else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'total_repos': '3325634'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [{'python_repos': '550905'}], 'var_functions.query_db:28': [{'python_repos': '550905'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total_repos': '3325634'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [{'total_repos': '3325634'}], 'var_functions.query_db:40': [{'python_repos': '550905'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
