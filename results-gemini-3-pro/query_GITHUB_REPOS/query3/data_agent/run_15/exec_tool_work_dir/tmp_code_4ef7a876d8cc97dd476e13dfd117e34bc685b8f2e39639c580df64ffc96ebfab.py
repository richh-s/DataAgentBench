code = """import json

# Load metadata repos (Shell + Apache-2.0)
with open(locals()['var_function-call-1339008272902058649'], 'r') as f:
    metadata_repos_list = json.load(f)

# Create a set for faster lookup
metadata_repos = set(item['repo_name'] for item in metadata_repos_list)

# Load commit counts from artifacts_database
# var_function-call-5670889441163704325 is a list of dicts, not a file path
commit_counts = locals()['var_function-call-5670889441163704325']

total_commits = 0
matching_repos = []

for entry in commit_counts:
    repo = entry['repo_name']
    # The count in result might be a string or int, convert to int
    count = int(entry['count'])
    
    if repo in metadata_repos:
        total_commits += count
        matching_repos.append(repo)

print("__RESULT__:")
print(json.dumps({"total_commits": total_commits, "matching_repos": matching_repos}))"""

env_args = {'var_function-call-14559876417495664485': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-14559876417495666220': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-1339008272902058649': 'file_storage/function-call-1339008272902058649.json', 'var_function-call-14508020189717351832': {'count': 114972, 'first_10': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_function-call-5670889441163704325': [{'repo_name': 'facebook/react', 'count': '104'}, {'repo_name': 'tensorflow/tensorflow', 'count': '114'}, {'repo_name': 'twbs/bootstrap', 'count': '251'}, {'repo_name': 'Microsoft/vscode', 'count': '171'}, {'repo_name': 'apple/swift', 'count': '963'}, {'repo_name': 'torvalds/linux', 'count': '13413'}], 'var_function-call-17218747592043829641': 6, 'var_function-call-10262722290280000029': [{'repo_name': 'facebook/react'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}]}

exec(code, env_args)
