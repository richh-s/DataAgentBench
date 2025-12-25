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

# Filter READMEs for non-Python repos
# Deduplicate by repo_name. Use the first one found.
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

env_args = {'var_function-call-1903000112947810567': 'file_storage/function-call-1903000112947810567.json', 'var_function-call-6426268876323897969': 'file_storage/function-call-6426268876323897969.json', 'var_function-call-11435390623773592546': {'total_non_python_repos': 2774729, 'repos_with_readme': 101, 'repos_with_copyright': 15, 'proportion': 0.1485148514851485}, 'var_function-call-7479995353690718165': [{'count_star()': '24286'}], 'var_function-call-12233106141421077653': [{'count_star()': '133'}], 'var_function-call-163315687997329742': 'file_storage/function-call-163315687997329742.json'}

exec(code, env_args)
