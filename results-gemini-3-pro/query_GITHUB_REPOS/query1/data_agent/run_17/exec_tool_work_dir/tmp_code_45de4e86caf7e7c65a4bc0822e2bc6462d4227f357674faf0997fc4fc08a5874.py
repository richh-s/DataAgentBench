code = """import json

# Load languages
with open(locals()['var_function-call-2946045897821113260'], 'r') as f:
    languages_data = json.load(f)

# Identify non-Python repos
non_python_repos = set()
for item in languages_data:
    desc = item.get('language_description', '')
    # Check if 'Python' is present as a whole word or part of the language listing.
    # Given the format "Language (bytes)", "Python" usually appears capitalized.
    # We'll check for "Python" string.
    if desc and 'Python' not in desc:
        non_python_repos.add(item['repo_name'])

# Load contents (READMEs)
with open(locals()['var_function-call-12726813032886270267'], 'r') as f:
    readme_data = json.load(f)

# Filter READMEs for non-Python repos
# We use a set of seen repos to avoid duplicates if multiple READMEs exist per repo (though query filtered by path='README.md')
# However, if there are duplicates in the DB, we should handle them.
# The question asks "proportion of their README.md files".
# If a repo has one README, it counts once.
# If I have multiple entries for the same repo (maybe different commits? sample_ref?), I should probably deduplicate by repo.
# The table description says "sample_repo_name". It doesn't explicitly say distinct repos.
# But usually we analyze the HEAD or a sample.
# Let's count files. "what proportion of their README.md files".
# If I deduplicate by repo, I answer "what proportion of non-Python repos have a README with copyright".
# If I count files, I answer "what proportion of README files belonging to non-Python repos have copyright".
# The phrasing "proportion of their README.md files" suggests counting files.
# But usually there is 1 per repo.
# I will process the list as is.

filtered_readmes = []
for item in readme_data:
    repo = item.get('sample_repo_name')
    if repo in non_python_repos:
        filtered_readmes.append(item)

# Count copyright
total = len(filtered_readmes)
copyright_count = 0
for item in filtered_readmes:
    content = item.get('content', '')
    if content and 'copyright' in content.lower():
        copyright_count += 1

proportion = 0.0
if total > 0:
    proportion = copyright_count / total

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-16476119959139784129': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-9280870360935075941': 'file_storage/function-call-9280870360935075941.json', 'var_function-call-2946045897821113260': 'file_storage/function-call-2946045897821113260.json', 'var_function-call-12726813032886270267': 'file_storage/function-call-12726813032886270267.json'}

exec(code, env_args)
