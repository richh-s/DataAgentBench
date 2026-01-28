code = """import json
import pandas as pd

# Read the repository list from the file
result_file = locals()['var_functions.query_db:18']
with open(result_file, 'r') as f:
    repo_data = json.load(f)

# Extract repo names
repo_names = [item['repo_name'] for item in repo_data]
print(f"Total repositories: {len(repo_names)}")

# Process in batches to avoid query size limits
batch_size = 1000
batches = [repo_names[i:i + batch_size] for i in range(0, len(repo_names), batch_size)]
print(f"Number of batches: {len(batches)}")
print(f"First batch size: {len(batches[0]) if batches else 0}")
print(f"Last batch size: {len(batches[-1]) if batches else 0}")

# Store batch info for next step
result = {
    'total_repo_count': len(repo_names),
    'batch_count': len(batches),
    'batch_size': batch_size
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'commit_count': '15016'}], 'var_functions.query_db:7': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'repo_count': 114972, 'first_five': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook'], 'last_five': ['dleehr/common-workflow-language', 'uc-cdis/cwl', 'veact/scala-ssh', 'm4kspl/scala-ssh', 'stdweird/aquilon']}, 'var_functions.query_db:14': [{'count': '659616'}], 'var_functions.query_db:15': [{'count': '495134'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
