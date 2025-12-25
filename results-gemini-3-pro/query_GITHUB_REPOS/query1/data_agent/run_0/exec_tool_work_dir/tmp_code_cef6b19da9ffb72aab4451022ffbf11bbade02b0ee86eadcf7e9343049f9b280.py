code = """import json

non_python_repos_file = locals()['var_function-call-6293145715309141115']
with open(non_python_repos_file, 'r') as f:
    non_python_repos_list = json.load(f)

non_python_repos = set(item['repo_name'] for item in non_python_repos_list)

readmes_file = locals()['var_function-call-9987823125710353733']
with open(readmes_file, 'r') as f:
    readmes_list = json.load(f)

count_total = 0
count_has_copyright = 0
found_repos = []

for item in readmes_list:
    repo = item.get('sample_repo_name')
    if repo not in non_python_repos:
        continue
    
    count_total += 1
    content = item.get('content', '')
    if content is None:
        content = ''
    content_lower = content.lower()
    
    # Check indicators
    # Note: (c) matches simply. © is unicode.
    if 'copyright' in content_lower or '(c)' in content_lower or '\u00a9' in content_lower:
        count_has_copyright += 1
        found_repos.append(repo)

proportion = count_has_copyright / count_total if count_total > 0 else 0

print(f"Total relevant repos: {count_total}")
print(f"Has copyright: {count_has_copyright}")
print(f"Proportion: {proportion}")

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-633006030965842401': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-6293145715309141115': 'file_storage/function-call-6293145715309141115.json', 'var_function-call-9987823125710353733': 'file_storage/function-call-9987823125710353733.json', 'var_function-call-13118727994381467009': 0.1485148514851485, 'var_function-call-8885486065617528124': 'Done', 'var_function-call-12464819408794518007': {'count_non_python': 2774729, 'count_readmes': 128, 'sample_non_python': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter'], 'sample_readmes': ['ninja-ide/ninja-ide', 'cwilso/midi-synth', 'ha/doozerd', 'devsoulwolf/ChatMessageView', 'google/traceur-compiler']}}

exec(code, env_args)
