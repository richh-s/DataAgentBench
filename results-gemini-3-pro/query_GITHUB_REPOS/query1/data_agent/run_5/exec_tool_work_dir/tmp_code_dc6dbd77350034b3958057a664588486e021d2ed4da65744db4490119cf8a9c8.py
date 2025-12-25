code = """import json

# Load languages
with open(locals()['var_function-call-1903000112947810567'], 'r') as f:
    languages_data = json.load(f)

# Identify non-Python repos
non_python_repos = set()
for entry in languages_data:
    repo = entry.get('repo_name')
    desc = entry.get('language_description', '')
    if repo and 'Python' not in desc:
        non_python_repos.add(repo)

# Load READMEs
with open(locals()['var_function-call-163315687997329742'], 'r') as f:
    readmes_data = json.load(f)

# Filter READMEs for non-Python repos (keep all files)
target_readmes = []
for entry in readmes_data:
    repo = entry.get('sample_repo_name')
    if repo in non_python_repos:
        target_readmes.append(entry)

# Calculate proportion
total_readmes = len(target_readmes)
readmes_with_copyright = 0

for entry in target_readmes:
    content = entry.get('content')
    if content and 'copyright' in content.lower():
        readmes_with_copyright += 1

proportion = 0
if total_readmes > 0:
    proportion = readmes_with_copyright / total_readmes

print("__RESULT__:")
print(json.dumps({
    "total_readmes": total_readmes,
    "readmes_with_copyright": readmes_with_copyright,
    "proportion": proportion
}))"""

env_args = {'var_function-call-1903000112947810567': 'file_storage/function-call-1903000112947810567.json', 'var_function-call-6426268876323897969': 'file_storage/function-call-6426268876323897969.json', 'var_function-call-11435390623773592546': {'total_non_python_repos': 2774729, 'repos_with_readme': 101, 'repos_with_copyright': 15, 'proportion': 0.1485148514851485}, 'var_function-call-7479995353690718165': [{'count_star()': '24286'}], 'var_function-call-12233106141421077653': [{'count_star()': '133'}], 'var_function-call-163315687997329742': 'file_storage/function-call-163315687997329742.json', 'var_function-call-6780347969567941599': {'total_non_python_repos': 2774729, 'repos_with_readme': 105, 'repos_with_copyright': 16, 'proportion': 0.1523809523809524}}

exec(code, env_args)
