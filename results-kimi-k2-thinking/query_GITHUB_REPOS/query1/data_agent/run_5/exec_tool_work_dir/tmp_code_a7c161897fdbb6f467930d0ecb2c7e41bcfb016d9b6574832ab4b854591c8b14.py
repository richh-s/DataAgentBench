code = """import json
import random
import re

# Get non-Python repo list
non_python_file = locals()['var_functions.query_db:16']
with open(non_python_file, 'r') as f:
    all_non_python_repos = json.load(f)

# Take a sizeable but manageable sample
sample_size = 5000
sampled_repos = random.sample(all_non_python_repos, sample_size)
repo_names = [repo['repo_name'] for repo in sampled_repos]

# Prepare query for DuckDB (which supports large IN clauses better)
# We'll fetch all READMEs and then filter in Python
query = f"""
SELECT sample_repo_name, content 
FROM contents 
WHERE (sample_path LIKE '%README.md' OR sample_path = 'README.md')
  AND sample_repo_name IN (
    SELECT repo_name FROM (
      VALUES {','.join([f"('{name}')" for name in repo_names])}
    ) AS t(repo_name)
  )
"""

print('__RESULT__:')
print(json.dumps({
    'total_non_python_repos': len(all_non_python_repos),
    'sample_size': sample_size,
    'query_preview': query[:200] + '...'
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'count': 2774729, 'example_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'count': '2774729'}], 'var_functions.execute_python:32': {'total_non_python_repos': 2774729, 'sample_size': 1000, 'sample_repos': ['ilesan-ypg/htty', 't0mz06/JVCPrevisualizer', 'CrearAyT/maquina-de-samba', 'sofish/wechat.js', 'bitHero/boostrap', 'RReverser/pure-cjs', 'jeenuine/test-repo', 'sdgdsffdsfff/rn-china-region-picker', 'iionly/users_online', 'maly/ez65265']}, 'var_functions.execute_python:36': 'file_storage/functions.execute_python:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:48': {'total_non_python_repos': 2774729, 'sample_size': 1000, 'sample_repos': ['jackreacher1994/sav', 'umaxfun/serve-static', 'harryLittleroom/tromba', 'ZeleEG/diesel2016', 'binarylogic/authlogic_openid', 'tdfischer/rippit', 'isc-carlos-gomez/scala-trial', 'HarvinWang/learning-swing', 'iromu/eReg-parser', 'ann1019/android-delicious-bookmarks']}}

exec(code, env_args)
