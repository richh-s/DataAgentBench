code = """import json

# Load non-python repos
with open(locals()['var_function-call-11513096632638864993'], 'r') as f:
    non_python_repos_list = json.load(f)

non_python_repos = set(item['repo_name'] for item in non_python_repos_list)

# Load readmes
with open(locals()['var_function-call-6372203990509813929'], 'r') as f:
    readmes = json.load(f)

total_readmes = 0
copyright_readmes = 0

for readme in readmes:
    repo = readme.get('sample_repo_name')
    if repo in non_python_repos:
        total_readmes += 1
        content = readme.get('content', '')
        if content and 'copyright' in content.lower():
            copyright_readmes += 1

if total_readmes == 0:
    proportion = 0
else:
    proportion = copyright_readmes / total_readmes

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-9966727217511841873': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-11513096632638864993': 'file_storage/function-call-11513096632638864993.json', 'var_function-call-6372203990509813929': 'file_storage/function-call-6372203990509813929.json'}

exec(code, env_args)
