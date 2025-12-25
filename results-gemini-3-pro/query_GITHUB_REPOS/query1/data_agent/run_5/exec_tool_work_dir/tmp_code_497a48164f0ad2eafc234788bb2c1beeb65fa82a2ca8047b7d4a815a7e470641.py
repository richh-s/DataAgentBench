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
with open(locals()['var_function-call-6426268876323897969'], 'r') as f:
    readmes_data = json.load(f)

# Filter READMEs for non-Python repos
# We will store them in a dictionary to deduplicate by repo_name
# If multiple READMEs exist for a repo (e.g. different refs), we'll just take the first one found.
repo_readme_content = {}
for entry in readmes_data:
    repo = entry.get('sample_repo_name')
    content = entry.get('content')
    if repo in non_python_repos:
        if repo not in repo_readme_content:
             repo_readme_content[repo] = content

# Calculate proportion
total_repos_with_readme = len(repo_readme_content)
repos_with_copyright = 0

for repo, content in repo_readme_content.items():
    if content and 'copyright' in content.lower():
        repos_with_copyright += 1

proportion = 0
if total_repos_with_readme > 0:
    proportion = repos_with_copyright / total_repos_with_readme

print("__RESULT__:")
print(json.dumps({
    "total_non_python_repos": len(non_python_repos),
    "repos_with_readme": total_repos_with_readme,
    "repos_with_copyright": repos_with_copyright,
    "proportion": proportion
}))"""

env_args = {'var_function-call-1903000112947810567': 'file_storage/function-call-1903000112947810567.json', 'var_function-call-6426268876323897969': 'file_storage/function-call-6426268876323897969.json'}

exec(code, env_args)
