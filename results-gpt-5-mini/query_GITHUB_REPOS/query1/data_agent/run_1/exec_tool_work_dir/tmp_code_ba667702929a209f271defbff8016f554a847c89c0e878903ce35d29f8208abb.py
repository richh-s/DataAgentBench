code = """import json, re

# Load previous tool results (they may be file paths or direct lists)
try:
    data_non_py = var_call_MUT55vXGXc2qPd05LzHkmel9
except NameError:
    data_non_py = None
try:
    data_contents = var_call_LgAXodjJvWihWYKTuUgiNPTC
except NameError:
    data_contents = None

def load_data(x):
    if x is None:
        return []
    if isinstance(x, str):
        # It's a filepath to a JSON file
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return x

non_py_list = load_data(data_non_py)
contents_list = load_data(data_contents)

non_py_set = set()
for item in non_py_list:
    # Each item should have 'repo_name'
    rn = item.get('repo_name') if isinstance(item, dict) else None
    if rn:
        non_py_set.add(rn)

# Filter contents for README.md files (case-insensitive)
readme_md_entries = []
for c in contents_list:
    path = c.get('sample_path') if isinstance(c, dict) else None
    if not path:
        continue
    if path.lower().endswith('readme.md'):
        readme_md_entries.append(c)

# Consider only those in non-python repos
readme_md_non_py = [c for c in readme_md_entries if c.get('sample_repo_name') in non_py_set]

# Unique repos with README.md
unique_repos_with_readme = set(c.get('sample_repo_name') for c in readme_md_non_py if c.get('sample_repo_name'))
repos_with_readme_count = len(unique_repos_with_readme)

# Detect copyright using keywords
pattern = re.compile(r'copyright|©|\(c\)', re.I)
repos_with_copyright = set()
for c in readme_md_non_py:
    repo = c.get('sample_repo_name')
    content = c.get('content')
    if not content or not isinstance(content, str):
        continue
    if pattern.search(content):
        repos_with_copyright.add(repo)

num_with_copyright = len(repos_with_copyright)
proportion = None
if repos_with_readme_count > 0:
    proportion = num_with_copyright / repos_with_readme_count

result = {
    'non_python_repos_total': len(non_py_set),
    'repos_with_readme_md': repos_with_readme_count,
    'repos_with_copyright_in_readme_md': num_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MUT55vXGXc2qPd05LzHkmel9': 'file_storage/call_MUT55vXGXc2qPd05LzHkmel9.json', 'var_call_LgAXodjJvWihWYKTuUgiNPTC': 'file_storage/call_LgAXodjJvWihWYKTuUgiNPTC.json'}

exec(code, env_args)
