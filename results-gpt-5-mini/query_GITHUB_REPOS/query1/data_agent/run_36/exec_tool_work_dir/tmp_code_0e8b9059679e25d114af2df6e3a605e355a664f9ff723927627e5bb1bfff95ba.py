code = """import json, re

# Load the non-Python repo list (stored as a JSON file path in the provided variable)
with open(var_call_rN5BhDxG0vIzlSVM0cc8y3CC, 'r', encoding='utf-8') as f:
    non_python_repos_list = json.load(f)

with open(var_call_DL4GDRfPQgmJbHxtswRVITLM, 'r', encoding='utf-8') as f:
    contents_list = json.load(f)

# Build set of repo names that do not use Python
non_python_repos = set()
for r in non_python_repos_list:
    name = r.get('repo_name')
    if name:
        non_python_repos.add(name)

# Filter README.md contents that belong to non-Python repos
readmes = [c for c in contents_list if c.get('sample_repo_name') in non_python_repos]

# Define detection for copyright info
def has_copyright(text):
    if not text:
        return False
    t = text.lower()
    if 'copyright' in t:
        return True
    if 'all rights reserved' in t:
        return True
    if '©' in text:
        return True
    if '(c)' in t:
        return True
    return False

total = len(readmes)
with_copyright = sum(1 for r in readmes if copyright_text := r.get('content') and (1 if has_copyright(r.get('content')) else 0))

proportion = (with_copyright / total) if total > 0 else None

result = {
    'total_readme_files_in_non_python_repos': total,
    'readme_files_with_copyright': with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rN5BhDxG0vIzlSVM0cc8y3CC': 'file_storage/call_rN5BhDxG0vIzlSVM0cc8y3CC.json', 'var_call_DL4GDRfPQgmJbHxtswRVITLM': 'file_storage/call_DL4GDRfPQgmJbHxtswRVITLM.json'}

exec(code, env_args)
