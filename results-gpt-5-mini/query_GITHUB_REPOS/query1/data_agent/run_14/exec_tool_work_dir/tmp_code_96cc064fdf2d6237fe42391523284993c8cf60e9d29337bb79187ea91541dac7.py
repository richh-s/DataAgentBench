code = """import json, os, re

# Load the query results from the stored JSON file paths
with open(var_call_zyMq5UoU7qXiQM6xakep8ECH, 'r') as f:
    non_py_repos = json.load(f)  # list of dicts with repo_name

with open(var_call_26h4cDEbWcoiCRhpmNWOpHl4, 'r') as f:
    contents = json.load(f)  # list of dicts with sample_repo_name, sample_path, content, repo_data_description

# Build set of non-Python repo names
non_py_set = set(r['repo_name'] for r in non_py_repos)

# Function to get basename
def basename(path):
    return os.path.basename(path) if path is not None else ''

# Regex to detect copyright: 'copyright', © symbol, or (c)
pattern = re.compile(r'copyright|©|\(c\)', flags=re.IGNORECASE)

# Iterate through contents and find README.md files belonging to non-Python repos
readme_files = []
for row in contents:
    repo = row.get('sample_repo_name')
    path = row.get('sample_path')
    if repo in non_py_set and path:
        if basename(path).lower() == 'readme.md':
            readme_files.append(row)

# Denominator: number of README.md files for non-Python repos
denominator = len(readme_files)

# Numerator: how many of these contain copyright info
numerator = 0
examples = []
for row in readme_files:
    content = row.get('content') or ''
    # Some content fields may contain the string 'None' or be non-text; ensure it's a string
    if isinstance(content, str):
        if pattern.search(content):
            numerator += 1
            if len(examples) < 5:
                examples.append({'sample_repo_name': row.get('sample_repo_name'), 'sample_path': row.get('sample_path')})

proportion = (numerator / denominator) if denominator > 0 else None

result = {
    'numerator': numerator,
    'denominator': denominator,
    'proportion': proportion,
    'examples_of_matches': examples
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zyMq5UoU7qXiQM6xakep8ECH': 'file_storage/call_zyMq5UoU7qXiQM6xakep8ECH.json', 'var_call_26h4cDEbWcoiCRhpmNWOpHl4': 'file_storage/call_26h4cDEbWcoiCRhpmNWOpHl4.json'}

exec(code, env_args)
