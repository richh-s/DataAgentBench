code = """# Better filtering for Python repositories
import json

# Read the full languages data
lang_data_file = locals()['var_functions.query_db:5']
with open(lang_data_file, 'r') as f:
    languages_data = json.load(f)

# Filter repositories that do NOT use Python (case-insensitive check)
non_python_repos = []
for repo in languages_data:
    repo_name = repo['repo_name']
    language_desc = repo['language_description'].lower()
    # Check if python is NOT in the language description
    if 'python' not in language_desc and 'py' not in language_desc.split():
        non_python_repos.append(repo_name)

# Check some edge cases
python_examples = []
for repo in languages_data[:1000]:
    language_desc = repo['language_description'].lower()
    if 'python' in language_desc:
        python_examples.append(repo)

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(languages_data),
    'non_python_repos_count': len(non_python_repos),
    'python_repos_count': len(languages_data) - len(non_python_repos),
    'sample_python_repos': [repo['repo_name'] for repo in python_examples[:5]]
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'total_repos': 3325634, 'non_python_repos_count': 2774729, 'sample_non_python_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_non_python_repos': 2774729, 'sample_size': 5000, 'sample_repos': ['rajat4493/powershell', 'TingSyuanWang/ReactSimpleBlog', 'nelodvn/restzero', 'garora/number2text', 'SmarkSeven/WaveSwipeRefreshLayout', 'Sitback/helm', 'vailum/ResponsiveImage', 'lzkjyang/LearnPython3.6', 'wtflucas/Luna', 'nvcleemp/square', 'ouonline/myhashmap', 'maroekun/go-setlock', 'osgi-forks/spring-osgi', 'iota-arbitrage/iota-arbitrage.github.com', 'steve1rm/chatbar', 'oldwo/sudoku', 'DerekMarcinyshyn/source', 'AlexSteele/stratos', 'botanicus/dm-is-serialized', 'AlexRib/Suru']}}

exec(code, env_args)
