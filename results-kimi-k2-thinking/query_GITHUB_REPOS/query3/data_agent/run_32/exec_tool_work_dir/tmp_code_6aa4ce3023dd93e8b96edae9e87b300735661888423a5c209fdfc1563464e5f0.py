code = """import json

# Load the repository list from metadata database
file_path = locals()['var_functions.query_db:6']
with open(file_path, 'r') as f:
    metadata_repos = json.load(f)

metadata_repo_names = [repo['repo_name'] for repo in metadata_repos]

# Load some commit data from artifacts database
commit_file_path = locals()['var_functions.query_db:12']
with open(commit_file_path, 'r') as f:
    commits = json.load(f)

commit_repo_names = list(set([commit['repo_name'] for commit in commits]))

# Find overlap between metadata repos and repos in commits
overlap = set(metadata_repo_names) & set(commit_repo_names)

print(f"__RESULT__:")
print(json.dumps({
    "metadata_repo_count": len(metadata_repo_names),
    "commit_repo_count": len(commit_repo_names),
    "overlap_count": len(overlap),
    "sample_overlap": list(overlap)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'repo_count': 114972, 'sample_for_query': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c"}, 'var_functions.query_db:18': [{'commit_count': '0'}], 'var_functions.query_db:20': [{'total_commits': '0'}], 'var_functions.query_db:22': [{'repo_name': 'facebook/react'}, {'repo_name': 'apple/swift'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'tensorflow/tensorflow'}], 'var_functions.query_db:24': [{'repo_count': '6'}]}

exec(code, env_args)
