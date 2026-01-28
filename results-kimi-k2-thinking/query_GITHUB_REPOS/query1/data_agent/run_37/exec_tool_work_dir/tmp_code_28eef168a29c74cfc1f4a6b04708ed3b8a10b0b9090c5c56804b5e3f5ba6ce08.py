code = """# Read the sample repos data
import json

sample_file = locals()['var_functions.execute_python:18']
with open(sample_file, 'r') as f:
    sample_data = json.load(f)

sample_repos = sample_data['sample_repos']
print('__RESULT__:')
print(json.dumps({
    'repos_to_query': sample_repos,
    'count': len(sample_repos)
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'total_repos': 3325634, 'non_python_repos_count': 2774729, 'sample_non_python_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_non_python_repos': 2774729, 'sample_size': 5000, 'sample_repos': ['rajat4493/powershell', 'TingSyuanWang/ReactSimpleBlog', 'nelodvn/restzero', 'garora/number2text', 'SmarkSeven/WaveSwipeRefreshLayout', 'Sitback/helm', 'vailum/ResponsiveImage', 'lzkjyang/LearnPython3.6', 'wtflucas/Luna', 'nvcleemp/square', 'ouonline/myhashmap', 'maroekun/go-setlock', 'osgi-forks/spring-osgi', 'iota-arbitrage/iota-arbitrage.github.com', 'steve1rm/chatbar', 'oldwo/sudoku', 'DerekMarcinyshyn/source', 'AlexSteele/stratos', 'botanicus/dm-is-serialized', 'AlexRib/Suru']}, 'var_functions.execute_python:16': {'total_repos': 3325634, 'non_python_repos_count': 2774729, 'python_repos_count': 550905, 'sample_python_repos': []}, 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json'}

exec(code, env_args)
