code = """import json

# Read the repos list from the file
with open('file_storage/functions.query_db:10.json', 'r') as f:
    repos_data = json.load(f)

# Extract repo names
apache_shell_repos = set([repo['repo_name'] for repo in repos_data])

print('__RESULT__:')
print(json.dumps({
    'total_apache_shell_repos': len(apache_shell_repos),
    'sample_repos': list(apache_shell_repos)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['commits', 'contents', 'files'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'repo_count': 114972, 'first_5_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:20': [{'total_commits': '17976'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.query_db:24': [{'count': '0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'matching_commits': 1077, 'unique_repos': 2, 'sample_commits': [{'repo': 'apple/swift', 'message_preview': 'Use "if cond is True" instead of discouraged "if cond == True".\n'}, {'repo': 'apple/swift', 'message_preview': 'Sync with https://github.com/practicalswift/swift-compiler-crashes\n\nAdd 5 compiler crashes (+ 1 fixe'}, {'repo': 'apple/swift', 'message_preview': '[gardening] Fix recently introduced typo: "anothor" → "another"\n'}, {'repo': 'apple/swift', 'message_preview': '[gardening] Daily cleanup: typos, header formatting.\n'}, {'repo': 'apple/swift', 'message_preview': 'Sync with https://github.com/practicalswift/swift-compiler-crashes\n\nAdd 2 compiler crashes (+ 1 fixe'}]}, 'var_functions.query_db:30': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'Microsoft/vscode'}]}

exec(code, env_args)
