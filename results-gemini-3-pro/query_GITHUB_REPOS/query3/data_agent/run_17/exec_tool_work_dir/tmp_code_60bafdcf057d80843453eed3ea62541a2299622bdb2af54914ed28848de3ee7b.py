code = """import json

# Load licenses result
with open(locals()['var_function-call-13170069200725513451'], 'r') as f:
    licenses_data = json.load(f)
apache_repos = {item['repo_name'] for item in licenses_data}

# Load languages result
with open(locals()['var_function-call-16045999110330458863'], 'r') as f:
    languages_data = json.load(f)
shell_repos = {item['repo_name'] for item in languages_data}

# Intersection
target_repos = list(apache_repos.intersection(shell_repos))

print("__RESULT__:")
print(json.dumps(target_repos))"""

env_args = {'var_function-call-13170069200725512364': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-13170069200725513451': 'file_storage/function-call-13170069200725513451.json', 'var_function-call-16045999110330458863': 'file_storage/function-call-16045999110330458863.json'}

exec(code, env_args)
