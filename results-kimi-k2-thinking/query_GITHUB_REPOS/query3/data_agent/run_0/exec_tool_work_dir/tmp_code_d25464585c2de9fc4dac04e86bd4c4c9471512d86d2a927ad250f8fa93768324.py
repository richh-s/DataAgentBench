code = """import json

# Read the file with Apache-2.0 repositories
file_path = "file_storage/functions.query_db:5.json"

with open(file_path, 'r') as f:
    apache_repos = json.load(f)

# Create a lookup of repo_name to language_description for Apache-2.0 repos
apache_repo_lookup = {repo['repo_name']: repo['language_description'] for repo in apache_repos}

# The repos that actually have commit data based on previous queries
repos_with_commit_data = [
    'torvalds/linux',
    'apple/swift', 
    'twbs/bootstrap',
    'Microsoft/vscode',
    'facebook/react',
    'tensorflow/tensorflow'
]

# Check which of these repos are in our Apache-2.0 + Shell list
shell_repos_in_commit_data = []
for repo in repos_with_commit_data:
    if repo in apache_repo_lookup:
        lang_desc = apache_repo_lookup[repo]
        if 'shell' in lang_desc.lower():
            shell_repos_in_commit_data.append(repo)

print('__RESULT__:')
print(json.dumps({
    'shell_repos_count': len(shell_repos_in_commit_data),
    'shell_repos_in_commit_data': shell_repos_in_commit_data
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'type': "<class 'str'>", 'is_string': True, 'preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:18': {'total_apache_repos': 495134, 'shell_repos_count': 114972, 'first_few_shell_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor', 'ivschukin/learning-azure', 'arrawatia/cp-docker-images', 'wolfitem/docker', 'sdgdsffdsfff/ModSecurity', 'frapposelli/govmomi', 'Grimmjowjack/google-services', 'chuangWu/butterknife', 'louwrentius/eztables', 'riddlesio/hack-man-engine', 'DavitTevanyan/word2vec']}, 'var_functions.query_db:20': [{'total_commits': '0'}], 'var_functions.query_db:22': [], 'var_functions.query_db:24': [{'count_star()': '17976'}], 'var_functions.query_db:26': [{'repo_name': 'torvalds/linux', 'commit_count': '14318'}, {'repo_name': 'apple/swift', 'commit_count': '1034'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'repo_name': 'torvalds/linux'}]}

exec(code, env_args)
