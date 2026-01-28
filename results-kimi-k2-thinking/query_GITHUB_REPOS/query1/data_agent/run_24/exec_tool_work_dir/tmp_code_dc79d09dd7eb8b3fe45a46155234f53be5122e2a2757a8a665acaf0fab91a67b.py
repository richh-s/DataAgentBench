code = """import json
import re

# Load language data
with open('var_functions.query_db:0', 'r') as f:
    languages_data = json.load(f)

# Load README.md content data
with open('var_functions.query_db:2', 'r') as f:
    readme_data = json.load(f)

# Step 1: Identify repositories that use Python
python_repos = set()
all_repos = set()

for item in languages_data:
    repo_name = item['repo_name']
    language_description = item['language_description'].lower()
    all_repos.add(repo_name)
    
    # Check if Python is mentioned in the language description
    if 'python' in language_description:
        python_repos.add(repo_name)

# Step 2: Identify repositories that do NOT use Python
non_python_repos = all_repos - python_repos

# Step 3: Filter README.md files for non-Python repositories
non_python_readmes = []
for item in readme_data:
    repo_name = item['sample_repo_name']
    if repo_name in non_python_repos:
        non_python_readmes.append({
            'repo_name': repo_name,
            'content': item.get('content', '') or ''
        })

# Step 4: Check for copyright information in README content
copyright_indicators = [
    r'copyright', r'\bcopyright\b', r'©', r'\(c\)', r'\bcopr\b',
    r'all rights reserved', r'rights reserved'
]

def has_copyright(content):
    if not content:
        return False
    content_lower = content.lower()
    for indicator in copyright_indicators:
        if re.search(indicator, content_lower, re.IGNORECASE):
            return True
    return False

total_readmes = len(non_python_readmes)
readmes_with_copyright = 0

for readme in non_python_readmes:
    if has_copyright(readme['content']):
        readmes_with_copyright += 1

# Step 5: Calculate proportion
proportion = readmes_with_copyright / total_readmes if total_readmes > 0 else 0

result = {
    'total_non_python_repos_with_readme': total_readmes,
    'readmes_with_copyright': readmes_with_copyright,
    'proportion': proportion,
    'percentage': proportion * 100
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
