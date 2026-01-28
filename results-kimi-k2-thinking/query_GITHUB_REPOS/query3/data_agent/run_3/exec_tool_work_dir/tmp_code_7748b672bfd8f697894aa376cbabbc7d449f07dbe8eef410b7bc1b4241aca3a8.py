code = """import json

# Get repositories with Shell language
shell_repos = [
    {"repo_name": "juliandunn/rackspacecloud", "language_description": "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."}, 
    {"repo_name": "xMarkusSpringerx/coloranalyzer", "language_description": "This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes)."}, 
    {"repo_name": "michaellihs/gitlab", "language_description": "The codebase includes: Ruby (162,002 bytes), Shell (168 bytes)."}, 
    {"repo_name": "vyorkin/xftp", "language_description": "The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes)."}, 
    {"repo_name": "airatshigapov/drophunter", "language_description": "The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes)."}
]

# Get repositories with Apache-2.0 license
apache_repos = [
    {"repo_name": "brandonhimpfen/Techie", "license": "apache-2.0"}, 
    {"repo_name": "mychoices/android-percent-support-extend", "license": "apache-2.0"}, 
    {"repo_name": "YY030913/start", "license": "apache-2.0"}, 
    {"repo_name": "WeiLend/WeiLend.github.io", "license": "apache-2.0"}, 
    {"repo_name": "amaj674/Blog-Site-mern-", "license": "apache-2.0"}
]

# Find common repositories (this is just a sample - we need to query the actual databases)
shell_repo_names = {repo['repo_name'] for repo in shell_repos}
apache_repo_names = {repo['repo_name'] for repo in apache_repos}
common_repos = shell_repo_names.intersection(apache_repo_names)

print("__RESULT__:")
print(json.dumps({"shell_count": len(shell_repo_names), "apache_count": len(apache_repo_names), "common_count": len(common_repos), "common_repos": list(common_repos)}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:8': [{'repo_name': 'brandonhimpfen/Techie', 'license': 'apache-2.0'}, {'repo_name': 'mychoices/android-percent-support-extend', 'license': 'apache-2.0'}, {'repo_name': 'YY030913/start', 'license': 'apache-2.0'}, {'repo_name': 'WeiLend/WeiLend.github.io', 'license': 'apache-2.0'}, {'repo_name': 'amaj674/Blog-Site-mern-', 'license': 'apache-2.0'}]}

exec(code, env_args)
