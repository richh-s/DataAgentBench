code = """import json
import pandas as pd
import re

# Load the languages data to identify repos without Python
languages_path = var_functions.query_db_0
with open(languages_path, 'r') as f:
    languages_data = json.load(f)

df_languages = pd.DataFrame(languages_data)
df_languages['has_python'] = df_languages['language_description'].str.contains('Python', case=False, na=False)

# Get list of repos without Python
repos_without_python = set(df_languages[~df_languages['has_python']]['repo_name'].tolist())

print(f'Total repositories: {len(df_languages)}')
print(f'Repositories without Python: {len(repos_without_python)}')

# Load the README data
readme_path = var_functions.query_db_10
with open(readme_path, 'r') as f:
    readme_data = json.load(f)

df_readmes = pd.DataFrame(readme_data)
print(f'Total READMEs retrieved: {len(df_readmes)}')

# Filter READMEs to only those from repos without Python
df_readmes_filtered = df_readmes[df_readmes['sample_repo_name'].isin(repos_without_python)].copy()
print(f'READMEs from repos without Python: {len(df_readmes_filtered)}')

# Check for copyright information in README content
def has_copyright(content):
    if not content:
        return False
    # Look for copyright patterns
    copyright_patterns = [
        r'copyright\s+[©©]\s+\d{4}',
        r'copyright\s+\d{4}',
        r'©\s+\d{4}',
        r'©\s+\d{4}-\d{4}',
        r'copyright\s+[©©]?\s*\d{4}\s+\w+',
        r'copyright\s+(c|C)\s+\d{4}',
        r'Copyright\s+[©©]\s*\d{4}',
        r'Copyright\s+\d{4}',
        r'Copyright\s+(c|C)\s+\d{4}'
    ]
    
    content_str = str(content).lower()
    for pattern in copyright_patterns:
        if re.search(pattern, content_str, re.IGNORECASE):
            return True
    return False

# Apply the copyright check
df_readmes_filtered['has_copyright'] = df_readmes_filtered['content'].apply(has_copyright)

# Calculate statistics
total_readmes = len(df_readmes_filtered)
readmes_with_copyright = df_readmes_filtered['has_copyright'].sum()
proportion = readmes_with_copyright / total_readmes if total_readmes > 0 else 0

print(f'Total READMEs from non-Python repos: {total_readmes}')
print(f'READMEs with copyright: {readmes_with_copyright}')
print(f'Proportion: {proportion:.4f}')

# Show some examples of READMEs with copyright
examples_with_copyright = df_readmes_filtered[df_readmes_filtered['has_copyright']].head(3)
print('\nExamples with copyright:')
for idx, row in examples_with_copyright.iterrows():
    print(f"\n--- {row['sample_repo_name']} ---")
    print(f"Path: {row['sample_path']}")
    print(f"Content snippet: {str(row['content'])[:200]}...")

# Show some examples without copyright
examples_without_copyright = df_readmes_filtered[~df_readmes_filtered['has_copyright']].head(3)
print('\n\nExamples without copyright:')
for idx, row in examples_without_copyright.iterrows():
    print(f"\n--- {row['sample_repo_name']} ---")
    print(f"Path: {row['sample_path']}")
    print(f"Content snippet: {str(row['content'])[:200]}...")

result = {
    'total_repos_without_python': len(repos_without_python),
    'total_readmes_from_non_python_repos': total_readmes,
    'readmes_with_copyright': int(readmes_with_copyright),
    'proportion': float(proportion)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_repos': 3325634, 'repos_with_python': 550905, 'repos_without_python': 2774729, 'repos_without_python_list': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'status': 'setup complete', 'repos_without_python_count': 2774729}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
