code = """# Read the full README data from the file
readme_file = locals()['var_functions.query_db:20']

import json
import re

with open(readme_file, 'r') as f:
    readme_data = json.load(f)

# Count total README files
total_readme = len(readme_data)

# Count README files with copyright information
copyright_pattern = re.compile(r'(copyright|©|Copyright)', re.IGNORECASE)
has_copyright = 0
for record in readme_data:
    if 'content' in record and record['content']:
        if copyright_pattern.search(record['content']):
            has_copyright += 1

# Also count sample records for debugging
sample_records = []
for record in readme_data[:5]:
    sample_records.append({
        'repo_name': record.get('sample_repo_name'),
        'has_copyright': copyright_pattern.search(record['content']) is not None if record.get('content') else False
    })

result = {
    'total_readme_files': total_readme,
    'copyright_count': has_copyright,
    'proportion_with_copyright': has_copyright / total_readme if total_readme > 0 else 0,
    'sample_records': sample_records
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.list_db:2': ['languages', 'repos', 'licenses'], 'var_functions.list_db:4': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'total_repos': '400000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [{'total_readme': '195'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
