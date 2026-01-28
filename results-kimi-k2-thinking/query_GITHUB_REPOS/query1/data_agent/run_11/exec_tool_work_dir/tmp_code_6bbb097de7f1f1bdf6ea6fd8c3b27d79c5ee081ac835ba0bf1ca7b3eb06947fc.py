code = """import json
import os

# Load languages data
lang_file = var_functions.query_db_19
with open(lang_file, 'r') as f:
    languages_data = json.load(f)

# Filter for repos that do not use Python
non_python_repos = []
for item in languages_data:
    lang_desc = item['language_description'].lower()
    if 'python' not in lang_desc:
        non_python_repos.append(item['repo_name'])

# Load README contents data
readme_file = var_functions.query_db_14
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

# Filter READMEs for non-Python repos
copyright_indicators = ['copyright', '©', 'all rights reserved', 'licensed under']
results = []

total_readmes = 0
copyright_readmes = 0

for readme_item in readme_data:
    repo_name = readme_item['sample_repo_name']
    content = readme_item.get('content', '') or ''
    
    if repo_name in non_python_repos:
        total_readmes += 1
        
        # Check for copyright information
        content_lower = content.lower()
        has_copyright = any(indicator in content_lower for indicator in copyright_indicators)
        
        if has_copyright:
            copyright_readmes += 1
            results.append({
                'repo_name': repo_name,
                'has_copyright': True,
                'content_preview': content[:200] if len(content) > 200 else content
            })
        else:
            results.append({
                'repo_name': repo_name,
                'has_copyright': False,
                'content_preview': content[:200] if len(content) > 200 else content
            })

# Calculate proportion
proportion = 0.0
if total_readmes > 0:
    proportion = copyright_readmes / total_readmes

print('__RESULT__:')
print(json.dumps({
    'total_readmes_non_python': total_readmes,
    'copyright_readmes': copyright_readmes,
    'proportion': proportion,
    'sample_results': results[:10]  # Include a sample of results
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json'}

exec(code, env_args)
