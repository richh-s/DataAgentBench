code = """import json

# Access the stored results
lang_data = locals()['var_functions.query_db:0']
readme_data = locals()['var_functions.query_db:2']

# Step 1: Identify repos that do not use Python
non_python_repos = set()
for item in lang_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description'].lower()
    # Check if 'python' is mentioned in the language description
    if 'python' not in lang_desc:
        non_python_repos.add(repo_name)

# Step 2: Filter README files from non-Python repos and check for copyright
copyright_indicators = ['copyright', '©', 'all rights reserved']
readme_count = 0
copyright_count = 0

for item in readme_data:
    repo_name = item['sample_repo_name']
    content = item['content'] or ''  # Handle null content
    
    if repo_name in non_python_repos:
        readme_count += 1
        # Check for copyright information (case-insensitive)
        content_lower = content.lower()
        has_copyright = any(indicator in content_lower for indicator in copyright_indicators)
        
        if has_copyright:
            copyright_count += 1

# Calculate proportion
proportion = copyright_count / readme_count if readme_count > 0 else 0

final_result = {
    'total_non_python_readmes': readme_count,
    'readmes_with_copyright': copyright_count,
    'proportion': proportion,
    'proportion_percentage': f"{proportion:.2%}"
}

print('__RESULT__:')
print(json.dumps(final_result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
