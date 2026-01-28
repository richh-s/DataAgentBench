code = """import json
# Check what type of data is stored
commit_storage_key = 'var_functions.query_db:14'
commit_data = locals()[commit_storage_key]
print('__RESULT__:')
print(json.dumps({'type': str(type(commit_data)), 'value': str(commit_data)[:200]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'type': "<class 'str'>", 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.execute_python:12': {'total_repos': 914225, 'non_python_repos': 893211, 'language_counts': {'Shell': 185349, 'CSS': 113124, 'HTML': 94995, 'Makefile': 80811, 'JavaScript': 80595, 'Ruby': 63902, 'C': 34293, 'ApacheConf': 33937, 'Batchfile': 31309, 'Python': 21014}, 'sample_non_python': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'tibastral/web_motion', 'Haegin/stately', 'Scripted/pandago-ruby']}, 'var_functions.query_db:14': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
