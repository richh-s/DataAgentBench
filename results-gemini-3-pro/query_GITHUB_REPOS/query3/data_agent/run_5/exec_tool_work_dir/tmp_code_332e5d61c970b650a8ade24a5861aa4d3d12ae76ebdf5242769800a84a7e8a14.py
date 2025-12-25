code = """import json

# Load the valid repos list (large file)
with open(locals()['var_function-call-17368171006005567624'], 'r') as f:
    valid_repos_list = json.load(f)

# Create a set for fast lookup
valid_repos = set(item['repo_name'] for item in valid_repos_list)

# Load the commit counts (small list from memory)
commit_counts = locals()['var_function-call-17787656969448352453']

# Filter and sum
total_commits = 0
matching_repos = []
for entry in commit_counts:
    repo = entry['repo_name']
    count = int(entry['cnt'])
    if repo in valid_repos:
        total_commits += count
        matching_repos.append(repo)

print(f"Matching repos found in commits table: {matching_repos}")
print(f"Total valid commits: {total_commits}")

print("__RESULT__:")
print(json.dumps(total_commits))"""

env_args = {'var_function-call-15296750945497281807': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-15296750945497281482': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-17368171006005567624': 'file_storage/function-call-17368171006005567624.json', 'var_function-call-4096428950375466377': {'count': 114972, 'preview': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_function-call-17787656969448352453': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'facebook/react', 'cnt': '104'}], 'var_function-call-16249038577847206316': [{'total_commits': '17976', 'total_repos': '6'}]}

exec(code, env_args)
