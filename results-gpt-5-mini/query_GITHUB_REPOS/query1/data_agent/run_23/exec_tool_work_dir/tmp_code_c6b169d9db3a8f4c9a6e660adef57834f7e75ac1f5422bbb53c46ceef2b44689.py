code = """import json, re

# Load the list of non-Python repo names
with open(var_call_oyHW3L9OQYmZr1DP8Rap8ITX, 'r') as f:
    non_py_list = json.load(f)
non_py_repos = set(d['repo_name'] for d in non_py_list)

# Load README contents
with open(var_call_a7uNhHUN25aoQZTxjqhzuuZs, 'r') as f:
    contents = json.load(f)

# Filter contents to only those from non-Python repos
readmes = [c for c in contents if c.get('sample_repo_name') in non_py_repos]

# Define patterns indicating copyright information
pattern = re.compile(r'copyright|©|\(c\)|all rights reserved', re.IGNORECASE)

total = len(readmes)
count = 0
for r in readmes:
    txt = r.get('content') or ''
    if pattern.search(txt):
        count += 1

proportion = None
percentage = None
if total > 0:
    proportion = round(count / total, 6)
    percentage = round(proportion * 100, 4)

result = {
    'total_readme_files': total,
    'readmes_with_copyright': count,
    'proportion': proportion,
    'percentage': percentage
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oyHW3L9OQYmZr1DP8Rap8ITX': 'file_storage/call_oyHW3L9OQYmZr1DP8Rap8ITX.json', 'var_call_a7uNhHUN25aoQZTxjqhzuuZs': 'file_storage/call_a7uNhHUN25aoQZTxjqhzuuZs.json'}

exec(code, env_args)
