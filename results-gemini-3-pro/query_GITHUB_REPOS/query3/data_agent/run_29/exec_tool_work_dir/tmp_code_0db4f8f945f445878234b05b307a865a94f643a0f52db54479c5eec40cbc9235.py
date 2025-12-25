code = """import json

repo_file = locals()['var_function-call-10815371365636378488']
commit_file = locals()['var_function-call-3608308409946616951']

with open(repo_file, 'r') as f:
    repos = json.load(f)
    # Extract repo_name
    valid_repos = set(r['repo_name'] for r in repos)

with open(commit_file, 'r') as f:
    commits = json.load(f)

count = 0
for c in commits:
    repo = c.get('repo_name')
    msg = c.get('message')
    
    if repo in valid_repos:
        if msg:
            # Check message start condition (case-insensitive)
            msg_lower = msg.lower()
            # "does not begin with 'merge', 'update', or 'test'"
            if not msg_lower.startswith(('merge', 'update', 'test')):
                count += 1

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-2939043559931441822': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-2939043559931441277': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-10815371365636378488': 'file_storage/function-call-10815371365636378488.json', 'var_function-call-2702238739522881891': 114972, 'var_function-call-15136695239173122027': [{'count_star()': '17976'}], 'var_function-call-3608308409946616951': 'file_storage/function-call-3608308409946616951.json'}

exec(code, env_args)
