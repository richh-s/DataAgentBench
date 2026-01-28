code = """import json
import os

# Load data from previous tool results. The variables are provided by the tool storage.
# var_call_K0C8Sr0o7NvHNabNHn0Q51fI: languages query result (possibly a path to a .json file)
# var_call_2tHZjnTqU1AI3z2KquC7VnW9: contents query result (possibly a path to a .json file)

def load_storage(var):
    # If var is a string, assume it's a path to a .json file; otherwise it's already a Python object list
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

langs = load_storage(var_call_K0C8Sr0o7NvHNabNHn0Q51fI)
contents = load_storage(var_call_2tHZjnTqU1AI3z2KquC7VnW9)

# Build set of repos that do NOT use Python (case-insensitive check on language_description)
non_python_repos = set()
for r in langs:
    repo = r.get('repo_name')
    desc = r.get('language_description') or ''
    if 'python' not in desc.lower():
        non_python_repos.add(repo)

# Filter contents for README.md files in those repos
readmes = []
for c in contents:
    repo = c.get('sample_repo_name')
    path = c.get('sample_path') or ''
    if not repo or not path:
        continue
    if repo in non_python_repos and path.lower().endswith('readme.md'):
        readmes.append(c)

# Function to detect copyright-like text
def has_copyright_text(s):
    if not isinstance(s, str):
        return False
    low = s.lower()
    if 'copyright' in low:
        return True
    if '©' in s:
        return True
    if 'all rights reserved' in low:
        return True
    return False

total = len(readmes)
with_copyright = sum(1 for r in readmes if has_copyright_text(r.get('content')))

proportion = None
if total > 0:
    proportion = with_copyright / total

result = {
    'total_readme_md_files_in_non_python_repos': total,
    'readme_md_files_with_copyright': with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NjMZAWFjj94SErWhWexTjZnY': ['languages', 'repos', 'licenses'], 'var_call_13a2jC5dSDqxec1GQdYRajLV': ['commits', 'contents', 'files'], 'var_call_K0C8Sr0o7NvHNabNHn0Q51fI': 'file_storage/call_K0C8Sr0o7NvHNabNHn0Q51fI.json', 'var_call_2tHZjnTqU1AI3z2KquC7VnW9': 'file_storage/call_2tHZjnTqU1AI3z2KquC7VnW9.json'}

exec(code, env_args)
