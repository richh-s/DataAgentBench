code = """import json

# Get the file path from the previous tool result
file_path = locals()['var_function-call-16205692850786819155']

with open(file_path, 'r') as f:
    repos = json.load(f)

# Extract repo names
# The file contains a list of strings directly, based on my previous thought (preview showed ["repo1", "repo2"...])
# Wait, let's verify the file content format from the preview.
# Preview: ["jitsi/jipopro", "NuGet/json-ld.net", ...]
# So it is a list of strings.
repo_names = repos

# Create SQL list
# Escape single quotes just in case (replace ' with '')
repo_list_str = ", ".join([f"'{r.replace('\'', '\'\'')}'" for r in repo_names])

query = f"""
SELECT COUNT(*) 
FROM commits 
WHERE repo_name IN ({repo_list_str})
  AND message IS NOT NULL
  AND LENGTH(message) < 1000
  AND LOWER(message) NOT LIKE 'merge%'
  AND LOWER(message) NOT LIKE 'update%'
  AND LOWER(message) NOT LIKE 'test%'
"""

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-4123773394754128272': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-4123773394754129877': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-17526777643317543344': 'file_storage/function-call-17526777643317543344.json', 'var_function-call-16205692850786819155': 'file_storage/function-call-16205692850786819155.json'}

exec(code, env_args)
