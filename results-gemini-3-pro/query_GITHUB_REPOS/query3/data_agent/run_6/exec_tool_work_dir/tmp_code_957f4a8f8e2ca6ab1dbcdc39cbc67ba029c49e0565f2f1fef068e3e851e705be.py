code = """import json
import re

# Load Repos
with open(locals()['var_function-call-10504877886590857824'], 'r') as f:
    repo_data = json.load(f)

# Load Commits
with open(locals()['var_function-call-17402463240102202561'], 'r') as f:
    commit_data = json.load(f)

print("Total repos loaded:", len(repo_data))
print("Total commits loaded:", len(commit_data))

valid_repos = set()
shell_descriptions = []
for r in repo_data:
    desc = r.get('language_description', '')
    if re.search(r'\bShell\b', desc): # Remove IGNORECASE to see strict match first
        valid_repos.add(r['repo_name'])
        if len(shell_descriptions) < 5:
            shell_descriptions.append(desc)

print("Valid Shell repos:", len(valid_repos))
if len(valid_repos) > 0:
    print("Sample valid repo:", list(valid_repos)[0])

if len(commit_data) > 0:
    print("Sample commit repo:", commit_data[0]['repo_name'])

# Check for intersection without filtering
repo_names_commits = set(c['repo_name'] for c in commit_data)
repo_names_metadata = set(r['repo_name'] for r in repo_data)
intersection = repo_names_commits.intersection(repo_names_metadata)
print("Intersection of ALL repos (before Shell filter):", len(intersection))
if len(intersection) > 0:
    print("Sample intersection:", list(intersection)[0])
else:
    print("No intersection between metadata and artifacts repos!")

# Check license filter in previous query
# I queried: WHERE t2.license = 'apache-2.0' AND t1.language_description LIKE '%Shell%'
# So `repo_data` should already be Apache-2.0 and contain "Shell" substring.
# Why did I get 0? 
# Maybe "Shell" in substring matches "PowerShell" but \bShell\b doesn't, and ONLY PowerShell repos exist?
# Let's see the descriptions.
print("__RESULT__:")
print(json.dumps(shell_descriptions))"""

env_args = {'var_function-call-13088382630648990338': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-13088382630648991249': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-10504877886590857824': 'file_storage/function-call-10504877886590857824.json', 'var_function-call-15916807321362983497': 114972, 'var_function-call-18020883217836689134': [{'count_star()': '17976'}], 'var_function-call-17402463240102202561': 'file_storage/function-call-17402463240102202561.json', 'var_function-call-8639217337742392574': 0}

exec(code, env_args)
