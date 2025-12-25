code = """import json

# Load non-python repos
non_python_repos_file = locals()['var_function-call-6293145715309141115']
with open(non_python_repos_file, 'r') as f:
    non_python_repos_list = json.load(f)

non_python_repos = set(item['repo_name'] for item in non_python_repos_list)

# Load README contents
readmes_file = locals()['var_function-call-9987823125710353733']
with open(readmes_file, 'r') as f:
    readmes_list = json.load(f)

# Process
repo_has_copyright = {} # repo_name -> bool
# We only care about repos in non_python_repos

for item in readmes_list:
    repo = item.get('sample_repo_name')
    if repo not in non_python_repos:
        continue
    
    content = item.get('content', '')
    if content is None:
        content = ''
    
    # Check for copyright
    # Simple check: 'copyright' case-insensitive
    has_copyright = 'copyright' in content.lower()
    
    # Also check for (c) or ©?
    # Usually "Copyright" is enough, but let's be slightly more robust if needed.
    # But usually questions like this rely on the word "Copyright".
    # Let's stick to "copyright" case-insensitive for now. 
    # If the text has "(c) 2013", it often also says "Copyright". 
    # If I miss "©" without "Copyright", it might be a small error.
    
    if repo not in repo_has_copyright:
        repo_has_copyright[repo] = has_copyright
    else:
        # If we already saw this repo, and it didn't have copyright, but this file does, update it.
        if not repo_has_copyright[repo] and has_copyright:
            repo_has_copyright[repo] = True

total_repos = len(repo_has_copyright)
repos_with_copyright = sum(1 for v in repo_has_copyright.values() if v)

proportion = repos_with_copyright / total_repos if total_repos > 0 else 0

print(f"Total non-python repos with README: {total_repos}")
print(f"Repos with copyright in README: {repos_with_copyright}")
print(f"Proportion: {proportion}")

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-633006030965842401': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-6293145715309141115': 'file_storage/function-call-6293145715309141115.json', 'var_function-call-9987823125710353733': 'file_storage/function-call-9987823125710353733.json'}

exec(code, env_args)
