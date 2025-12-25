code = """import json

# Load languages
with open(locals()['var_function-call-1672906937517553520'], 'r') as f:
    languages_data = json.load(f)

# Load contents (READMEs)
with open(locals()['var_function-call-1672906937517555443'], 'r') as f:
    readmes_data = json.load(f)

# Identify non-Python repos
non_python_repos = set()
for entry in languages_data:
    repo = entry['repo_name']
    desc = entry['language_description']
    # Check if Python is mentioned
    # "Python" could be part of a word, but in language descriptions it's usually distinct.
    # However, to be safe, we can look for "Python (" or "Python," or just "Python" if we trust the format.
    # Given the format "Language (bytes)", "Python" will be followed by space or punctuation.
    if 'Python' not in desc:
        non_python_repos.add(repo)

# Filter READMEs for non-Python repos
target_readmes = []
for entry in readmes_data:
    repo = entry['sample_repo_name']
    if repo in non_python_repos:
        target_readmes.append(entry['content'])

# Count copyright
total_readmes = len(target_readmes)
copyright_count = 0

for content in target_readmes:
    if content is None:
        continue
    content_lower = content.lower()
    if 'copyright' in content_lower:
        copyright_count += 1

proportion = 0.0
if total_readmes > 0:
    proportion = copyright_count / total_readmes

print("__RESULT__:")
print(json.dumps({
    "non_python_repo_count": len(non_python_repos),
    "readme_count": total_readmes,
    "copyright_count": copyright_count,
    "proportion": proportion
}))"""

env_args = {'var_function-call-1672906937517553520': 'file_storage/function-call-1672906937517553520.json', 'var_function-call-1672906937517555443': 'file_storage/function-call-1672906937517555443.json'}

exec(code, env_args)
