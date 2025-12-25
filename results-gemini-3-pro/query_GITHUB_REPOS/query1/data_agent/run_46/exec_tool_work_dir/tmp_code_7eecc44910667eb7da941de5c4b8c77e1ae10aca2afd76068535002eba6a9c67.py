code = """import json

# Load data
with open(locals()['var_function-call-17316050141868196047'], 'r') as f:
    repos_list = json.load(f)

with open(locals()['var_function-call-3366446698735946739'], 'r') as f:
    readme_files = json.load(f)

with open(locals()['var_function-call-8828968465635628992'], 'r') as f:
    contents_list = json.load(f)

# Process repos
# Repos list contains all non-python repos.
non_python_repos = set(item['repo_name'] for item in repos_list)

# Process contents
# Create a dict mapping id to has_copyright
# The query result has "True"/"False"/None as strings or booleans depending on JSON parsing
# Let's inspect one to be sure, but generally safe to check for truthiness
contents_map = {}
for item in contents_list:
    val = item['has_copyright']
    # It might be string "True" or boolean True
    if str(val).lower() == 'true':
        contents_map[item['id']] = True
    else:
        contents_map[item['id']] = False

# Calculate
total_count = 0
copyright_count = 0

# We iterate over readme files
# If a file is in a non-python repo, we check its content
for item in readme_files:
    repo = item['repo_name']
    blob_id = item['id']
    
    if repo in non_python_repos:
        # Check if we have content for this blob
        if blob_id in contents_map:
            total_count += 1
            if contents_map[blob_id]:
                copyright_count += 1

proportion = 0.0
if total_count > 0:
    proportion = copyright_count / total_count

print("__RESULT__:")
print(json.dumps({
    "total_readmes_checked": total_count,
    "copyright_readmes": copyright_count,
    "proportion": proportion
}))"""

env_args = {'var_function-call-2607864808049419873': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-8444357205340828073': 'file_storage/function-call-8444357205340828073.json', 'var_function-call-10172226988217569572': [{'count_star()': '524077'}], 'var_function-call-10205520039209315791': [{'count_star()': '24286'}], 'var_function-call-17316050141868196047': 'file_storage/function-call-17316050141868196047.json', 'var_function-call-3366446698735946739': 'file_storage/function-call-3366446698735946739.json', 'var_function-call-8828968465635628992': 'file_storage/function-call-8828968465635628992.json'}

exec(code, env_args)
