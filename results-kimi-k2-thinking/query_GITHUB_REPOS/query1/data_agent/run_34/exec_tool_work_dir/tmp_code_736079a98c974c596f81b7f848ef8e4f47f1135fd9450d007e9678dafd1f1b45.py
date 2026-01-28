code = """import json
import pandas as pd
import re

# Load languages data
languages_path = var_functions.query_db_0
with open(languages_path, 'r') as f:
    languages_data = json.load(f)

df_languages = pd.DataFrame(languages_data)
df_languages['has_python'] = df_languages['language_description'].str.contains('Python', case=False, na=False)

repos_without_python = set(df_languages[~df_languages['has_python']]['repo_name'].tolist())

# Load README data
readme_path = var_functions.query_db_10
with open(readme_path, 'r') as f:
    readme_data = json.load(f)

df_readmes = pd.DataFrame(readme_data)

# Filter to non-Python repos only
df_readmes_filtered = df_readmes[df_readmes['sample_repo_name'].isin(repos_without_python)]

# Check for copyright
def has_copyright(content):
    if not content:
        return False
    patterns = [
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
    for pattern in patterns:
        if re.search(pattern, content_str, re.IGNORECASE):
            return True
    return False

df_readmes_filtered['has_copyright'] = df_readmes_filtered['content'].apply(has_copyright)

total = len(df_readmes_filtered)
with_copyright = df_readmes_filtered['has_copyright'].sum()
proportion = with_copyright / total if total > 0 else 0

result = {
    'total_readmes': total,
    'with_copyright': int(with_copyright),
    'proportion': float(proportion)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_repos': 3325634, 'repos_with_python': 550905, 'repos_without_python': 2774729, 'repos_without_python_list': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'status': 'setup complete', 'repos_without_python_count': 2774729}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
