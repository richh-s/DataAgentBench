code = """import json

# Load languages
with open(locals()['var_function-call-1672906937517553520'], 'r') as f:
    languages = json.load(f)

# Identify non-Python repos
# Check if "Python" appears in language_description
non_python_repos = set()
for entry in languages:
    desc = entry.get('language_description', '')
    if 'Python' not in desc:
        non_python_repos.add(entry['repo_name'])

# Load readmes
with open(locals()['var_function-call-5095110927782742149'], 'r') as f:
    readmes = json.load(f)

# Filter readmes to those in non_python_repos
target_readmes = []
for entry in readmes:
    repo = entry.get('sample_repo_name')
    if repo in non_python_repos:
        target_readmes.append(entry.get('content', ''))

# Count copyright
total_readmes = len(target_readmes)
copyright_count = 0

for content in target_readmes:
    if content:
        content_lower = content.lower()
        # Search for "copyright" or the symbol "©"
        if 'copyright' in content_lower or '©' in content_lower:
            copyright_count += 1

proportion = 0.0
if total_readmes > 0:
    proportion = copyright_count / total_readmes

print("__RESULT__:")
print(json.dumps({
    "total_readmes_in_non_python": total_readmes,
    "copyright_found": copyright_count,
    "proportion": proportion
}))"""

env_args = {'var_function-call-1672906937517553520': 'file_storage/function-call-1672906937517553520.json', 'var_function-call-1672906937517555443': 'file_storage/function-call-1672906937517555443.json', 'var_function-call-5642452289215253424': {'non_python_repo_count': 2774729, 'readme_count': 101, 'copyright_count': 15, 'proportion': 0.1485148514851485}, 'var_function-call-11065072480230208605': [{'total_rows': '24286', 'readme_count': '204'}], 'var_function-call-5095110927782742149': 'file_storage/function-call-5095110927782742149.json'}

exec(code, env_args)
