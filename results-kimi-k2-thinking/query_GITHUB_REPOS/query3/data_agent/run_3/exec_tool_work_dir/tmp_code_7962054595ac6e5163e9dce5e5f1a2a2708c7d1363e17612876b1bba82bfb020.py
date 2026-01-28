code = """import json

# Read the shell repositories file - correct variable name format
shell_file = var_functions_query_db_18
if isinstance(shell_file, str) and shell_file.endswith('.json'):
    with open(shell_file, 'r') as f:
        shell_repos = json.load(f)
else:
    shell_repos = shell_file

# Read the apache-2.0 repositories file  
apache_file = var_functions_query_db_20
if isinstance(apache_file, str) and apache_file.endswith('.json'):
    with open(apache_file, 'r') as f:
        apache_repos = json.load(f)
else:
    apache_repos = apache_file

# Extract repo names
shell_repo_names = {repo['repo_name'] for repo in shell_repos}
apache_repo_names = {repo['repo_name'] for repo in apache_repos}

# Find intersection
common_repos = shell_repo_names.intersection(apache_repo_names)

print("__RESULT__:")
print(json.dumps({
    "shell_repos_count": len(shell_repo_names), 
    "apache_repos_count": len(apache_repo_names),
    "common_repos_count": len(common_repos),
    "common_repos_sample": list(common_repos)[:10] if common_repos else []
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:8': [{'repo_name': 'brandonhimpfen/Techie', 'license': 'apache-2.0'}, {'repo_name': 'mychoices/android-percent-support-extend', 'license': 'apache-2.0'}, {'repo_name': 'YY030913/start', 'license': 'apache-2.0'}, {'repo_name': 'WeiLend/WeiLend.github.io', 'license': 'apache-2.0'}, {'repo_name': 'amaj674/Blog-Site-mern-', 'license': 'apache-2.0'}], 'var_functions.execute_python:10': {'shell_count': 5, 'apache_count': 5, 'common_count': 0, 'common_repos': []}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
